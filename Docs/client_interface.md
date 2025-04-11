
---

##  Client Interface Documentation – CLI Chatbot


A Python command-line interface (CLI) client that allows users to interact with the language learning chatbot server. It handles login, profile setup, chat interaction, and fetching mistake overviews.

---

###  Running the Client


#### 1. **Run the Client**
```bash
python client.py
```

---

### How It Works

#### Step 1: Login
User is prompted to enter a username. The client sends a `POST` request to `/login`.

- If the user is new, a user is created.
- If the profile is incomplete, it proceeds to profile setup.

---

#### Step 2: Profile Setup (if required)
User is prompted for:
- Target language to learn
- Proficiency level (Beginner / Intermediate / Advanced / Fluent)
- Native language
- Whether they speak English

Data is sent to the server via `POST /profile/update`.

---

#### Step 3: Chat Interface

Once profile is ready, the chatbot is activated. User can:
- Send any message to the AI assistant
- Type `END` to exit and receive a summary overview of mistakes

**Each message flow:**
- Client sends `POST` to `/chat`
- Receives `reply`, `translation`, and correctness feedback
- Feedback is displayed inline with emoji indicators (✅/❌)

---

#### Step 4: Mistake Overview

When user types `END`, a summary is retrieved via `GET /overview` and printed in the terminal.

---

### Configuration

- **Base URL:** Defined in the script as `http://localhost:5000`
  - Change this if deploying the server remotely:
  ```python
  BASE_URL = "https://your-deployed-server.com"
  ```

---

