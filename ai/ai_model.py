from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory 
from custom_types import AI_Response
from langchain_core.messages import HumanMessage,AIMessage
from utils import get_mistake_messages, add_mistake_entry, load_prompt

def get_chat_session():
    system_prompt = load_prompt("prompts/chat_prompt.txt")
    intro_message = load_prompt("prompts/chat_intro.txt")
    template = [( "system",
                system_prompt
            ),
            # No previous chat history on first run
            ("ai", intro_message),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human","{input}")]

    prompt = ChatPromptTemplate.from_messages(template)

    # model = OllamaLLM(model="llama3.1")
    model = ChatOpenAI(model="gpt-4o-mini").with_structured_output(AI_Response)

    chain = prompt | model

    chain_with_message_history = RunnableWithMessageHistory(
        chain,
        lambda session_id:SQLChatMessageHistory(session_id=session_id,connection_string="sqlite:///sqlite.db") ,
        input_messages_key="input",
        history_messages_key="chat_history",
    )
    return chain_with_message_history

historyChain = get_chat_session()


def get_ai_response(user,human_input):
    human_input = HumanMessage(human_input)
    
    # if(human_input.content.strip().upper()=="END"):
    #         return(getMistakeOverview(user).content)
    # print(f"user: {human_input.content}")
    try: 
        ai_message = historyChain.invoke({"target_language":user.target_lang,
                    "native_language":user.native_lang,
                    "input": human_input},config={"configurable":{"session_id":user.session_id}})
    except:
        pass
    # print(f"ai: {ai_message.reply} ({ai_message.english_translation})")
    # ai_response = f"ai: {ai_message.reply} ({ai_message.english_translation})"
    messages = [
        human_input,
        AIMessage(ai_message.reply)
    ]
    chat_message_history = SQLChatMessageHistory(session_id=user.session_id,connection_string="sqlite:///sqlite.db")
    chat_message_history.add_messages(messages)
    add_mistake_entry(user.session_id,ai_message)
    return ai_message


def get_mistake_overview_model_chain():
  
    template = [ (
                "system", load_prompt('prompts/mistake_overview_prompt.txt')
                ),    
                MessagesPlaceholder(variable_name="user_messages"),
             ]

    prompt = ChatPromptTemplate.from_messages(template)

    # model = OllamaLLM(model="llama3.1")
    model = ChatOpenAI(model="gpt-4o-mini")
    chain = prompt | model
    return chain

MistakeOverviewChain = get_mistake_overview_model_chain()

def getMistakeOverview(user):
    mistake_messages = get_mistake_messages(user.session_id)
    output = MistakeOverviewChain.invoke(
        {   "target_language":user.target_lang,
            "user_messages":mistake_messages,
            "user_language_level": user.target_lvl,
            "user_native_lang":user.native_lang
        }
    )
    return output