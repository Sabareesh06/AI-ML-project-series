import datetime
import re

def greet_user():
    return "Hi buddy! How can I help you today?"

chat_history = {}
user_name = ""

def remember_user_input(question, answer):
    
    chat_history[question.lower()] = answer

def recall_context(question):
    
    question_lower = question.lower()
    for stored_question in chat_history:
        if re.search(re.escape(question_lower), stored_question):
            return f"You previously asked about '{stored_question}', and I responded: {chat_history[stored_question]}"
    return "I don't recall discussing that."

def chatbot_response(user_input):
    global user_name
    user_input = user_input.lower()  

    if "name" in user_input:
        answer = f"I'm Spidy, your virtual assistant."
        remember_user_input("name", answer)
        return answer
    elif "date" in user_input:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        remember_user_input("date", current_date)
        return f"Today's date is {current_date}, {user_name}."
    elif "day" in user_input:
        current_day = datetime.datetime.now().strftime("%A")
        remember_user_input("day", current_day)
        return f"Today is {current_day}, {user_name}."
    elif "joke" in user_input:
        answer = "Maggie is male or female? It's male because it gets ready in 2 minutes."
        remember_user_input("joke", answer)
        return f"{answer}, {user_name}."
    elif "can you do" in user_input or "what do you do" in user_input:
        answer = "I can answer questions, chat with you, and more!"
        remember_user_input("abilities", answer)
        return f"{answer}, {user_name}."
    elif "how are you" in user_input or "how do you feel" in user_input:
        answer = "I'm good, what about you?"
        remember_user_input("how are you", answer)
        return f"{answer}, {user_name}."
    elif "are you doing" in user_input or "what are you up to" in user_input:
        answer = "Nothing special, what about you?"
        remember_user_input("what are you doing", answer)
        return f"{answer}, {user_name}."
    elif user_input in ["hi", "hello", "hey", "greetings"]:
        return f"Hello, {user_name}!"
    elif user_input in ["i'm good", "i'm fine", "i am good", "i am fine", "good", "fine"]:
        return f"Good to hear, {user_name}!"
    elif "recall" in user_input:
        question = input("What would you like me to recall? ")
        return recall_context(question)
    else:
        return handle_error(user_input)

def handle_error(user_input):
    
    if "help" in user_input:
        return "I'm here to assist you! Could you please specify what you need help with?"
    elif "who" in user_input or "what" in user_input:
        return "I can answer various questions! Please try asking something specific."
    else:
        return "I'm sorry, I didn't quite understand that. Could you please rephrase?"

def ask_user_name():
    global user_name
    user_name = input("What's your name? ")
    return user_name

def ask_user():
    questions = [f"How was your day, {user_name}?", f"How can I assist you today, {user_name}?"]
    answers = {}
    for q in questions:
        user_input = input(q + " ")
        answers[q] = user_input 
    return answers

def react_to_answers(answers):
    if "help" in answers[f"How can I assist you today, {user_name}?"].lower():
        return f"Sure, {user_name}, I'm here to help! What do you need?"
    else:
        return f"I'm glad to know more about you, {user_name}!"

def start_chat():
    print(greet_user())
    
    ask_user_name()
    
    user_answers = ask_user()
    print("Chatbot:", react_to_answers(user_answers))

    while True:
        user_input = input(f"You ({user_name}): ").lower()

        farewell_phrases = ["bye", "thanks", "thank you", "goodbye"]
        if any(phrase in user_input for phrase in farewell_phrases):
            print(f"Chatbot: Goodbye, {user_name}! Have a great day!")
            break

        print("Chatbot:", chatbot_response(user_input))

start_chat()
