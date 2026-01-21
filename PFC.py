from random import randrange
import json

def _save(victoire: bool) -> None:   
    save_data = None
    with open("save.txt", "w", encoding="utf8") as save_file:
        #save_data = json.loads(save.read())
        save_data = max(0, 1 if victoire else -1)
        save_file.write(f"Victoires: {save_data}")
        save_file.close()

def _PFC(choix: int) -> int:
    combos_gagnant: dict[int, int] = {
        1: 3,
        2: 1,
        3: 2
    }
    
    if choix not in list(choix_possibles.keys()):
        choix = randrange(1, 3)
    
    choix_adverse = randrange(1, 3)
    
    print(f"\nPlayer joue {choix_possibles[choix]}.")
    print(f"IA joue {choix_possibles[choix_adverse]}.")
    
    if combos_gagnant[choix] == choix_adverse:
        print(f"{choix_possibles[choix]} bat {choix_possibles[choix_adverse]}, Player remporte ce round.")
        return 1
    if combos_gagnant[choix_adverse] == choix:
        print(f"{choix_possibles[choix_adverse]} bat {choix_possibles[choix]}, IA remporte ce round.")
        return -1
    if choix == choix_adverse:
        print("\nEgalité, pas de gagnant.")
    return 0

choix_possibles: dict[int, str] = {
    1: "Pierre",
    2: "Feuille",
    3: "Ciseaux",
}

def main():
    victoire: bool = False
    
    score: int = 0
    for i in range(3):
        print()
        for i, v in choix_possibles.items():
            print(f"> {i}: {v}")
        choix: str = input("\nChoix: ")
        """if not choix.isdigits():
            choix = -1"""
        try:
            choix = int(choix)
        except:
            choix = -1
        
        score += _PFC(choix)
        print("\n----------------------\n")
    
    if score > 0: victoire = True
    
    if victoire:
        print("Player remporte la partie!")
        _save(True)
    else:
        print("Player a perdu la partie...")
        _save(False)

if __name__ == "__main__":
    main()