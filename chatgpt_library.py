# Import the necessary libraries for ChatGPT API interaction
import openai

#OPENAI_API_KEY
OPENAI_API_KEY = 'my_open_ai_key'

def chatgpt_simplified_explanation(mixtral_output):
    # Use the OpenAI ChatGPT API to generate simplified explanations using the Feynman Technique
    prompt = f"Given the explanation: '{mixtral_output}', please use the Feynman Technique to explain in a simple, intuitive way."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100
    )

    return response.choices[0].text.strip()
