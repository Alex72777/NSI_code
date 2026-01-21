from typing import Literal
from dataclasses import dataclass

@dataclass
class Eleve:
    """
    Représente un élève avec son nom, prénom, notes, spécialités et dossier disciplinaire.
    """
    nom: str
    prenom: str
    notes: list[float]
    spes: list[Literal['Mathématiques', 'Physique-Chimie', 'NSI', 'SVT', 'HGGSP', 'HLP', 'LLCE Anglais', 'LLCE Espagnol', 'SES']]
    dossier_discipline: dict[str, str]
    
    def nouv_note(self, matiere: str, note: float) -> None:
        """Ajoute une nouvelle note à l'élève."""
        self.notes.append(note)
        self.spes.append(matiere)
    
    def remplir_appreciation(self, matiere: str, appreciation: str) -> None:
        """Remplie une appréciation."""
        self.dossier_discipline[matiere] = appreciation
    
    @property
    def moyenne(self) -> float:
        """Renvoie la moyenne de l'élève des notes de toutes ses matières."""
        if self.notes:
            return round(sum(self.notes) / len(self.notes), 2)
        raise ValueError("Aucune note")
    
    def __repr__(self) -> str:
        return f"Nom: {self.nom}\nPrénom: {self.prenom}\nNotes: {self.notes}\nSpés: {self.spes}\nMoyenne: {self.moyenne}\nDossier discipline: {self.dossier_discipline}"

@dataclass
class Character:
    nom: str
    prenom: str
    sante: float = 100
    faim: float = 100
    soif: float = 100
    hygiene: float = 100
    humeur: float = 100
    energie: float = 100
    argent: int = 20
    
    def manger(self) -> None:
        self.faim = max(100, self.faim + 25)
    
    def boire(self) -> None:
        self.soif = max(100, self.soif + 25)
    
    def prendre_une_douche(self) -> None:
        self.hygiene = 100
    
    def aller_au_toilette(self) -> None:
        self.hygiene = max(100, self.hygiene + 50)
    
    def dormir(self) -> None:
        self.energie = 100
    
    def jouer(self, temps: float) -> None:
        """"""
        self.humeur
def main():
    eleve1 = Eleve(
        nom="Dupont",
        prenom="Jean",
        notes=[15.5, 13.0],
        spes=["Mathématiques", "NSI"],
        dossier_discipline={"Mathématiques": "Très bien"}
    )
    
    # 1: Initialisation de l'instance de la classe Eleve
    # 2: Appel de la fonction nouvelle_note sur l'instance d'Eleve
    # 3: Ajout de la note à la liste de notes propre à l'instance d'Eleve

    print(eleve1)
    # print(Eleve.moyenne(eleve1))

if __name__ == "__main__":
    main()