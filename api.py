import os

import anthropic
import openai
from dotenv import load_dotenv

assert load_dotenv(), "Failed to load .env file"


def call_model(agent_instruction, conversation, model_name):
    if model_name.startswith("gpt-"):
        return call_gpt(agent_instruction, conversation, model_name)
    if model_name.startswith("mistral-") or model_name.startswith("ministral-"):
        return call_mistral(agent_instruction, conversation, model_name)
    if model_name.startswith("claude-"):
        return call_anthropic(agent_instruction, conversation, model_name)
    raise Exception(f"Model {model_name} not supported")


def call_gpt(agent_instruction, conversation, model_name):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.base_url = "https://api.openai.com/v1"
    messages = [{"role": "system", "content": agent_instruction}]
    for role, text in conversation:
        messages.append({"role": role, "content": text})
    response = openai.chat.completions.create(
        model=model_name,
        messages=messages,
    )
    return response.choices[0].message.content


def call_mistral(agent_instruction, conversation, model_name):
    openai.api_key = os.getenv("MISTRAL_API_KEY")
    openai.base_url = "https://api.mistral.ai/v1/"
    messages = [{"role": "system", "content": agent_instruction}]
    for role, text in conversation:
        messages.append({"role": role, "content": text})
    response = openai.chat.completions.create(
        model=model_name,
        messages=messages,
    )
    return response.choices[0].message.content


def call_anthropic(agent_instruction, conversation, model_name):
    client = anthropic.Anthropic()
    messages = [{"role": "system", "content": agent_instruction}]
    for role, text in conversation:
        messages.append({"role": role, "content": text})
    message = client.messages.create(
        model=model_name,
        messages=messages,
        max_tokens=250,
    )
    return message.content
