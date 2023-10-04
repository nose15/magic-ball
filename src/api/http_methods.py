import os
import requests
import json

API_KEY = ""
URL = "https://api.openai.com/v1/chat/completions"


def http_post(payload: dict) -> dict:
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(URL, json=payload, headers=headers)

        if response.ok:
            response_json = response.json()

            if "function_call" in response_json["choices"][0]["message"].keys():
                function_args = response_json["choices"][0]["message"]["function_call"]["arguments"]
                response_json["choices"][0]["message"]["function_call"]["arguments"] = json.loads(function_args)
                return response_json["choices"][0]["message"]["function_call"]

            return response_json["choices"][0]["message"]
        else:
            raise Exception("Http POST Exception", response.status_code, response.reason)

    except requests.RequestException as exception:
        print("Request Exception", exception.response)


