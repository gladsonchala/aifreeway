import requests

class HuggingFaceLLMAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {
            'Content-Type': 'application/json'
        }

    def get_available_models(self):
        url = f"{self.base_url}/api/v1/models"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def chat_completions(self, model=None, messages=None, temperature=None, top_p=None, max_tokens=None, use_cache=None, stream=None):
        url = f"{self.base_url}/api/v1/chat/completions"
        payload = {
            "model": model or "nous-mixtral-8x7b",
            "messages": messages or [{"role": "user", "content": "Hello, who are you?"}],
            "temperature": temperature or 0.5,
            "top_p": top_p or 0.95,
            "max_tokens": max_tokens or -1,
            "use_cache": use_cache or False,
            "stream": stream or True
        }
        response = requests.post(url, json=payload, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 422:
            raise ValueError(response.json())
        else:
            response.raise_for_status()

# Example usage:
base_url = "https://iseehf-hf-llm-api.hf.space"

api = HuggingFaceLLMAPI(base_url)

# Get available models
models = api.get_available_models()
print(models)

# Generate chat completions
completions = api.chat_completions(messages=[{"role": "user", "content": "What is the capital of France?"}])
print(completions)
