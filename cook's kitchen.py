from random import randint as rn
import time
import os

cooks = {
    "equiped": None,
    "objective": None,
    "experience": 0
}

items = {
    "vegetables": ["carrote", "tomate", "haricots vert"],
    "fruits": ["pomme", "banane", "kiwi"]
}

cmdHist = []

def printDialogue(dialogue:str):
    textToOutput = ""
    for i in range(len(dialogue)):
        textToOutput += dialogue[i]
        print(textToOutput)
        time.sleep(.1)

def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")

def lavabo():
    pass

def four_plaques():
    pass

def chambre_froide():
    pass

def service():
    pass

def kitchen(items):
    commands = {"Lavabo": lavabo, "Four & Plaques": four_plaques, "Chambre froide": chambre_froide, "Service": service}
    print("-=-=-=-=-=--=-=- Cuisine -=-=-=-=-=--=-=-\n")

def menu():
    SLEEP_TIME = 1
    print("Vous êtes chef cuisinier étoilé, aujourd'hui est votre premier jour dans un nouveau restaurant connu dans Paris.")
    time.sleep(SLEEP_TIME)
    print("Vous angoissez un peu quant aux attentes qui vous sont demandés mais vous vous êtes préparés toute votre vie.")
    time.sleep(SLEEP_TIME)
    print("Votre rêve va enfin se réaliser, êtes vous prêt à l'accomplir?")
    print("1: Oui\n2: Non")
    usrInput = input("")
    
    if usrInput == "1":
        pass
    else:
        print("Dommage ! :(")