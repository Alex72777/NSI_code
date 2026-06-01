from tkinter import *
from sims import personnages

def main() -> None:
    fenetre = Tk()
    fenetre.title("Tableau 5x5")
    perso=personnages("Alex")

    B=[]
    for i in range(5):
        B.append([])
        for j in range(5):
            
            valeur = str(i)+' : '+str(j)#(i+1)*10 + (j+1) #str(i)+' : '+str(j) # ex: 11, 12, 13...
            bouton = Button(fenetre, text=valeur, width=5, height=2)
            bouton.grid(row=i, column=j, padx=2, pady=2)
            B[i].append(bouton)
        #print(B)

    B[1][1]["text"]='manger'
    B[1][1]['command']= perso.manger

    B[1][2]["text"]='dormir'
    B[1][2]['command']= perso.dormir

    B[1][3]["text"]='travaille'
    B[1][3]['command']= perso.travaille

    fenetre.mainloop()