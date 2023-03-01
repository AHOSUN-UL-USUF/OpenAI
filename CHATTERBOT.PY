##{PYTHON CHATBOT USING OPENAI}##
from colorama import (Fore)
print(Fore.GREEN + "Acces by all of your devices using this link :")
print(Fore.CYAN + "[ https://replit.com/@AHOSUNULYOUSUF/OpenAI ]")
print(Fore.LIGHTGREEN_EX +"See the source code at:")
print(Fore.LIGHTCYAN_EX + "[ https://github.com/AHOSUN-UL-USUF/OpenAI/blob/main/CHATTERBOT.PY ]")
newlist = []
for i in range(1000):
    from sys import (stdout)
    from time import (sleep)
    from openai import (Completion)
    import openai

    def write(text, speed=0.02):
        for char in text:
            stdout.write(char)
            stdout.flush()
            sleep(speed)
# Set up the OpenAI API client 
    openai.api_key = "Your API_KEY here"


    model_engine = "text-davinci-003"
    prompt = input(Fore.RED + f"[ Please enter your prompt. ] {Fore.BLUE}")
# Generate a response
    completion = Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text #type:ignore
    print("          ")
    write(Fore.RED + "[ OpenAI ]")
    write(f"{Fore.BLUE}{response}\n")
    print("          ")

    if prompt == "->":
        exit()
