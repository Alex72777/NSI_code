import cesar
import peagePOO
import vehicule
import boyermoore

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



if __name__ == "__main__":
    main()