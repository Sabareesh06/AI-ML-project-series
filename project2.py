import nltk
from nltk.chat.util import Chat, reflections


pairs = [
    [
        r"What is the admission process?",
        ["The admission process includes submitting an application form, required documents, and paying the application fee."]
    ],
    [
        r"How can I apply for admission?",
        ["You can apply for admission through the college website or by visiting the admissions office."]
    ],
    [
        r"What are the documents required for admission?",
        ["You need to submit your transcripts, ID proof, and entrance exam score for admission."]
    ],
    [
        r"Is there any entrance exam needed?",
        ["Yes, you are required to take an entrance exam depending on the program."]
    ],
    [
        r"What academic qualifications do I need for admission?",
        ["You need to have passed the relevant pre-requisite exams and meet the minimum score required for the program."]
    ],
    [
        r"What is the last date for applying?",
        ["The last date to apply for admission is June 30th."]
    ],
    [
        r"When is the admission form submission deadline?",
        ["The form submission deadline is June 30th."]
    ],
    [
        r"Is there a late fee for missing the admission deadline?",
        ["Yes, there is a late fee if you miss the deadline. Please check the college website for details."]
    ],
    [
        r"Can I apply online?",
        ["Yes, you can apply online through the college's official website."]
    ],
    [
        r"Where can I find more information about admission?",
        ["You can find more information on the college website or by visiting the admissions office."]
    ]
]


user_context = {}


chatbot = Chat(pairs, reflections)


print("AdmissionBot is ready to help with your admission queries! (Type 'quit' to exit)")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "quit":
        print("AdmissionBot: Goodbye!")
        break
    
    
    if "my name is" in user_input.lower():
        name = user_input.split("my name is")[-1].strip()
        user_context['name'] = name
        print(f"AdmissionBot: Nice to meet you, {name}!")
        continue

    
    response = chatbot.respond(user_input)
    
    
    if response:
        if 'name' in user_context:
            print(f"AdmissionBot: {response}, {user_context['name']}!")
        else:
            print(f"AdmissionBot: {response}")
    else:
        print("AdmissionBot: I'm sorry, but I don't have an answer to that. Please check the college website or rephrase your question.")
