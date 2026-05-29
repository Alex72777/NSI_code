import cesar
import peagePOO
import tableaux5x5
import boyermoore
from random import randint, choice

def main() -> None:
        alpha = "abcdefghijklmnopqrstuvwxyz 123456789"
        message = "bonjour monsieur"
        print("message original:", message)
        # on veut transmettre le message a mr germant, on applique cesar
        message_cesar  = cesar.cesar(3, message, alpha)
        print("message crypté cesar:", message_cesar)

        # si chacun des deux partis connaissent la clé et personne d'autre, une attaque man in the middle n'est pas possible.

        message_fin = cesar.cesar(-3, message_cesar, alpha)
        print("message recu par mr germant:", message_fin)

        print("analyse frequentielle message cesar: -------------------")

        cesar.analyse_frequentielle(message_cesar, alpha)

        print("tentative brute force du message transmis: -------------")
        cesar.brute_force(message_cesar, alpha)

        print("fin brute force-----------------------------------------")

        print("Recherche boyer moore...")
        print("Analyse de '{}' pour 'bonjour'".format(message))

        index = boyermoore.rechBoyerMoore(message, "bonjour")
        if index != None:
                print(message[index-100:index] + f">bonjour<" + message[index + len("bonjour"): index + 100])
        
        print("Vehicules ----------------------------------------------")

        liste_vehc = []
        liste_vehc.append(peagePOO.Vehicule('voiture'))
        liste_vehc.append(peagePOO.Vehicule('camion'))
        liste_vehc.append(peagePOO.Vehicule('moto'))
        liste_vehc.append(peagePOO.Vehicule('velo'))
        liste_vehc.append(peagePOO.Vehicule('avion'))
        [print(vehc) for vehc in liste_vehc]

        peage = peagePOO.Peage()
        [peage.enfiler(peagePOO.Vehicule(choice(liste_vehc))) for i in range(10)]
        [peage.defiler() for i in range(3)]

        print(peage)

        peage.vider()

        print(peage)
        print("File d'attente vide:", peage.est_vide)

        print("Sims ---------------------------------------------------")

        tableaux5x5.main()


if __name__ == "__main__":
    main()