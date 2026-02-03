from dataclasses import dataclass, field
from random import shuffle

"""

# Exo 1

Vous avez une liste de véhicules en attente au péage (file)
peage = ["C4", "DS3", "P7" , "R4"]
Donner le résultat après avoir effectuer les opérations suivantes ;
 - les 2 premiers sont passés : ["P7", "R4"]
 - arrivée dans la file (R19) : ["P7", "R4", "R19"]
 - arrivée dans la fire (2CV) : ["P7", "R4", "R19", "2CV"]
 - le premier est passé :       ["R4", "R19", "2CV"]

# Exo 2

Une pile des fonctions du système est représentée ainsi :
["Allumage", "Ouvrir_OS", "Ouvrir_GIMP", "Tracer_Droite", "Remplir_Couleur"]
 - Expliquer ce qu'a fait l'utilisateur sur son ordinateur et dans quel ordre
 > Appuyer sur le bouton d'alimentation, l'ordinateur démarre l'OS, il ouvrir le logiciel GIMP, trace une droite et met de la couleur
 - L'utilisateur souhaite ouvrir VLC et non GIMP, quelles conséquences sur la pile ?
 > ["Allumage", "Ouvrir_OS", "Ouvrir_VLC"]

# Exo 3

Donner les commandes pour une liste permettant de faire les opérations qui simuleraient selon les fonctions:
 - le comportement d'une pile : pile.pop() et pile.append()
 - le comportement d'une file : file.pop(0) et file.append()

Coder une fonction pilerfiler(liste, comportement) qui traite selon le comportement choisis l'opération demandée à l'utilisateur puis renvoie la liste
Coder une fonction piler(liste=[]) / filer(liste=[]) qui traite le choix de l'opération demandée à l'utilisateur, puis renvoie la liste
"""

def piler(liste, comportement: int) -> list:
    if not liste: return liste
    if comportement == 1:
        return liste.append("a")
    liste.pop()
    return liste

def filer(liste, comportement: int) -> list:
    if not liste: return liste
    if comportement == 3:
        return liste.append("a")
    liste.pop(0)
    return liste

def pilerfiler(liste: list, comportement: int) -> list:
    if comportement in [1, 2]:
        piler(liste, comportement)
    elif comportement in [3, 4]:
        filer(liste, comportement)
    return liste


"""
Exo 3 b)

Coder la class pile avec :
 - empiler(self) qui retourne la liste
 - depiler(self) qui retourne l'objet retiré
 - est_vide(self) -> True si vide sinon False

Coder la class file avec :
 - enfiler(self) qui retourne la liste
 - defiler(self) qui retourne l'objet retiré
 - est_vide(self) -> True si vide sinon False
"""

@dataclass
class Pile:
    liste: list = field(default_factory=lambda: [])

    def empiler(self, element: object) -> list:
        self.liste.append(element)
        return self.liste

    def depiler(self) -> object:
        if not self.est_vide():
            return None
        element = self.liste.pop()
        return element

    def est_vide(self) -> bool:
        return True if self.liste else False

    def inserer(self, element: object, index: int):
        self.liste = self.liste[:index] + [element] + self.liste[index:]

@dataclass
class File:
    liste: list = field(default_factory=lambda: [])

    def enfiler(self, element: object) -> list:
        self.liste.append(element)
        return self.liste

    def defiler(self) -> object:
        if not self.est_vide():
            return None
        element = self.liste.pop(0)
        return element

    def est_vide(self) -> bool:
        return True if self.liste else False

    def inserer(self, element: object, index: int):
        self.liste = self.liste[:index] + [element] + self.liste[index:]

def _auto_solving():
	L1 = list(range(1, 9))

	pile = Pile(L1)
	pile_tampon = Pile()
	file = File()

	while file.liste != L1:
		if pile.liste and pile_tampon.liste and file.liste:
			if file.liste[-1] - 1 == pile_tampon.liste[0]:
				element = pile.depiler()
				file.enfiler(element)
			else:
				element = pile.depiler()
				pile_tampon.empiler(element)
		elif pile_tampon.liste and file.liste:
			if file.liste[-1] - 1 != pile_tampon.liste[0]:
				pass

def _manual_solving():
	L1 = list(range(8, 0, -1))
	# ~ shuffle(L1)
	print(L1)

	pile = Pile([] + L1)
	pile_tampon = Pile()
	file = File()

	while file.liste != L1:
		print(f"\n{'*' * 20}\nPile: {pile.liste}\nPile tampon: {pile_tampon.liste}\nFile: {file.liste}")
		action = input("(1) Empiler (2) Dépiler")
		if action.isdigit(): action = int(action)
		else: action = 0

		if action == 1 and not pile.est_vide():
			element = pile.depiler()
			pile_tampon.empiler(element)

		if action == 2 and not pile_tampon.est_vide():
			element = pile_tampon.depiler()
			file.enfiler(element)
	print(file.liste)
	print("gg")

"""
Exo 5
Modéliser l'EDT des suspects selon le principe d'une pile en listant les élements prioritaires
"""

def _edt_suspects():
	EDT = {"6:00": "Lever", "6:05": "Ptit déjeuner", "6:30": "Transport", "8:00": "DM"}
	edt_liste = list(EDT.values())
	edt_liste.reverse()
	edt_eleve_pile = Pile(edt_liste)
	print("EDT sous forme de pile:", edt_eleve_pile.liste)

"""
Exo 6
A partir de la liste suivante: ["Au bureau du Boss", "***", "****", "****", "****"], identifier les indices pour construire le mot clé #####
"""

def main():
	# ~ comportement = input("1: Empiler 2: Dépiler 3: Enfiler, 4: Défiler : ")
	# ~ if not comportement.isdigit(): return

	# ~ _manual_solving()
	_edt_suspects()

if __name__ == "__main__":
	main()
