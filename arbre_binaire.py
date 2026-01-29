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
                 abr_gauche: "ArbreBinaire | None" = None,
                 abr_droit: "ArbreBinaire | None" = None) -> None:
        self.racine = racine
        self.abr_gauche = abr_gauche
        self.abr_droite = abr_droit

    def creer_fils(self, s_abr: str, val: float = None) -> None:
        """
        creer_fils(s_abr: "G" | "D") -> None : Définie un sous abre
        """
        if s_abr.lower() == "d":
            self.abr_droit = ArbreBinaire(val)
        elif s_abr.lower() == "g":
            self.abr_gauche = ArbreBinaire(val)
        else:
            raise ValueError("Type d'abre invalide: '{}'. Expected: 'G' | 'D'".format(s_abr))

    def a_valeur(self) -> float | None:
        """
        a_valeur() -> object | None : renvoie la valeur de la racine sinon None
        """
        return self.racine
    
    def sous_arbre(self, s_abr: str) -> "ArbreBinaire | None":
        if self.est_feuille():
            return None
        
        if s_abr.lower() == "d":
            return self.abr_droit
        elif s_abr.lower() == "g":
            return self.abr_gauche
    
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
            raise ValueError("Type d'abre invalide: '{}'. Expected: 'G' | 'D'".format(s_abr))

    def est_feuille(self) -> bool:
        """
        est_feuille() -> bool : renvoie True si aucun sous arbre sinon False
        """
        if self.abr_droite == None and self.abr_gauche == None:
            return True
        else:
            return False
    
    def ajouter_feuille(self, val: float) -> None:
        attente = [self.racine]
    
    def _prefixe(self, arbre: "ArbreBinaire") -> list:
        if abr == None:
            return []
        else:
            return self._infixe(arbre.valeur_sous_arbre('g')) + [arbre.racine] + infixe(arbre.valeur_sous_arbre('d'))
    
    def _infixe(self) -> list:
        pass
    
    def _post_fixe(self) -> list:
        pass
    
    def __repr__(self) -> str:
        #return str(self._prefixe())
        return f"[{self.racine}, {self.sous_arbre('g')}, {self.sous_arbre('d')}]"
        

#################################################
############  Runtime execution  ################
#################################################

abr = ArbreBinaire(racine=12)
abr.creer_fils("G", 5)
abr.creer_fils("d", 1)
print(f"Est feuille: {abr.est_feuille()}")
print(f"Valeur racine: {abr.a_valeur()}")
print(abr)
