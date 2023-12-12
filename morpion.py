print("choose a number on the numpad between 1 and 9 as if it were a tic-tac-toe game. Player 1 is X, Plauer 2 is O")
case_1 = "" 
case_2 = ""
case_3 = ""
case_4 = ""
case_5 = ""
case_6 = ""
case_7 = ""
case_8 = ""
case_9 = ""
#condition boucle
score_1=0
score_2=0
#boucle
while (score_1<1 and score_2<1):
    joueur1 = int(input("joueur1, choisis une case (1-9) \n"))
    
    if joueur1 == 1:
        case_1 = "X"
    elif joueur1 == 2:
        case_2 = "X"
    elif joueur1 == 3:
        case_3 = "X"
    elif joueur1 == 4:
        case_4 = "X"
    elif joueur1 == 5:
        case_5 = "X"
    elif joueur1 == 6:
        case_6 = "X"
    elif joueur1 == 7:
        case_7 = "X"
    elif joueur1 == 8:
        case_8 = "X"
    elif joueur1 == 9:
        case_9 = "X"
    
    #condition victoire
    if (case_1 == case_2 == case_3 == "X"\
        or case_4 == case_5 == case_6 == "X"\
        or case_7 == case_8 == case_9 == "X"\
        or case_1 == case_4 == case_7 == "X"\
        or case_2 == case_5 == case_8 == "X"\
        or case_3 == case_6 == case_9 == "X"):
        score_1 += 1
        continue

    joueur2 = int(input("joueur2, choisis une case (1-9) \n"))

    if joueur2 == 1:
        case_1 = "O"
    elif joueur2 == 2:
        case_2 = "O"
    elif joueur2 == 3:
        case_3 = "O"
    elif joueur2 == 4:
        case_4 = "O"
    elif joueur2 == 5:
        case_5 = "O"
    elif joueur2 == 6:
        case_6 = "O"
    elif joueur2 == 7:
        case_7 = "O"
    elif joueur2 == 8:
        case_8 = "O"
    elif joueur2 == 9:
        case_9 = "O"                           

    if (case_1 == case_2 == case_3 == "O"\
        or case_4 == case_5 == case_6 == "O"\
        or case_7 == case_8 == case_9 == "O"\
        or case_1 == case_4 == case_7 == "O"\
        or case_2 == case_5 == case_8 == "O"\
        or case_3 == case_6 == case_9 == "O"):
        score_2 += 1 

    elif not "" == (case_1 and case_2 and case_3 and case_4 and case_5 and case_6 and case_7 and case_8 and case_9):
        print = ("Pas de gagnant")
        break

if score_1==1:
    print("Joueur1 bravo tu as gagné")
elif score_2==2:
    print("Joueur2 bravo tu as gagné")
                     