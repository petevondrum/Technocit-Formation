# meteo = input("quelle est la météo ?")

# if meteo == "pluie":
#     print("sortez les parapluies!")
# elif meteo == "soleil":
#     print("n'oublie pas ta casquette !")    
# else:
#     print("pas d'info sur la météo...")

# age = input("Quel est l'âge de l'entrant?")

# if int(age) >= 18:
#     print ("entrée acceptée")

# else:
#     print ("entrée refusée")

# number1 = input("entrer le premier nombre ")
# number2 = input("entrer le deuxième nombre ")

# if int(number1)> int(number2):
#     print (number1)

# elif int(number2)> int(number1):
#     print (number2)

# elif int(number1) == int(number2):
#     print ("Egalité")

# number1 = int(input("entrer le premier nombre "))
# number2 = int(input("entrer le deuxième nombre "))
# number3 = int(input("entrer le troisième nombre "))

# if number1 > number2 and number1 > number3:
#     print ('le plus grand est '+ str(number1))

# elif number1 < number2 and number2 > number3:
#     print ('le plus grand est '+ str(number2))

# elif number3 > number2 and number3 > number1:
#     print ('le plus grand nombre est '+ str(number3))

# else:
#     print ("Egalité")


# X = int(input("entrer le premier nombre "))
# Y = int(input("entrer le deuxième nombre "))

# if X > 0 or Y > 0:
#     print ("Bravo!")


nom1 = input("Quel est ton nom?")
nom2 = input("Quel est ton nom?")
joueur1 = input(nom1 + "Choisis entre pierre, papier, ciseaux \n")
joueur2 = input(nom2 + "Choisis entre pierre, papier, ciseaux \n")

if joueur1 == "pierre" and joueur2 == "ciseaux" or joueur1 == "papier" and joueur2 == "pierre" or joueur1 == "ciseaux" and joueur2 == "papier":
    print ("le joueur1 gagne")
elif joueur2 == "pierre" and joueur1 == "ciseaux" or joueur2 == "papier" and joueur1 == "pierre" or joueur2 == "ciseaux" and joueur1 == "papier":
    print ("le joueur2 gagne")
elif joueur1 == 
joueur2:
    print ("Egalité")
else:
    print ("une des données a été mal orthographiée")       

