from typing import Literal, Callable

class ArbreBinaire():
    """
    Représentation sous forme de classe d'un arbre binaire.
    Attributs:
     racine: object
     abr_gauche: ArbreBinaire | None "Sous arbre gauche"
     abr_droit: ArbreBinaire | None "Sous arbre droit"

    Méthodes:
     creer_fils(s_abr: "G" | "D") -> None : Définie un sous abre
     a_valeur() -> object | None : renvoie la valeur de la racine sinon None
     est_feuille() -> bool : renvoie True si aucun sous arbre sinon False
    """
    def __init__(self,
                 racine: float,
                 methode_representation: Literal['prefixe', 'infixe', 'postfixe'] = 'prefixe',
                 abr_gauche: "ArbreBinaire | None" = None,
                 abr_droit: "ArbreBinaire | None" = None) -> None:
        self.racine = racine
        self.abr_gauche = abr_gauche
        self.abr_droit = abr_droit
        self.parcours = methode_representation
        self._repr_call = self._prefixe
        
        if methode_representation == 'infixe':
            self.repr_call = self._infixe
        elif methode_representation == 'postfixe':
            self.repr_call = self._post_fixe

    def creer_fils(self, s_abr: str, val: "ArbreBinaire") -> None:
        """
        creer_fils(s_abr: "G" | "D") -> None : Définie un sous abre
        """

        if s_abr.lower() == "d":
            self.abr_droit = val
            val.repr_call = self.repr_call
        elif s_abr.lower() == "g":
            self.abr_gauche = val
            val.repr_call = self.repr_call
        else:
            raise ValueError("Type d'abre invalide: '{}'. Expected: 'G' | 'D'".format(s_abr))

    def a_valeur(self) -> float | None:
        """
        a_valeur() -> object | None : renvoie la valeur de la racine sinon None
        """
        return self.racine

    def sous_arbre(self, s_abr: str) -> "ArbreBinaire | None":
        if s_abr.lower() == "d":
            return self.abr_droit
        elif s_abr.lower() == "g":
            return self.abr_gauche
        return None

    def valeur_sous_arbre(self, s_abr: str) -> float | None:
        """
        valeur_sous_arbre(s_abr: "G" | "D") -> float | None : renvoie la valeur du sous arbre gauche ou droite
        """

        if self.est_feuille():
            return None

        if s_abr.lower() == "d" and self.abr_droit:
            return self.abr_droit.racine
        elif s_abr.lower() == "g" and self.abr_gauche:
            return self.abr_gauche.racine
        else:
            raise ValueError("Type d'abre invalide: '{}'. Attendu: 'G' | 'D'".format(s_abr))

    def est_feuille(self) -> bool:
        """
        est_feuille() -> bool : renvoie True si aucun sous arbre sinon False
        """
        if self.abr_droit is None and self.abr_gauche is None:
            return True
        else:
            return False

    def ajouter_feuille(self, new_abr: "ArbreBinaire") -> None:
        abr = self
        val = new_abr.racine
        while abr:
            print(val, abr.racine)
            abr_gauche = abr.abr_gauche
            abr_droit = abr.abr_droit
            if abr_droit and val >= abr.racine:
                print("will look right")
                abr = abr.abr_droit
            elif abr_droit is None and val >= abr.racine:
                print("went right")
                abr.creer_fils('d', new_abr)
                abr = None
            elif abr_gauche is None and val < abr.racine:
                print("went left")
                abr.creer_fils('g', new_abr)
                abr = None
            else:
                print("will look left")
                abr = abr.abr_gauche
    
    def _tri_fusion(self) -> list[float]:
        return []
    
    def _prefixe(self, arbre: "ArbreBinaire") -> list:
        if abr == None:
            return []
        else:
            return [self.racine] + [arbre.sous_arbre('g')] + [arbre.sous_arbre('d')]

    def _infixe(self, arbre: "ArbreBinaire") -> list:
        if abr == None:
            return []
        else:
            return arbre.sous_arbre('g') + [self.racine] + arbre.sous_arbre('d')

    def _post_fixe(self, arbre: "ArbreBinaire") -> list:
        if abr == None:
            return []
        else:
            return arbre.sous_arbre('g') + arbre.sous_arbre('d') + [self.racine]
    
    @property
    def repr_call(self) -> Callable:
        return self._repr_call
    
    @repr_call.setter
    def repr_call(self, val: Literal['prefixe', 'infixe', 'postfixe']) -> None:
        self._repr_call = self._prefixe
        self.parcours = val
        if val == 'infixe':
            self._repr_call = self._infixe
        elif val == 'postfixe':
            self._repr_call = self._post_fixe
        
    def __repr__(self) -> str:
        return str(self.repr_call(self))
        # return f"[{self.racine}, {self.sous_arbre('g')}, {self.sous_arbre('d')}]"

#################################################
############  Runtime execution  ################
#################################################

abr = ArbreBinaire(racine=8)
sag = ArbreBinaire(racine=3)
sad = ArbreBinaire(racine=13)
ssad = ArbreBinaire(racine=14)
sad.creer_fils("d", ssad)
abr.creer_fils("G", sag)
abr.creer_fils("d", sad)

print(f"Parcours: {abr.parcours}")
print(f"Est feuille: {abr.est_feuille()}")
print(f"Valeur racine: {abr.a_valeur()}")
print(abr)

abr.ajouter_feuille(ArbreBinaire(racine=1))
abr.ajouter_feuille(ArbreBinaire(racine=6))
abr.ajouter_feuille(ArbreBinaire(racine=4))
abr.ajouter_feuille(ArbreBinaire(racine=10))
abr.ajouter_feuille(ArbreBinaire(racine=11))
print(abr)
