import json
import shortuuid
from models import MessageFeedback
from db.db_manager import get_db_session
from models.db_models import MessageStore, User
from langchain_core.messages import HumanMessage


def get_mistake_messages(session_id: str) -> list[HumanMessage]:
    with get_db_session() as db:
        results = db.query(MessageStore).join(MessageFeedback,MessageStore.id == MessageFeedback.message_id).filter(
            MessageStore.session_id == session_id,
            MessageFeedback.is_correct == False
        ).all()

        return [
            HumanMessage(content=json.loads(msg.message).get("data", {}).get("content"))
            for msg in results
        ]

def get_last_message_id(session_id: str) -> int | None:
    with get_db_session() as db:
        messages = db.query(MessageStore).filter(
            MessageStore.session_id == session_id
        ).order_by(MessageStore.id.desc()).all()

        for message in messages:
            msg_data = json.loads(message.message)
            if msg_data.get("type") == "human":
                return message.id

    return None

def add_mistake_entry(session_id,ai_message):
    with get_db_session() as db:
        feedback = MessageFeedback(message_id = get_last_message_id(session_id),
                                    session_id=session_id,
                                    is_correct=ai_message.is_correct
                                    )

        db.add(feedback)
        db.commit()


def get_or_create_user(user_name :str) -> User:
    """
    fetch user by name or create one
    """
    with get_db_session() as db:
        user = db.query(User).filter_by(user_name=user_name).first()
        if user:
            return user

        session_id = shortuuid.uuid()
        new_user = User(user_name=user_name, session_id=session_id)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user
    

def update_user_profile(user: User, target_lang: str, target_lvl: str, native_lang: str, know_eng: bool) -> User:
    """
    update user's language profile.
    """
    with get_db_session() as db:
        user_in_db = db.query(User).filter_by(user_id=user.user_id).first()
        if not user_in_db:
            raise ValueError("User not found.")

        user_in_db.target_lang = target_lang
        user_in_db.target_lvl = target_lvl
        user_in_db.native_lang = native_lang
        user_in_db.know_eng = know_eng

        db.commit()
        db.refresh(user_in_db)

        return user_in_db