
---

## API Documentation – Flask Server

### Base URL
```http
http://localhost:5000/
```

> Note: For production or deployment, replace with the appropriate server IP or domain.

---

### Authentication
- Stateless authentication is handled via `session_id` for each user.
- Make sure the `session_id` is included in all relevant requests.

---

### Endpoints

---

####  `POST /login`

**Description:**  
Logs in a user (or creates a new one if it doesn’t exist) and checks if the user profile is complete.

**Request Body (JSON):**
```json
{
  "username": "john_doe"
}
```

**Response (JSON):**
- If profile is complete:
```json
{
  "user_id": "abc123",
  "username": "john_doe",
  "session_id": "xyz789",
  "profile_complete": true,
  "target_lang": "Spanish",
  "target_lvl": "Beginner",
  "native_lang": "English",
  "know_eng": true
}
```

- If profile is incomplete:
```json
{
  "user_id": "abc123",
  "username": "john_doe",
  "session_id": "xyz789",
  "profile_complete": false
}
```

---

#### ✅ `GET /profile/complete`

**Description:**  
Checks if the user’s profile is complete.

**Query Parameters:**
```
session_id=xyz789
```

**Response:**
```json
{
  "profile_complete": true
}
```

---

#### `POST /profile/update`

**Description:**  
Updates the user profile with language learning preferences.

**Request Body (JSON):**
```json
{
  "session_id": "xyz789",
  "target_lang": "French",
  "target_lvl": "Intermediate",
  "native_lang": "English",
  "know_eng": true
}
```

**Response:**
```json
{
  "message": "Profile updated",
  "target_lang": "French",
  "target_lvl": "Intermediate",
  "native_lang": "English",
  "know_eng": true
}
```

---

####  `POST /chat`

**Description:**  
Handles the chat interaction between the user and the AI assistant.

**Request Body (JSON):**
```json
{
  "session_id": "xyz789",
  "message": "How do I say 'I am hungry' in French?"
}
```

**Response:**
```json
{
  "reply": "En français, vous dites 'J'ai faim'.",
  "translation": "I am hungry.",
  "is_correct": true
}
```

---

####  `GET /overview`

**Description:**  
Returns an overview of the user's common mistakes or feedback from previous interactions.

**Query Parameters:**
```
session_id=xyz789
```

**Response:**
```json
{
  "overview": "You often confuse verb tenses. Review past perfect vs present perfect."
}
```

---

### ⚠️ Error Responses
- `400 Bad Request`: Missing or invalid parameters (e.g., missing session_id)
- `404 Not Found`: User not found in the system

---
