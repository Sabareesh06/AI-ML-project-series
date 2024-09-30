from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from flask import Flask, request, jsonify

# Step 1: Initialize chatbot
admission_bot = ChatBot(
    'CollegeAdmissionBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
    ],
    database_uri='sqlite:///admission_db.sqlite3'  # database to store chat history
)

# Step 2: Train the bot with admission-related Q&A
trainer = ListTrainer(admission_bot)

# Basic training data for admissions
training_data = [
    "What is the admission process?",
    "The admission process involves filling out the online application, submitting required documents, and attending an interview.",
    "What are the admission requirements?",
    "You need a high school diploma, letters of recommendation, and proof of English proficiency.",
    "When is the application deadline?",
    "The application deadline is June 30th for the fall semester.",
    "What documents are required for admission?",
    "You need to submit your high school transcripts, personal statement, and letters of recommendation.",
    "How do I apply for financial aid?",
    "You can apply for financial aid by filling out the FAFSA form on the college's website.",
    "What is the fee for the admission application?",
    "The application fee is $50, payable online.",
]

trainer.train(training_data)

# Step 3: Create a Flask app for chatbot interaction
app = Flask(__name__)

# Memory to store previous user interactions (context)
user_context = {}

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    user_id = request.json.get("user_id")
    
    # Retrieve previous context if available
    if user_id in user_context:
        context = user_context[user_id]
    else:
        context = ""

    # Generate bot response
    bot_response = admission_bot.get_response(user_message)
    
    # Simple context management for remembering information
    if "deadline" in user_message.lower():
        context = "deadline"
    elif "documents" in user_message.lower():
        context = "documents"
    
    # Save context for future interaction
    user_context[user_id] = context
    
    # If bot can't answer, provide feedback
    if float(bot_response.confidence) < 0.5:
        bot_response = "I'm sorry, I don't have the information you're asking for. Please contact the admissions office."

    return jsonify({"response": str(bot_response)})

# Step 4: Error handling for unanswerable queries
@app.errorhandler(500)
def handle_500_error(exception):
    return jsonify({"response": "An error occurred. Please try asking another question."}), 500

# Step 5: Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
