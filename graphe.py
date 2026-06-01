from typing import Any

gr = {
    "A": ["B", "C"],
    "B": ["A", "F"],
    "C": ["A", "D", "G"],
    "D": ["C"],
    "E": ["C", "F", "G"],
    "F": ["B", "E"],
    "G": ["C", "E"]
}

def lecture_graphe_largeur(gr: dict[Any, list[Any]], depart: Any) -> list[Any]:
    """
    Lecture d'un graphe non orienté consideré connexe via parcours en largeur. Renvoie la lecture sous liste.
    """
    att = gr[depart]
    lect = [depart]
    
    while len(att) > 0:
        print(att, lect)
        for k in att:
            if not k in lect:
                lect.append(k)
        
        att_len = len(att)
        for k in att:
            for v in gr[k]:
                if not v in lect and not v in att:
                    att.append(v)
        att = att[att_len:]
    print(att, lect)
    return lect

print("->".join(lecture_graphe_largeur(gr, "A")))
print("->".join(lecture_graphe_largeur(gr, "E")))
print("->".join(lecture_graphe_largeur(gr, "F")))

def lecture_graphe_longueur(gr: dict[Any, list[Any]], depart: Any) -> list[Any]:
    """
    Lecture d'un graphe non orienté consideré connexe via parcous en longueur. Renvoie la lecture sous liste.
    """
    att = gr[depart]
    lect = [depart]
    
    while len(att) > 0:
        print(att, lect)
        for k in att:
            if not k in lect:
                lect.append(k)
        
        att_len = len(att)
        for k in att:
            for v in gr[k]:
                if not v in lect and not v in att:
                    att.append(v)
        att = att[att_len:]
    print(att, lect)
    return lect
