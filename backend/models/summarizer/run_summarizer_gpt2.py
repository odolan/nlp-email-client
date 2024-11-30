# Import dependencies
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

# path to the fine tuned model
FINE_TUNED_MODEL_PATH = "./gpt2-finetuned-email-summary"

# class Summarizer 
class Summarizer:

    def __init__(self, path=FINE_TUNED_MODEL_PATH):
        # Load tokenizer and model
        self.tokenizer = GPT2Tokenizer.from_pretrained(path)
        self.model = GPT2LMHeadModel.from_pretrained(path)

    def summarize(self, email, verbose=False):

        # Tokenize the input
        inputs = self.tokenizer(email, return_tensors="pt")

        # Generate the output (model prediction)
        with torch.no_grad():
            outputs = self.model.generate(
                inputs["input_ids"],
                max_length=100,  # Maximum length of the generated text
                num_beams=5,    # Beam search for better results
                no_repeat_ngram_size=2,  # Avoid repetition
                early_stopping=True      # Stop generating early if end is reached
            )

        # Decode and print the generated text
        output_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        if verbose:
            print('output ', output_text)
        
        return output_text



# hold_on = Summarizer(path="dddd")

# test_input = "Owen, I miss and love you so much. I hope you are doing well and I look forward to sailing with you."

# hold_on.summarize(test_input, verbose=True)
    