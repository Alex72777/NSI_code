

def regner(gauche: list, droite: list) -> list:
    final = []
    while len(gauche) > 0 or len(droite) > 0:
        if len(gauche) == 0:
            final.append(droite.pop(0))
        elif len(droite) == 0:
            final.append(gauche.pop(0))
        elif gauche[0] < droite[0]:
            final.append(gauche.pop(0))
        else:
            final.append(droite.pop(0))
#     print(final)
    return final
    

def diviser_regner(liste: list[float]) -> list[float]:
    """
    Docstring
    """
    
    if len(liste) <= 1:
        return liste
    
    milieu = len(liste)//2
    l_gauche = liste[:milieu]
    l_droite = liste[milieu:]
    #print(l_gauche, l_droite)
    gauche = diviser_regner(l_gauche)
    droite = diviser_regner(l_droite)
    
    return regner(gauche, droite)
    

print(diviser_regner([]))
print(diviser_regner([0, 45, 17, 999, 36]))
# assert diviser_regner(([0, 45, 17, 999, 36]) = [0,36,45,999]
