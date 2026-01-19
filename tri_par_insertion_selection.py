def tri_par_insertion(liste: list) -> list:
    for i in range(1, len(liste)): 
        k = i - 1
        cle = liste[i]
        while liste[k] > cle and k >= 0:
            liste[k + 1] = liste[k]
            k -= 1
        liste[k + 1] = cle
               
    return liste

def tri_par_selection(liste: list) -> list:
    for k in range(len(liste)-1):
        min_i = k
        for i in range(k + 1, len(liste)):
           if liste[i] < liste[min_i]:
                min_i = i
        liste[k], liste[min_i] = liste[min_i], liste[k]

    return liste

liste = [5, 9, 2, 4, 7]
print(tri_par_insertion(liste))
print(tri_par_selection(liste))
