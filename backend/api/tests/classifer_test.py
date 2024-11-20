import requests

# test email
email_text = "Congratulations! You've won a free ticket. Claim your prize now."

# make a POST request
response = requests.post("http://localhost:8080/classify", json={"text": email_text})

# print the response
print("Response:", response.json())
