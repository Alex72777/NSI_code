from random import randint

def BatNav(largeurMap: int):
    Xennemy = randint(1, largeurMap)
    Yennemy = randint(1, largeurMap)
    #print(Xennemy, Yennemy)
    
    Xplayer = 0
    Yplayer =  0
    
    limite = True if input("Tours limités (O/n)") in ["O", "o"] else False
    toursLimite = int(input("Tours?")) if limite else 0
    tours = 0
    print(f"Tours limités à {toursLimite}." if limite else "Tours illimités.")
    
    while (Xennemy != Xplayer or Yennemy != Yplayer) and (limite and tours < toursLimite):
        tours += 1
        
        print(f"\nTour {tours}:")
        if Xplayer and Yplayer:
            print("Position actuelle : x={} y={}".format(Xplayer, Yplayer))
        
        if Xplayer == Xennemy:
            print("Vous êtes sur la même ligne.")
        elif Yplayer == Yennemy:
            print("Vous êtes dans la même colonne.")
        
        while True: # X coordinate
            try:
                Xplayer = int(input("Coordonnée en x?"))
                if  Xplayer < 1 or Xplayer > largeurMap:
                    print("Entrez un charactère valide (chiffre allant de 1 à {})".format(largeurMap))
                    continue
                break
            except:
                print("Entrez un charactère valide (chiffre allant de 1 à {})".format(largeurMap))
                
        while True: # Y coordinate
            try:
                Yplayer = int(input("Coordonnée en y?"))
                if Yplayer < 1 or Yplayer > largeurMap:
                    print("Entrez un charactère valide (chiffre allant de 1 à {})".format(largeurMap))
                    continue
                break
            except:
                print("Entrez un charactère valide (chiffre allant de 1 à {})".format(largeurMap))
    
    if Xennemy == Xplayer and Yennemy == Yplayer:
        print(f"\nFélicitations, vous avez coulé le bateau adverse. ({tours} tours)")
        print("Coordonnées adversaire x={} y={}".format(Xennemy, Yennemy))
    elif tours == toursLimite and limite:
        print("\nVous n'avez pas réussi à couler l'adversaire dans la limite de tours imparti.")
        print("Vos coordonnées x={} y={}".format(Xplayer, Yplayer))
        print("Coordonnées adversaire x={} y={}".format(Xennemy, Yennemy))

BatNav(5)