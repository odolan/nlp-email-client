from openai import OpenAI
import re

class GPTClassifier:
    def __init__(self, api_key):
        # initialize client with API key
        self.client = OpenAI(api_key=api_key)

    def preprocess_plain_text(self, email_text):
        # clean the text: remove non-alphabetic characters and convert to lowercase
        email_text = re.sub(r"[^a-zA-Z]", " ", email_text).lower()
        return email_text

    def predict_email(self, email_text):
        try:
            # prompt messages
            messages = [
                {"role": "system", "content": "You are an email classifier. Classify emails as 'Spam' or 'Not Spam'."},
                {"role": "user", "content": f"Email: {email_text}"}
            ]

            # get a response from GPT client given messages and emaik
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                response_format={"type": "text"},
                temperature=0,
                max_tokens=10,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            # extract the content of the classification
            classification = response.choices[0].message.content
            return classification
        except Exception as e:
            return f"Error in classification: {str(e)}"

    def classify(self, email):
        preprocessed_email = self.preprocess_plain_text(email)
        return self.predict_email(preprocessed_email)
