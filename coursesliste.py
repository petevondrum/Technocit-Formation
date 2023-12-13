# Affichage Menu
def afficher_menu():
    print("*"*19 +" Menu :"+"*"*20)
    print("1." + "*"*13 + "Ajouter un article" + "*"*13)
    print("2." + "*"*12 + "Supprimer un article" + "*"*12)
    print("3."+ "*"*13 + "Afficher la liste"+ "*"*14)
    print("4." + "*"*8 + "Vider complètement la liste" + "*"*9)
    print("5." + "*"*17 + "Quitter" + "*"*20)

# Créer une liste de courses
def creer_liste_courses():
    return []

# Ajouter un article
def ajouter_article(liste):
    article = input("Entrer le nom de l'article à ajouter: ")
    liste.append(article)
    print(f"{article} a été ajouté à la liste.")

# Supprimer un article
def supprimer_article(liste):
    article = input("Entrer le nom de l'article à supprimer de la liste: ")
    if article in liste:
        liste.remove(article)
        print(f"{article} a été supprimé de la liste.")
    else:
        print(f"{article} n'est pas dans la liste.")

# Afficher la liste
def afficher_liste(liste):
    print("\nListe de course: ")
    for article in liste:
        print(article)

# Vider la liste
def vider_liste(liste):
    confirmation = input("\nEtes-vous sûr de vouloir vider la liste ? (O/N) : ")
    if confirmation.lower() == 'o':
        liste.clear()
        print("La liste a été vidée.")
    else:
        print("La liste n'a pas été vidée.")

# Exemple d'utilisation
ma_liste = creer_liste_courses()

while True:
    afficher_menu()
    choix = input("\nEntrez le numéro de votre choix : ")

    if choix == '1':
        ajouter_article(ma_liste)
    elif choix == '2':
        supprimer_article(ma_liste)
    elif choix == '3':
        afficher_liste(ma_liste)
    elif choix == '4':
        vider_liste(ma_liste)
    elif choix == '5':
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez entrer un numéro valide.")
