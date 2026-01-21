from dataclasses import dataclass
from random import randint, choice

@dataclass
class Dresseur:
    nom: str
    pokemons: list["Pokemon"]

@dataclass
class Pokemon:
    nom: str
    le_type: str
    max_PV: int
    PV: int
    att: int
    deff: int
    exp: int
    competences: list[str]
    
    def aller_au_pokecentre(self) -> None:
        print(f"{self.nom} est allé au pokecentre")
        self.PV = self.max_PV
    
    @staticmethod
    def combat(attaquant: "Pokemon", adversaire: "Pokemon") -> None:
        print(f"Nouveau combat !\n{attaquant.nom} affronte {adversaire.nom}.")
        print(attaquant)
        print(adversaire)
        
        tour = 1
        print("Premier tour !")
        while attaquant.PV > 0 and adversaire.PV > 0:
            if tour > 1: print(f"Tour {tour}!")
            tour += 1
            print(f"\n{attaquant.nom} utilise sa compétence {choice(attaquant.competences)}.")
            
            print(f"{adversaire.nom} riposte avec {choice(adversaire.competences)}")
            
            nb_attaquant = randint(1, 100)
            nb_adv = randint(1, 100)
            if nb_attaquant > 50:
                degats = int(attaquant.att * ((100 - adversaire.deff) / 100))
                adversaire.PV = max(0, adversaire.PV - degats)
                print(f"\n{attaquant.nom} a réussi son attaque sur {adversaire.nom} !")
                print(f"{adversaire.nom}: {adversaire.PV + degats} -> {adversaire.PV} PV")
            else:
                print(f"\n{attaquant.nom} rate son attaque sur {adversaire.nom} !")
                print(f"{adversaire.nom}: {adversaire.PV} -> {adversaire.PV} PV")
            
            if nb_adv > 50:
                degats = int(adversaire.att * ((100 - attaquant.deff) / 100))
                attaquant.PV = max(0, attaquant.PV - degats)
                print(f"\n{adversaire.nom} a réussi son attaque sur {attaquant.nom} !")
                print(f"{attaquant.nom}: {attaquant.PV + degats} -> {attaquant.PV} PV")
            else:
                print(f"\n{adversaire.nom} rate son attaque sur {attaquant.nom} !")
                print(f"{attaquant.nom}: {attaquant.PV} -> {attaquant.PV} PV")
        
        if attaquant.PV > 0 and adversaire.PV == 0:
            print(f"{attaquant.nom} remporte la victoire sur {adversaire.nom}!")
        elif adversaire.PV > 0 and attaquant.PV == 0:
            print(f"{adversaire.nom} remporte la victoire sur {attaquant.nom}!")
        else:
            print(f"Egalité entre {attaquant.nom} et {adversaire.nom}, aucun vainceur.")

type_poke = [
    "Feu",
    "Eau",
    "Plante",
    "Électrik",
    "Vol",
    "Sol",
    "Roche",
    "Psy",
    "Spectre",
    "Combat",
    "Poison",
    "Glace",
    "Dragon",
    "Acier",
    "Ténèbres",
    "Fée",
    "Insecte",
    "Normal"
]

competences_poke = [
    "Flammeche",
    "Pistolet à O",
    "Vampigraine",
    "Tonnerre",
    "Vol",
    "Tunnel",
    "Jet-Pierres",
    "Choc Mental",
    "Ball’Ombre",
    "Uppercut",
    "Dard-Venin",
    "Laser Glace",
    "Draco-Rage",
    "Griffe Acier",
    "Tricherie",
    "Éclat Magique",
    "Plaie-Croix",
    "Charge"
]

noms_poke = [
    "Bulbizarre",
    "Salamèche",
    "Carapuce",
    "Pikachu",
    "Roucool",
    "Rattata",
    "Nosferapti",
    "Mystherbe",
    "Miaouss",
    "Psykokwak",
    "Machoc",
    "Gravalanch",
    "Fantominus",
    "Onix",
    "Magicarpe",
    "Dracaufeu",
    "Lokhlass",
    "Ronflex",
    "Mewtwo",
    "Evoli"
]

def main():
    pokes = []
    
    for i in range(10):
        poke_PV = randint(60, 90)
        max_att = min(50, 150 - poke_PV - 10)
        poke_att = randint(35, max_att)
        poke_def = 150 - poke_PV - poke_att
        
        poke = Pokemon(
            nom=f"{choice(noms_poke)}{i}",
            le_type=choice(type_poke),
            max_PV=poke_PV,
            PV=poke_PV,
            att=poke_att,
            deff=poke_def,
            competences=[choice(competences_poke), choice(competences_poke)]
        )
        pokes.append(poke)
    
    Pokemon.combat(choice(pokes), choice(pokes))

if __name__ == "__main__":
    main()