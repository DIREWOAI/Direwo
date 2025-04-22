import os
import gradio as gr
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("hugging_face_api_key")

def chat_with_ai(message):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistralai/mixtral-8x7b",  # Or try: openchat/openchat-7b
        "messages": [{"role": "user", "content": message}]
    }
    response = requests.post(url, headers=headers, json=data)
    try:
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {str(e)}\n{response.text}"

gr.Interface(fn=chat_with_ai, inputs="text", outputs="text", title="Direwo AI Chatbot").launch()
