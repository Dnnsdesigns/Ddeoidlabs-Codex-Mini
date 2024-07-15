# load_pretrained_model.py
from transformers import AutoModelForCausalLM, AutoTokenizer

def load_model_and_tokenizer():
    model_name = "gpt-3"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return model, tokenizer
