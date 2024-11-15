import json
import numpy as np
import re
from flask import Flask, request, jsonify

# initialize the flask app
app = Flask(__name__)

# load the model parameters
with open("models/naive_bayes_model.json", "r") as file:
    model_params = json.load(file)

spam_prior = model_params["spam_prior"]
not_spam_prior = model_params["not_spam_prior"]
spam_likelihood = np.array(model_params["spam_likelihood"])
not_spam_likelihood = np.array(model_params["not_spam_likelihood"])
feature_names = model_params["feature_names"]

# preprocess plain text email
def preprocess_plain_text(email_text):
    # clean the text: remove non-alphabetic characters and convert to lowercase
    email_text = re.sub(r"[^a-zA-Z]", " ", email_text).lower()

    # tokenize the text into words
    tokens = email_text.split()

    # count the occurrences of each word in the vocabulary
    word_counts = np.zeros(len(feature_names))
    for word in tokens:
        if word in feature_names:
            word_index = feature_names.index(word)
            word_counts[word_index] += 1

    return word_counts

# predict function
def predict_email(email_features):
    # calculate the log-probabilities for spam and not spam
    spam_score = np.log(spam_prior) + np.sum(email_features * np.log(spam_likelihood))
    not_spam_score = np.log(not_spam_prior) + np.sum(email_features * np.log(not_spam_likelihood))

    # return the class with the higher score
    return "Spam" if spam_score > not_spam_score else "Not Spam"

# define the classify endpoint
@app.route("/classify", methods=["POST"])
def classify():
    try:
        # get the email text from the request
        email_text = request.json.get("text", "")
        if not email_text:
            return jsonify({"error": "Email text is required"}), 400

        # preprocess the email
        email_features = preprocess_plain_text(email_text)

        # classify the email
        prediction = predict_email(email_features)

        # return the result
        return jsonify({"classification": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# run the flask app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
