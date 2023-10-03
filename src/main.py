from api.gpt_client import GPTClient


def main():
    gptClient = GPTClient("gpt-3.5-turbo", "Wcielasz sie w role magicznej kuli ktora mowi w magiczny sposob, twoja rozmowczynia jest Monika, witasz sie z nia jako swoja pania")
    gpt_response = gptClient.complete_chat("Witaj magiczna kulo")
    print("Magiczna Kula:", gpt_response)
    prompt = input("Wpisz wiadomosc: ")
    while prompt != "exit":
        gpt_response = gptClient.complete_chat(prompt)
        print("Magiczna Kula:", gpt_response)
        prompt = input("Wpisz wiadomosc: ")


if __name__ == "__main__":
    main()
