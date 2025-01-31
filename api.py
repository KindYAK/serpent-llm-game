import os

import openai
from dotenv import load_dotenv

assert load_dotenv(), "Failed to load .env file"

openai.api_key = os.getenv("OPENAI_API_KEY")


def call_model(base_prompt, agent_instruction, conversation, model_name):
    if model_name.startswith("gpt-"):
        print("!!", agent_instruction)
        return call_gpt(base_prompt, agent_instruction, conversation, model_name)
    raise Exception(f"Model {model_name} not supported")


def call_gpt(base_prompt, agent_instruction, conversation, model_name):
    messages = [{"role": "system", "content": base_prompt + " " + agent_instruction}]
    for role, text in conversation:
        messages.append({"role": role, "content": text})
    response = openai.chat.completions.create(
        model=model_name,
        messages=messages,
    )
    return response.choices[0].message.content
