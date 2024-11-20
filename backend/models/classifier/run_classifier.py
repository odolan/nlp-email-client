import json
import numpy as np
import re

class Classifier:

    def __init__(self):
        with open("backend/models/classifier/naive_bayes_model.json", "r") as file:
            self.model_params = json.load(file)

        self.spam_prior = self.model_params["spam_prior"]
        self.not_spam_prior = self.model_params["not_spam_prior"]
        self.spam_likelihood = np.array(self.model_params["spam_likelihood"])
        self.not_spam_likelihood = np.array(self.model_params["not_spam_likelihood"])
        self.feature_names = self.model_params["feature_names"]


    # preprocess plain text email
    def preprocess_plain_text(self, email_text):
        # clean the text: remove non-alphabetic characters and convert to lowercase
        email_text = re.sub(r"[^a-zA-Z]", " ", email_text).lower()

        # tokenize the text into words
        tokens = email_text.split()

        # count the occurrences of each word in the vocabulary
        word_counts = np.zeros(len(self.feature_names))
        for word in tokens:
            if word in self.feature_names:
                word_index = self.feature_names.index(word)
                word_counts[word_index] += 1

        return word_counts
    

    # predict function
    def predict_email(self, email_features):
        # calculate the log-probabilities for spam and not spam
        spam_score = np.log(self.spam_prior) + np.sum(email_features * np.log(self.spam_likelihood))
        not_spam_score = np.log(self.not_spam_prior) + np.sum(email_features * np.log(self.not_spam_likelihood))

        # return the class with the higher score
        return "Spam" if spam_score > not_spam_score else "Not Spam"
    

    def classify(self, email):

        # preprocess the email
        email_features = self.preprocess_plain_text(email)

        # classify the email
        prediction = self.predict_email(email_features)

        return prediction

