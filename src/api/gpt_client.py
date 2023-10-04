from . import http_methods
import time


class GPTClient:
    messages = []
    functions = [
        {
            "name": "close_chat",
            "description": "Close the application when the user ends the conversation",
            "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "The goodbye message from the bot",
                    }
                },
                "required": ["message"],
            },
        }
    ]
    conversation = False

    def __init__(self, model: str, system_prompt="You are a chatbot"):
        self.model = model
        system_message = {
            "role": "system",
            "content": system_prompt
        }
        self.messages.append(system_message)

        self.function_names = {"close_chat": self.close_chat}

    def run_conversation(self):
        self.conversation = True

        gpt_response = self.complete_chat("Witaj magiczna kulo")
        print("Magiczna Kula:", gpt_response, "\n")

        while self.conversation:
            prompt = input("Wpisz wiadomosc: ")
            gpt_response = self.complete_chat(prompt)
            print("\nMagiczna Kula:", gpt_response, "\n")

        print("*Kula znika*\n")
        input()

    def complete_chat(self, message: str) -> str:
        response = self.send_message(message)

        if "content" in response.keys():
            return response["content"]

        func_name = response["name"]
        func = self.function_names[func_name]
        func_response = func(response["arguments"]["message"])

        return func_response

    def send_message(self, message: str) -> dict:
        user_message = {
            "role": "user",
            "content": message
        }

        self.messages.append(user_message)

        payload = {
            "model": self.model,
            "messages": self.messages,
            "functions": self.functions
        }

        response = http_methods.http_post(payload)

        self.messages.append(response)

        return response

    def close_chat(self, message: str) -> str:
        self.conversation = False
        return message







