## This file is used to call the saved best performing GPT2 model for use in the front end GUI

from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

# path to the fine tuned model
FINE_TUNED_MODEL_PATH = "./gpt2-finetuned-email-summary"

class Summarizer:

    def __init__(self, path=FINE_TUNED_MODEL_PATH):
        # load tokenizer and model
        self.tokenizer = GPT2Tokenizer.from_pretrained(path)
        self.model = GPT2LMHeadModel.from_pretrained(path) 

    def summarize(self, email, verbose=False):
        # tokenize the input
        inputs = self.tokenizer(email, return_tensors="pt")

        # generate the output
        with torch.no_grad():
            outputs = self.model.generate(
                inputs["input_ids"],
                max_length=100, 
                num_beams=5,    
                no_repeat_ngram_size=2,  
                early_stopping=True 
            )

        # decode and print the generated text
        output_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        if verbose:
            print('output ', output_text)
        
        return output_text



# hold_on = Summarizer(path="dddd")

# test_input = "Owen, I miss and love you so much. I hope you are doing well and I look forward to sailing with you."

# hold_on.summarize(test_input, verbose=True)
    