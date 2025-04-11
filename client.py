import requests

BASE_URL = "http://localhost:5000"  # change if hosted remotely


def login():
    username = input("Enter your username: ").strip().lower()
    response = requests.post(f"{BASE_URL}/login", json={"username": username})

    if response.status_code != 200:
        print("Login failed:", response.json().get("error"))
        exit()

    user_data = response.json()
    print("Logged in as:", user_data["username"])
    return user_data


def check_profile_complete(session_id):
    response = requests.get(f"{BASE_URL}/profile/complete", params={"session_id": session_id})
    return response.json().get("profile_complete", False)


def update_profile(session_id):
    print("Let's complete your profile:")
    target_lang = input("Which language do you want to learn?: ").strip()
    print(f"Your level in {target_lang}?")
    print("1. Beginner\n2. Intermediate\n3. Advanced\n4. Fluent")
    level_map = {'1': 'beginner', '2': 'intermediate', '3': 'advanced', '4': 'fluent'}
    target_lvl = level_map.get(input("Choose number: ").strip(), "beginner")
    native_lang = input("Your native language: ").strip()
    know_eng = input("Do you speak English? (yes/no): ").strip().lower() == 'yes'

    response = requests.post(f"{BASE_URL}/profile/update", json={
        "session_id": session_id,
        "target_lang": target_lang,
        "target_lvl": target_lvl,
        "native_lang": native_lang,
        "know_eng": know_eng
    })

    if response.status_code == 200:
        print("Profile updated.")
    else:
        print("Failed to update profile:", response.json())


def chat_loop(user):
    print("\n Start chatting with your AI instructor! Type 'END' to finish.\n")
    while True:
        msg = input("You: ")
        if msg.strip().upper() == "END":
            print("Getting your mistake overview...")
            overview = requests.get(f"{BASE_URL}/overview", params={"session_id": user['session_id']})
            print("\n Overview:")
            print(overview.json().get("overview", "No overview available"))
            break

        response = requests.post(f"{BASE_URL}/chat", json={
            "session_id": user["session_id"],
            "message": msg
        })

        if response.status_code != 200:
            print(" Chat error:", response.json())
        else:
            res = response.json()
            print(f"AI: {res['reply']} ({res['translation']}) {'✅' if res['is_correct'] else '❌'}")


def main():
    user = login()

    if not user.get("profile_complete"):
        update_profile(user["session_id"])

    chat_loop(user)


if __name__ == "__main__":
    main()
