
# Email Spam Classification and Summarization Project

This project aims to classify emails as **Spam** or **Not Spam** and summarize their content to make them more digestible for users. The goal is to provide a solution that helps users, particularly older adults, quickly identify and understand the nature of their emails.

We explore various machine learning and natural language processing (NLP) models to achieve this:

- **Spam Classification**:
  - **Naive Bayes**: A simple, traditional machine learning approach.
  - **GPT-3.5**: A state-of-the-art language model by OpenAI, fine-tuned for spam classification.
  
- **Email Summarization**:
  - **GPT-2**: An earlier generation of the GPT family, fine-tuned for text summarization.
  - **T5**: A powerful transformer model designed for various text generation tasks, including summarization.

---

## Project Structure
Please reference the below structure to understand how the code functions

```
.
├── backend
│   ├── api
│   │   # contains flask endpoint called by the front end
│   ├── data
│   │   # contains training data for classification and summarization tasks
│   └── models
│       ├── classifier
│       │   ├── compare_classifiers.py
│       │   │   # runs tests between models to determine performance on test set
│       │   ├── naive_bayes_model.json
│       │   │   # saved instance of trained model
│       │   ├── run_classifier.py
│       │   │   # calls saved naive bayes models and gpt for use in API
│       │   └── run_gpt_classifier.py
│       │       # calls saved naive bayes models and gpt for use in API
│       └── summarizer
│           ├── compare_models.py
│           │   # performs human feedback testing on models
│           ├── fine_tune_gpt2_model.py
│           │   # include model training code + hyperparameter adjustments
│           ├── fine_tune_t5_model.py
│           │   # include model training code + hyperparameter adjustments
│           ├── run_summarizer_gpt2.py
│           │   # call saved models for use in API
│           └── run_summarizer_t5.py
│               # call saved models for use in API
└── frontend
    # contains nextJS project which can be run by instructions below

```


## Project Setup
To run this project, follow the steps below:

### 1. Configure Environment

Create a `.env` file in the root of the backend/api direcotry and add your **OpenAI API key**:
```
OPENAI_API_KEY=your_openai_api_key
```

---

## Running the Demo

### Backend Setup
Navigate to the project root directory and start the backend:
```
python -m backend.api.app
```


### Frontend Setup
Navigate to the `frontend` directory and start the frontend:
```
cd frontend
npm run dev
```

### View the Live Site
The live site will be available at:  
[http://localhost:3000](http://localhost:3000)

---

## Video Demonstration

Check out the video demo of this project on YouTube:  
[![Video Demo](https://img.youtube.com/vi/v0918xZb_fY/0.jpg)](https://www.youtube.com/watch?v=v0918xZb_fY)

---

## About This Project

This project was built as part of a service-learning experience in a **Natural Language Processing (NLP) class**. The objective was to learn how to fine-tune and test machine learning models that solve real-world problems, specifically targeting the needs of older adults who may struggle with email management.

By combining modern NLP techniques with practical applications, this project aims to improve accessibility and reduce the cognitive load associated with email communication.

---
