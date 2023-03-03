#OpenAi Created By AI

import openai
openai.api_key = "YOUR_API_KEY"

def openai_request(prompt, model, max_tokens=1024, temperature=0.7):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature
    )

    return response.choices[0].text.strip()

def get_response(message):
    prompt = f"User: {message}\nAI:"
    response = openai_request(prompt, "davinci")
    return response

while True:
    message = input("User: ")
    response = get_response(message)
    print("AI: " + response)
