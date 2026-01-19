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
                 racine = object | None,
                 abr_gauche: "ArbreBinaire | None" = None,
                 abr_droit: "ArbreBinaire | None" = None) -> None:
        self.racine = racine
        self.abr_gauche = abr_gauche
        self.abr_droite = abr_droit

    def creer_fils(self, s_abr: str) -> None:
        """
        creer_fils(s_abr: "G" | "D") -> None : Définie un sous abre
        """
        if s_abr.lower() == "d":
            self.abr_droit = ArbreBinaire()
        elif s_abr.lower() == "g":
            self.abr_gauche = ArbreBinaire()
        else:
            raise ValueError("Type d'abre invalide: '{}'. Expected: 'G' | 'D'".format(s_abr))

    def a_valeur(self) -> object | None:
        """
        a_valeur() -> object | None : renvoie la valeur de la racine sinon None
        """
        return self.racine

    def racine_sous_arbre(self, s_abr: str) -> object:
        """
        valeur_sous_arbre(s_abr: "G" | "D") -> object : renvoie la valeur du sous arbre gauche ou droite
        """

        if s_abr.lower() == "d" and self.abr_droit != None:
            return self.abr_droit.racine
        elif s_abr.lower() == "g" and self.abr_gauche != None:
            return self.abr_gauche.racine
        else:
            raise ValueError("Type d'abre invalide: '{}'. Expected: 'G' | 'D'".format(s_abr))

    def est_feuille(self) -> bool:
        """
        est_feuille() -> bool : renvoie True si aucun sous arbre sinon False
        """
        if self.abr_droite == None and self.abr_gauche == None:
            return True
        return False

#################################################
############  Runtime execution  ################
#################################################

abr = ArbreBinaire(racine=12)
#abr.creer_fils("G")
print(f"Est feuille: {abr.est_feuille()}")
print(f"Valeur racine: {abr.a_valeur()}")
