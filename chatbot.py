from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import spacy

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
nlp = spacy.load("en_core_web_sm")

# Sample FAQ
faq = {

    "Hi?": "Hi, How can i help you?.",
    "Hello?" : "Hello, How can i help you.",
    "I want to cancel my order?" : "You can cancel your order from My Orders before it is shipped.",
    "What is your return policy?": "Our return policy allows returns within 6 days of purchase.",
    "What are your business hours?": "Our business hours are from 9 AM to 6 PM, Monday to Friday.",
    "How do i track my order?": "You can track your order using the tracking number sent to your email.",
    "What is your shipping policy?" : "We offer free shipping for orders above 500Rupees, and standard shipping rates apply otherwise.",
    "How can i change my password?" : "You can change your password by navigating to your account settings and selecting Change Password.",
    "How to cancel my order?" : "To cancel your order, please contact our support team within 24 hours of placing the order.",
    "When will i get my refund?" : "Refunds usually take 5-7 business days to process after we receive the returned product.",
    "How can i track my order?" : "You can track your order using the link we sent you.",
    "What payment methods do you accept?" : "We accept credit cards, PayPal, UPI and Apple Pay.",

}

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if user_message in faq:
        response_message = faq[user_message]
    else:
        response_message = "I'm sorry, I don't understand that."
    return jsonify({"response": response_message})

if __name__ == '__main__':
    app.run(debug=True)