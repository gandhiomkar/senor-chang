from flask import Flask, request, jsonify
from utils import get_or_create_user, update_user_profile
from ai.ai_model import get_ai_response, getMistakeOverview
from models import User
from db.db_manager import get_db_session

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username", "").strip().lower()
    if not username:
        return jsonify({"error": "Username is required"}), 400

    user = get_or_create_user(username)

    profile_complete = user.target_lang is not None

    if profile_complete:
        return jsonify({
            "user_id": user.user_id,
            "username": user.user_name,
            "session_id": user.session_id,
            "profile_complete": True,
            "target_lang": user.target_lang,
            "target_lvl": user.target_lvl,
            "native_lang": user.native_lang,
            "know_eng": user.know_eng
        })
    else:
        return jsonify({
            "user_id": user.user_id,
            "username": user.user_name,
            "session_id": user.session_id,
            "profile_complete": False
        })


# check if profile is complete
@app.route('/profile/complete', methods=['GET'])
def is_profile_complete():
    session_id = request.args.get("session_id")
    if not session_id:
        return jsonify({"error": "Session ID is required"}), 400

    with get_db_session() as db:
        user = db.query(User).filter_by(session_id=session_id).first()
        if not user:
            return jsonify({"error": "User not found"}), 404

        is_complete = user.target_lang is not None
        return jsonify({"profile_complete": is_complete})


# update profile
@app.route('/profile/update', methods=['POST'])
def update_profile():
    data = request.json
    session_id = data.get("session_id")
    target_lang = data.get("target_lang")
    target_lvl = data.get("target_lvl")
    native_lang = data.get("native_lang")
    know_eng = data.get("know_eng", False)

    with get_db_session() as db:
        user = db.query(User).filter_by(session_id=session_id).first()
        if not user:
            return jsonify({"error": "User not found"}), 404

    updated = update_user_profile(user, target_lang, target_lvl, native_lang, know_eng)
    return jsonify({
        "message": "Profile updated",
        "target_lang": updated.target_lang,
        "target_lvl": updated.target_lvl,
        "native_lang": updated.native_lang,
        "know_eng": updated.know_eng
    })

# chat endpoint
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    session_id = data.get("session_id")
    user_input = data.get("message")

    if not session_id or not user_input:
        return jsonify({"error": "Session ID and message are required"}), 400

    with get_db_session() as db:
        user = db.query(User).filter_by(session_id=session_id).first()
        if not user:
            return jsonify({"error": "User not found"}), 404

    ai_output = get_ai_response(user, user_input)

    return jsonify({
        "reply": ai_output.reply,
        "translation": ai_output.english_translation,
        "is_correct": ai_output.is_correct
    })


# mistake overview
@app.route('/overview', methods=['GET'])
def overview():
    session_id = request.args.get("session_id")

    if not session_id:
        return jsonify({"error": "Session ID is required"}), 400


    with get_db_session() as db:
        user = db.query(User).filter_by(session_id=session_id).first()
        if not user:
            return jsonify({"error": "User not found"}), 404

    overview = getMistakeOverview(user)
    return jsonify({"overview": overview.content})


if __name__ == "__main__":
    app.run(debug=True)
