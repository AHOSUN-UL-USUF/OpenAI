##{PYTHON CHATBOT USING OPENAI}##
from colorama import (Fore)
from os import (system)
from sys import (stdout)
from time import (sleep)
from openai import (Completion) 
import openai

def write(text, speed=0.06):
    for char in text:
        stdout.write(char)
        stdout.flush()
        sleep(speed)
system('cls')
write(f"{Fore.CYAN}┌{Fore.LIGHTGREEN_EX}Acces by all of your devices using the link below: \n{Fore.CYAN}└⟶ {Fore.LIGHTCYAN_EX}[ https://replit.com/@AHOSUNULYOUSUF/OpenAI ]\n")

newlist = []
for i in range(1000):

# Set up the OpenAI API client
    openai.api_key = "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"


    model_engine = "text-davinci-003"
    write(Fore.GREEN + f"┌{Fore.RED}[ Please enter your prompt. ]\n")
    write(Fore.GREEN + f"│\n")
    prompt = input(Fore.GREEN + f"└⟶  {Fore.BLUE}")
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
    write(f"{Fore.RED} [ OpenAI ]\n")
    write(f" {Fore.BLUE} {response}")
    print("          ")

    if prompt == "->":
        exit()
