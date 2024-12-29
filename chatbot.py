import os
import nltk
import ssl
import random 
import json
import ssl
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download('punkt')


with open('intents.json', 'r') as file:
    intents = json.load(file)


vectorizer = TfidfVectorizer()
clf = LogisticRegression(random_state=0, max_iter=10000)

tags=[]
patterns=[]
for intent in intents:
    for pattern in intent['patterns']:
         tags.append(intent['tag'])
         patterns.append(pattern)

x = vectorizer.fit_transform(patterns)
y= tags
clf.fit(x,y)


def chat_bot(input_text):
    input_text= vectorizer.transform([input_text])
    tag = clf.predict(input_text)[0]
    for intent in intents:
        if intent['tag']==tag:
            response=random.choice(intent['responses'])
            return response
        

            



# counter = 0 
# def main():
#     global counter
#     st.title("Intents of Chatbot using NLP")
#     # creating side bar
#     menue=["Home", "Converssation History","About"]
#     choice =st.sidebar.selectbox("Menue",menue)

# #Home 
#     if choice == "Home":
#         st.write("Welcome to the chatbot . Please type massage and press Enter to start conversatoin")

#         if not os.path.exists("chat_log.csv"):
#             with open ("chat_log.csv","w",newline='',encoding='utf-8') as csvfile:
#                 csv_writer = csv.writer(csvfile)
#                 csv_writer.writerow(['User Input','Chatbot Response','Timestamp'])

#         counter+=1
#         user_input= st.text_input("You",key=f"user_input_(counter)")

#         if user_input:

#     #Convert the user input to a string
#             user_input_str = str(user_input)

#             response = chat_bot(user_input)
#             st.text_area("Chatbot:",value=response, height=120, max_chars=None, key=f"chatbot")


#     #Get the current timestamp
#             timestamp  = datetime.datetime.now().strftime(f"%Y-%m-%d %H:%M:%S")


#     # Save the user input and chatbot response to the chat_log.csv file

#             with open('chat_log.csv' ,'a',newline='', encoding='utf-8') as csvfile:
#                  csv_writer = csv.writer(csvfile)
#                  csv_writer.writerow([user_input_str,response,timestamp])

#             if response.lower() in ['goodbye','bye']:
#                 st.write("Thank you to chatting with me. Have a greate day!")
#                 st.stop()

# #Conversatoin History Menu
#     elif choice == "Conversation History":
#     #Display the conversation history in a collapsible exander
#         st.header("Conversation History")
# #with st.beta_expender("Click to see conversatoin history"):
#         with open ('chat_log.csv','r',encoding='utf-8') as csvfile:
#             csv_reader= csv.reader(csvfile)
#             next(csv_reader) #Skip the header row
#             for row in csv_reader:
#                 st.text(f"User: (row[0])")
#                 st.text(f"Chatbot: (row[1])")
#                 st.text(f"Timestamp: (row[2])")
#                 st.text(f"User: (row[3])")
#                 st.markdown("---")

#     elif choice== "About":
#          st.write("The goal of this project to create a chatbot that can understand and resonce on give text")
#          st.subheader("Project Overview:")

#          st.write("""This chatbot project is a conversational AI system designed to understand and respond to user queries. 
#                 Built using Python, Natural Language Processing (NLP) techniques, and the Logistic Regression algorithm, 
#                 the chatbot provides a user-friendly interface through the Streamlit web framework.""")

#          st.header("Key Achievements")
#          st.subheader(" 1. NLP Techniques:")
#          st.write(" This chatbot effectively utilizes NLP techniques to understand user input.")
#          st.subheader(" 2. Logistic Regression Algorithm:")
#          st.write(" The Logistic Regression algorithm is successfully employed to classify user input.")
#          st.subheader(" 3. Streamlit Web Framework:")
#          st.write("The Streamlit web framework provides an intuitive and interactive interface.")
#          st.subheader(" 4. User Input Understanding:")
#          st.write("This chatbot project successfully understands user input.")
#          st.subheader(" 5. Suitable Response Generation:")
#          st.write("The project generates suitable responses to user queries")
             
#          st.header("Future Scope")
#          st.subheader(" 1. Intent Identification:")
#          st.write(" Incorporating intent identification capabilities will improve the chatbot's understanding of user input")
#          st.subheader(" 2. Emotion Detection:")
#          st.write("Adding emotion detection capabilities will enable the chatbot to understand user emotions.")
#          st.subheader(" 3. Multi-Language Support:")
#          st.write(" Incorporating multi-language support will allow the chatbot to understand user input in various languages.")

# if __name__ =='__main__':
#     main()