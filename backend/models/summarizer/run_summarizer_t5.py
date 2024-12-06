## This file is used to call the saved best performing t5 model for use in the front end GUI

from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

# path to the fine tuned model
FINE_TUNED_MODEL_PATH = "backend/models/summarizer/saved_t5_summary_model"

class Summarizer:

    def __init__(self, path=FINE_TUNED_MODEL_PATH):

        self.device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

        # load the fine tuned model for testing
        self.model = T5ForConditionalGeneration.from_pretrained(path)
        self.tokenizer = T5Tokenizer.from_pretrained(path)
        self.model.to(self.device)

    def summarize(self, email, verbose=False):
        
        # generate a summary for a test email
        inputs = self.tokenizer(email, return_tensors="pt", max_length=512, truncation=True).to(self.device)
        outputs = self.model.generate(inputs["input_ids"], max_length=150, num_beams=2, early_stopping=True)

        if verbose: 
            print("Generated Summary:")
            print(self.tokenizer.decode(outputs[0], skip_special_tokens=True))

        output = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        return output

    