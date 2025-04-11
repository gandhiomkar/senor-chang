

# Señor Chang 
### Language Learning Chatbot (CLI + API)

---

A multi-user, stateless chatbot designed to help people learn any language through realistic, scenario-based conversations. Built using LangChain, OpenAI, and a lightweight Flask API, the chatbot gathers information about the user's target language, native language, and skill level, then sets a contextual scene (e.g., ordering food, booking a hotel) to simulate real-world dialogue. During the conversation, the bot provides corrections, tracks user mistakes, and offers a final review of weak areas. The application features a command-line interface (CLI) client and is designed to be easily extended with a web UI in the future.

---

##  Features

-  **Stateless, multi-user architecture**
-  **Natural Language conversation**
-  **Scene setting** for contextual dialogue (e.g., coffee shop, travel, etc.)
-  **Profile-based personalization** (target language, level, native language, etc.)
-  **Interactive CLI chatbot** with translation and feedback
-  **AI-powered responses** using OpenAI GPT
-  **Mistake overview** to guide further learning
-  Modular design (API backend + CLI client + ready for frontend integration)

---

#### Tech Stack
- **Python**
- **LangChain**
- **OpenAI API**
- **Flask**

---

#### Setup Instructions

  - API guide
  - Client Interface guide

1. **Clone the repository**
   ```bash
   git clone https://github.com/gandhiomkar/senor-chang.git
   cd senor-chang
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your OpenAI API key**

   Create a `.env` file or directly set your environment variable:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

5. **Add Prompt templates**
   Add prompt templates to prompt/ with following structure
   ```
   prompt/
    - chat_prompt.txt
    - chat_intro.txt
    - mistake_overview_prompt.txt
    ```
    Example templates:
    ```
    chat_prompt.txt

    You are a helpful and friendly language instructor.

    Your job is to help the user learn and practice {target_language} by having simple, conversational roleplay based on real-life situations.

    The user is fluent in {native_language}. You may use {native_language} to clarify explanations when needed, but keep most of the conversation in {target_language}.

    Start by offering the user a few scenarios to choose from, such as:
    1. Ordering food at a restaurant
    2. Asking for directions
    3. Booking a hotel room
    4. Shopping in a store
    5. Casual conversation with a stranger

    Once the user picks a scenario, begin the conversation in {target_language} as if it were happening in real life. 
    Correct the user's mistakes gently and explain why something is wrong using simple language. 
    Encourage the user to respond in the target language.

    Be kind, patient, and encouraging throughout.

    ```

    ```
    chat_intro.txt
    Hello! 👋 Ready to practice your {target_language} skills?

    Please choose a conversation scenario:
    6. 🍽️ Ordering food at a restaurant
    7. 🗺️ Asking for directions
    8. 🏨 Booking a hotel room
    9. 🛍️ Shopping in a store
    10. 💬 Making small talk

    Type the number of the scenario you want to try!

    ```

    ```
    mistake_overview_prompt.txt

    You are a professional language instructor.

    The user has just completed a conversation practice session in {target_language}. 
    They are fluent in {user_native_lang}, so your summary and suggestions should be written in {user_native_lang}.

    Your task is to:
    - Provide an overview of the most common or important mistakes the user made
    - Offer clear, constructive feedback
    - Include short explanations and examples when possible
    - Suggest specific areas or topics the user should study or practice more

    Keep your tone helpful, encouraging, and supportive. 
    Make the user feel confident and motivated to keep learning.

    ```

6. **Run the chatbot**
   ```bash
   python main.py
   ```

---

#### How It Works
- **LangChain** manages the conversation flow and chaining of prompts.
- **OpenAI GPT** handles the natural language processing and generation.
- The user sends a message → LangChain builds context and prompts → GPT returns a language learning response.

---

#### Example


---

#### 📌 Notes
- This chatbot is a prototype and can be extended with web UI, user progress trackin.
- Designed with modularity in mind for easy scaling and updates.

