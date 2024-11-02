import requests
import json

url = "https://openai.jadve.com/chatgpt"

headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en",
    "content-type": "application/json",
    "origin": "https://jadve.com",
    "referer": "https://jadve.com/",
    "sec-ch-ua": '"Chromium";v="130", "Brave";v="130", "Not?A_Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}

payload = {
    "action": "sendmessage",
    "model": "gpt-4o",
    "messages": [{"role": "user", "content": "Can you code python?"}],
    "temperature": 0.7,
    "language": "en",
    "returnTokensUsage": True,
    "botId": "guest-chat",
    "chatId": ""
}

response = requests.post(url, headers=headers, json=payload, stream=True)
#print(response.text)

# Initialize variables to accumulate the response
response_text = ""
full_content = ""

# Read the streamed response in chunks
for line in response.iter_lines():
    if line:
        decoded_line = line.decode('utf-8')
        if decoded_line.startswith("data:"):
            # Remove the "data:" prefix
            json_data = decoded_line[len("data:"):].strip()
            if json_data:
                # Parse the JSON data
                chunk = json.loads(json_data)
                if "choices" in chunk:
                    for choice in chunk["choices"]:
                        if "delta" in choice and "content" in choice["delta"]:
                            full_content += choice["delta"]["content"]

print(response.status_code)
print(full_content)
