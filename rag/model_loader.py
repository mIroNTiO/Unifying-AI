from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

def load_local_model(model_name="microsoft/phi-2"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, device=-1)
    return pipe
