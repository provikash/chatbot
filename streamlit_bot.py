import os
import csv
import datetime
from typing import Literal, TypeAlias
from dataclasses import dataclass
from sklearn.metrics import accuracy_score, classification_report
import streamlit.components.v1 as components
import streamlit as st
from chatbot import chat_bot, X_test,y_test,clf

@dataclass
class Message:
    """Class for keeping track of a chat message."""
    origin: Literal["human", "ai"]
    message: str

def load_css():
    try:
         with open("static/style.css", "r") as f:
            css = f"<style>{f.read()}</style>"
            st.markdown(css, unsafe_allow_html=True)
    except FileNotFoundError: st.error("CSS file not found.") 
    except Exception as e: st.error(f"An error occurred: {e}")

def initialize_session_state():
    if "history" not in st.session_state:
        st.session_state.history = []

def on_click_callback():
    human_prompt = st.session_state.human_prompt
    response = chat_bot(human_prompt)
    st.session_state.history.append(Message("human", human_prompt))
    st.session_state.history.append(Message("ai", response))

load_css()



    # creating side bar
menue=["🏠Home","🕓Chat History","📊Model Evaluation","📝About"]
choice =st.sidebar.selectbox("Menue",menue)

 # Initialize chat history
  
if os.path.exists('chat_log.csv'):
            with open('chat_log.csv', 'r', newline='', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)
                next(csv_reader)
                for row in csv_reader:
                    st.write(f"**User**: {row[0]}\n**Chatbot**: {row[1]}\n*Time*: {row[2]}")

else :
    'chat_history' not in st.session_state
    st.session_state['chat_history'] = []





 
if choice == "🏠Home":
   
    
    initialize_session_state()
    st.title("GlobeGuru 🤖 ")
    st.write(" Ask me anythink relared travel 😀 ")

    chat_placeholder = st.container()
    prompt_placeholder = st.form("Chat-form")

 
    

    with chat_placeholder:
        for chat in st.session_state.history:
            div = f"""
    <div class="chat-row
        {'' if chat.origin =='ai' else 'row-reverse'}">
        <img class="chat-icon" src="app/static/{
            'ai_icon.png' if chat.origin == 'ai'
                        else 'user_icon.png'}
            "width=32 height=32>
        <div class="chat-bubble
        {'ai-bubble' if chat.origin == 'ai' else 'human-bubble'}">
            &#8203;{chat.message}
        </div>
    </div>
        """
            st.markdown(div, unsafe_allow_html=True)
            
            
        for _ in range(3):
            st.markdown("")

    with prompt_placeholder:
        st.markdown("Chat")
        cols = st.columns((6, 1))
        cols[0].text_input("chat", value="Hello bot", label_visibility="collapsed", key="human_prompt",)
        cols[1].form_submit_button("Submit", type="primary", on_click=on_click_callback,)





        components.html("""
    <script>
    const streamlitDoc = window.parent.document;

    const buttons = Array.from(
        streamlitDoc.querySelectorAll('.stButton > button')
    );
    const submitButton = buttons.find(
        el => el.innerText === 'Submit'
    );

    streamlitDoc.addEventListener('keydown', function(e) {
        switch (e.key) {
            case 'Enter':
                submitButton.click();
                break;
        }
    });
    </script>
    """, 
        height=0,
        width=0,
    )
        
elif choice == "🕓Chat History":
        st.subheader("📜 Conversation History")
        st.write("Below is a record of your recent conversations with the chatbot.")
        if st.session_state['chat_history']:
            for chat in st.session_state['chat_history'][-5:]:
                st.write(f"**💬 You:** {chat['user']}")
                st.write(f"**🤖 Chatbot:** {chat['chatbot']}")
                st.write(f"**⏱ Timestamp:** {chat['timestamp']}")
                st.markdown("---")
            if st.button("🗑️ Clear History"):
                st.session_state['chat_history'] = []
                st.success("Chat history cleared!")
        else:
            st.info("📂 No chat history available.")

elif choice == "📊Model Evaluation":
        st.subheader("📊 Model Performance Evaluation")
        st.write("Evaluate the performance of the Intent-Based Chatbot.")
        model_accuracy = accuracy_score(y_test, clf.predict(X_test))
        classification_rep = classification_report(y_test, clf.predict(X_test))
        st.write(f"📈 **Model Accuracy:** {model_accuracy * 100:.2f}%")
        st.write("### 🛠 Classification Report")
        st.text(classification_rep)

elif choice== "📝About":
         st.write("The goal of this project to create a chatbot that can understand and resonce on give text")
         st.subheader("Project Overview:")

         st.write("""This chatbot project is a conversational AI system designed to understand and respond to user queries. 
                Built using Python, Natural Language Processing (NLP) techniques, and the Logistic Regression algorithm, 
                the chatbot provides a user-friendly interface through the Streamlit web framework.""")

         st.header("Key Achievements")
         st.subheader(" 1. NLP Techniques:")
         st.write(" This chatbot effectively utilizes NLP techniques to understand user input.")
         st.subheader(" 2. Logistic Regression Algorithm:")
         st.write(" The Logistic Regression algorithm is successfully employed to classify user input.")
         st.subheader(" 3. Streamlit Web Framework:")
         st.write("The Streamlit web framework provides an intuitive and interactive interface.")
         st.subheader(" 4. User Input Understanding:")
         st.write("This chatbot project successfully understands user input.")
         st.subheader(" 5. Suitable Response Generation:")
         st.write("The project generates suitable responses to user queries")
             
         st.header("Future Scope")
         st.subheader(" 1. Intent Identification:")
         st.write(" Incorporating intent identification capabilities will improve the chatbot's understanding of user input")
         st.subheader(" 2. Emotion Detection:")
         st.write("Adding emotion detection capabilities will enable the chatbot to understand user emotions.")
         st.subheader(" 3. Multi-Language Support:")
         st.write(" Incorporating multi-language support will allow the chatbot to understand user input in various languages.")

