from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS from flask-cors
from backend.models.summarizer.run_summarizer_t5 import Summarizer
from backend.models.classifier.run_classifier import Classifier

"""
to run this file run the following from the root directory in terminal:

python -m backend.api.app 
"""

# initialize the flask app
app = Flask(__name__)
# apply cors to allow web access
CORS(app)

# load the models
summarizer = Summarizer()
classifier = Classifier()

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

# run the flask app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
