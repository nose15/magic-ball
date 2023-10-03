from . import http_methods


class GPTClient:
    messages = []

    def __init__(self, model, system_prompt="You are a chatbot"):
        self.model = model
        system_message = {
            "role": "system",
            "content": system_prompt
        }
        self.messages.append(system_message)

    def complete_chat(self, message):
        user_message = {
            "role": "user",
            "content": message
        }

        self.messages.append(user_message)

        payload = {
            "model": self.model,
            "messages": self.messages
        }

        response = http_methods.http_post(payload)

        self.messages.append(response)

        return response["content"]
