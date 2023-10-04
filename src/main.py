from api.gpt_client import GPTClient


def main():
    gptClient = GPTClient("gpt-3.5-turbo", "")
    gptClient.run_conversation()


if __name__ == "__main__":
    main()
