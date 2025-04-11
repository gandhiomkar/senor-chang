

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

5. **Run the chatbot**
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

