import os
import requests

API_KEY = ""
URL = "https://api.openai.com/v1/chat/completions"


def http_post(payload: dict) -> str:
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(URL, json=payload, headers=headers)

        if response.ok:
            response_json = response.json()
            return response_json["choices"][0]["message"]
        else:
            raise Exception("Http POST Exception", response.status_code, response.reason)

    except requests.RequestException as exception:
        print("Request Exception", exception.response)


