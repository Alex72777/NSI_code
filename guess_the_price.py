# Modules
import time
import os
from random import randint

# Variables

maxPrice = 100

doMaxAttempts = True
maxAttempts = 10

initTime =  time.time()
totalAttempts = 0
wins = 0
defeats = 0

# Functions

### Misc functions
def clearScreen() -> None:
    os.system("cls" if os.name == "nt" else "clear")

def printSessionStats() -> None:
    clearScreen()
    print("// Statistiques Session //")
    print(f"Total Playtime : {round(time.time()-initTime)} secondes")
    print(f"Victoires : {wins}")
    print(f"Défaites : {defeats}\n")

    input("Appuyez sur n'importe quelle touche pour retourner au jeu.")

def settings():
    clearScreen()
    print("/// Paramètres du jeu ///\n")
    print(f"Essais maximum en mode limité : {maxAttempts}\n")

    input("Appuyez sur n'importe quelle touche pour retourner au jeu.")

### Menu functions

def displayMenu() -> None:
    clearScreen()
    print("/// Guess the price ///\n")
    print("1: Infinite Attempts")
    print("2: Limited Attempts")
    print("3: Session History")
    print("4: Settings")
    print("5: Quit\n")

### Game functions

def printHistory(history:list, guessedPrice:int, price:int) -> str:
    line1 = ""
    for i in history:
        line1 += f"{i}>; " if i > price else f"{i}<; " 
        line2 = "\nDernier trop grand" if guessedPrice > price else "\nDernier trop petit"

    return line1+line2

def printStats(runTime:float, attempts:int) -> None:
    print("// Récapitulatif //")
    print(f"Temps joué : {round(time.time()-runTime)} secondes")
    print(f"Nombre total d'essais : {attempts}")

def win(time:float, attempts:int, wins) -> None:
    clearScreen()
    print("GG ! Vous avez gagné!\n")
    printStats(time, attempts)
    wins += 1
    input("Appuyez sur n'importe quelle touche pour retourner au jeu")

def defeat(time:float, attempts, defeats, price:int) -> None:
    clearScreen()
    print(f"Dommage! Vous avez perdu.\nRéponse : {price}\n")
    printStats(time, attempts)
    defeats += 1
    input("\nAppuyez sur n'importe quelle touche pour retourner au jeu")

def start(limitedAttempts:bool, wins, defeats, totalAttempts):
    price = randint(0, maxPrice)
    clearScreen()
    startTime = time.time()
    history = []
    success = False
    for i in range(0, maxAttempts if limitedAttempts else 9999):
        totalAttempts += 1
        if limitedAttempts:
            print(f"{maxAttempts-i} tentatives restantes")
        
        guessedPrice = int(input("Quel est votre prix ?\n"))
        history.append(guessedPrice)

        if guessedPrice == price:
            success = True
            win(startTime, totalAttempts, wins)
            break

        clearScreen()
        print(printHistory(history, guessedPrice, price))
    
    if not success:
        defeat(startTime, totalAttempts, defeats, price)

# Algorithm

## Commands List

commands = {
    "1": None,
    "2": None,
    "3": printSessionStats,
    "4": settings
}


clearScreen()

# Game Loop
while True:
    # Display Menu
    displayMenu()
    command = input("Entrer l'identifiant de la commande.\n")

    if command == "5":
        break
    
    if command in commands:
        if command == "1":
            start(False, wins, defeats, totalAttempts)
        elif command == "2":
            start(True, wins, defeats, totalAttempts)
        else:
            commands[command]()
    else:
        print("Identifiant invalide...")
        time.sleep(1)

clearScreen()