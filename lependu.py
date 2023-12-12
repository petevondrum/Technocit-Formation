mot_à_trouver = "balançoire"
mot__caché = "_" * len(mot_à_trouver)
vies= 5

print("Bienvenu au Pendu !")
print("Mot à trouver: " + mot__caché)

while vies > 0 and "_" in mot__caché:
    lettre = input("Entrez une lettre !")
    if lettre in mot_à_trouver:
        print("Bien deviné!")
        # char est une variable temporaire utile ds la comprehension de liste pour extraire les occurences de la lettre 
        # devinée ds le mot à trouver. enumerate(mot_à_trouver): cette fonction énumère les caratère du mot 
        # mot_à_trouver avec leur indice associé. cela renvoie des tuplesde la forme (indice, caractère).
        # for i, char in ... : la boucle for déstructure ces tuples en variables i pour l'indice et char pour le caractère.
        # if char == lettre/ Cela filtre les tuples pour inclure uniquement ceux où le caractère est égal à la lettre devinée (lettre).
        #[i for ...: ceci crée une liste des indices(i) correspondants aux occurences de la lettre dans le mot
        
        indices = [i for i, char in enumerate(mot_à_trouver) if char == lettre]
        for index in indices:
            mot__caché= mot__caché[:index] + lettre + mot__caché[index +1:]
    else:
        vies-=1
        print(f"Mal deviné. Il vous reste {vies} vies.")
        
    print("Mot actuel : " + mot__caché)
    if "_" not in mot__caché:
        print("Félicitations, vous avez trouvé le mot: "+ mot_à_trouver)
    else:
        print("Désolé vous avez épuisé vos vies, le mot était" + mot_à_trouver)
        
        
        
        # liste d'indices en utilisant la fonction range pour générer des indices allant de o à la longueur du mot à trouver. 
        # La condition mot_à_trouver[i] == lettre est utilisée pour filtrer les indices où la lettre devinée correspond à 
        # la lettre du mot à trouver à cet indice. la boucle for rest la même et utilise les indices pour mettre à jour le mot_caché. 
        # Elle utilise une liste plutôt que des tuples pour stocker les indices des occurences de la lettre devinée dans le mot à trouver: 
        
        indices = [i for i in range(len(mot_à_trouver)) if mot_à_trouver[i]==lettre]
        
        for index in indices:
            mot__caché = mot__caché[:index] + lettre + mot__caché[index +1]