from random import randint
sport=["Basket","foot", "atclétisme", "aviron", "rudby", "boxe"]
choix_plat=["pate carbonara","oeuf au plat", "oeuf à la coque", "oeuf brouille","oeuf pocher"]
choix_ou_dormir=["hotel_1*","hotel_2*","hotel_3*","hotel_4*", "hotel_5*", "PALACE_!!!"]
emploi=["pompier","policier","professeur","architecte","apiculteur","agriculteur"]
class personnages(object):
    def __init__(self, nom):
        self.nom=nom
        self.Energie=100
        self.faim=100
        self.Hygiene=100
        self.Loisir=10
        self.relation=10
        self.sport=100
        self.Argent=250

    def manger(self):
        self.faim =min(100, self.faim +50)
        self.Argent =max(0, self.Argent -10)
        
        choix_1=choix_plat[randint(0,len(choix_plat)-1)]
        
        if choix_plat[0]==choix_1:
            self.faim=min(100,self.faim+50) 
            self.Argent=max(0,self.Argent-13)
            
        elif choix_plat[1]==choix_1:
            self.faim=min(100,self.faim+45) 
            self.Argent=max(0,self.Argent-12)
            
        elif choix_plat[2]==choix_1:
            self.faim=min(100,self.faim+50) 
            self.Argent=max(0,self.Argent-10)
            
        elif choix_plat[3]==choix_1:
            self.faim=min(100,self.faim+60) 
            self.Argent=max(0,self.Argent-16)
       
        elif choix_plat[4]==choix_1:
            self.faim=min(100,self.faim+100) 
            self.Argent=max(0,self.Argent-60)
            
        print(f"{choix_plat} vous ête sur le point de manger {choix_1} vous avez obtenue {self.faim}faim, mais vous avez perdu {self.Argent}d'Argent")    
            
            
    def soif(self):
        self.faim =min(100, self.faim +20)
        
    def dormir(self):
        self.Energie =min(100,self.Energie+80)
        self.Hygiene =min(100, self.Hygiene-20)
        
        choix=choix_ou_dormir[randint(0,len(choix_ou_dormir)-1)]
        
        if choix_ou_dormir[0]==choix:
            self.Energie=min(100,self.Energie+10)
        elif choix_ou_dormir[1]==choix:
            self.Energie=min(100,self.Energie+20)
        elif choix_ou_dormir[2]==choix:
            self.Energie=min(100,self.Energie+40)
        elif choix_ou_dormir[3]==choix:
            self.Energie=min(100,self.Energie+50)
        elif choix_ou_dormir[4]==choix:
            self.Energie=min(100,self.Energie+70)
            
        elif choix_ou_dormir[5]==choix:
            self.Energie=min(100,self.Energie+100)
        
        print(f" Bonjour vous aller dormirais ce soir a {choix} passer une bonne nuit !!")
        
        
    def aller_au_WC(self):
        self.Hygiene=min(100, self.Hygiene+25)
        
    def travaille(self):
        self.Hygiene=min(100,self.Hygiene-50)
        self.Argent=max(0,self.Argent+750)
        
        choix_2=emploi[randint(0,len(emploi)-1)]
        if emploi[0]==choix_2:
            self.Hygiene=min(100,self.Hygiene-70)
            self.Argent=max(0, self.Argent+220)
        
        elif emploi[1]==choix_2:
            self.Hygiene=min(100,self.Hygiene-60)
            self.Argent=max(0, self.Argent+320)
        
        elif emploi[2]==choix_2:
            self.Hygiene=min(100,self.Hygiene-70)
            self.Argent=max(0, self.Argent+325)
        elif emploi[3]==choix_2:
            self.Hygiene=min(100,self.Hygiene-50)
            self.Argent=max(0, self.Argent+450)
        elif emploi[4]==choix_2:
            self.Hygiene=min(100,self.Hygiene-90)
            self.Argent=max(0, self.Argent+175)
        elif emploi[5]==choix_2:
            self.Hygiene=min(100,self.Hygiene-90)
            self.Argent=max(0, self.Argent+250)
                            
        print(f"Bonjours vous avez obtenue {choix_2} comme emploi !!")
        print(f"Vodre salaire par jour est de {self.Argent} € Felecitation")
        print(f"Par contre vous perdrais {self.Hygiene} comme Hygiene")
    def faire_du_sport(self):
        self.Hygienes =min(100, self.Hygiene -70)
        self.Loisir =min(100, self.Loisir +35)
        
        
        
        
    def discuter(self):
        self.relation =min(100, self.relation +30)
        self.Hygiene =max(0,self.Hygiene -20)



        
        