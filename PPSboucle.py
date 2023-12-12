

# nom1 = input("Quel est ton nom?")
# nom2 = input("Quel est ton nom?")

# score_1 = 0
# score_2 = 0

# while score_1 < 2 and score_2 < 2 :
    
#     joueur1 = input(nom1 + "Choisis entre pierre, papier, ciseaux \n")
#     bot = input(nom2 + "Choisis entre pierre, papier, ciseaux \n")

#     if joueur1 == "pierre" and bot == 1 or joueur1 == "papier" and bot == "pierre" or joueur1 == 1 and bot == "papier":
#         print ("le joueur1 gagne")
#         score_1 += 1
#     elif bot == "pierre" and joueur1 == 1 or bot == "papier" and joueur1 == "pierre" or bot == 1 and joueur1 == "papier":
#         print ("le bot gagne")
#         score_2 += 1
#     elif joueur1 == bot:
#         print ("Egalité")
#     else:
#         print ("une des données a été mal orthographiée")

# if score_1 == 2:
#     print (nom1 + " c'est gagné") 
# if score_2 == 2:
#     print (nom2 + " c'est gagné")                  
    


#exercice PPC en mode random 

import random
from random import randint

nom1 = input("Quel est ton nom? ")
score_1 = 0
score_2 = 0

while score_1 < 2 and score_2 < 2 :
    
    joueur1 = input("joueur1, choisis entre pierre, papier, ciseaux \n")
    bot = random.randint(1,3)
# ciseaux=1, pierre=2, papier=3
    if bot == 1:
        print("le bot a joué ciseaux")
    elif bot == 2:
        print("le bot a joué pierre")
    elif bot == 3:
        print("le bot a joué papier")    
# conditions de victoire
    if (joueur1 == "pierre" and bot == 1) or (joueur1 == "papier" and bot == 2) or (joueur1 == "ciseaux" and bot == 3):
         print ("le joueur1 gagne")
         score_1 += 1 
    elif (bot == 1 and joueur1 == "papier") or (bot == 2 and joueur1 == "ciseaux") or (bot == 3 and joueur1 == "pierre"):
        print ("le bot gagne")
        score_2 += 1
    elif (joueur1 == "pierre" and bot == 2) or (joueur1 == "ciseaux" and bot ==1) or (joueur1 == "papier" and bot == 3):
        print ("Egalité")
    else:
        print ("une des données a été mal orthographiée")

if score_1 == 2:
    print (nom1 + " c'est gagné") 
if score_2 == 2:
    print ("Le bot a gagné")                  
    