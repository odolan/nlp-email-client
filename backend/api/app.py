from flask import Flask, request, jsonify
from flask_cors import CORS 
from dotenv import load_dotenv
import os
from backend.models.summarizer.run_summarizer_t5 import Summarizer
from backend.models.classifier.run_classifier import Classifier
from backend.models.classifier.run_gpt_classifier import GPTClassifier 

"""
to run this file run the following from the root directory in terminal:

python -m backend.api.app 
"""

# load environment variables from the .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# initialize the flask app
app = Flask(__name__)
# apply cors to allow web access
CORS(app)

# load the models
summarizer = Summarizer()
classifier = Classifier()
gpt_classifier = GPTClassifier(api_key=OPENAI_API_KEY) 

# define the classify endpoint
@app.route("/classify", methods=["POST"])
def classify():
    try:
        # get the email text from the request
        email_text = request.json.get("text", "")
        if not email_text:
            return jsonify({"error": "Email text is required"}), 400

        # classify the email as spam or not spam
        prediction = classifier.classify(email_text)

        # return the result
        return jsonify({"classification": prediction}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# define the summarization endpoint
@app.route("/summarize", methods=["POST"])
def summarize():
    try:
        # get the email text from the request
        email_text = request.json.get("text", "")
        if not email_text:
            return jsonify({"error": "Email text is required"}), 400
        
        # summarize the email
        summary = summarizer.summarize(email_text)

        # return the result
        return jsonify({"summary": summary}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# define the GPT classify endpoint
@app.route("/gpt_classify", methods=["POST"])
def gpt_classify():
    try:
        # get the email text from the request
        email_text = request.json.get("text", "")
        if not email_text:
            return jsonify({"error": "Email text is required"}), 400

        # classify the email using GPTClassifier
        prediction = gpt_classifier.classify(email_text)

        # return the result
        return jsonify({"classification": prediction}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# run the flask app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
