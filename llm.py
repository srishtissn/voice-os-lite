from gpt4all import GPT4All

MODEL_PATH = "models/llama-3.2-1b-instruct-q4_0.gguf"

model = GPT4All(model_name=MODEL_PATH, model_path=".", allow_download=False)

def ask_llm(prompt):
    response = model.generate(prompt, max_tokens=100)
    return response
