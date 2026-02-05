

def fusion(gauche: list, droite: list) -> list:
    pass

def tri_fusion(liste: list[float]) -> list[float]:
    """
    Docstring
    """
    
    if len(liste) <= 1:
        return liste
    
    a = []
    length = len(a)
    milieu = length//2
    a.append(liste[:milieu])
    a.append(liste[milieu+1:])
    print(a)


tri_fusion([1,4,2,5,3])
