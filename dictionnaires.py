# dictionnary = {
#     'color' : 'red',
#     'name' : 'Jim',
#     'number' : 1994
# }
# print(dictionnary)
# print(dictionnary['color'])

# dacia = {
#     'genre' : 'utilitaire',
#     'couleur' : 'black',
#     'fuel': 'diesel'    
# }
# print(dacia)
# dacia['fuel']="essence"
# print(dacia)


# employees = {
#     'boss' : {'name': 'Anna', 'salary': 3000},
#     'accountant': {'name': 'Martin','salary':2300},
#     'intern': {'name': 'Fred', 'samary': 0},
# }
# employees['accountant']['salary']= 2800
# print(employees)

# def reverse(chaine):
#     return chaine[::-1]
# original_chain= "Mieux","cher"
# reverse_chain= reverse(original_chain)
# print(original_chain)
# print(reverse_chain)
  
# def reverse(mot):
#       list_caracteres= list(mot)
#       list_caracteres.reverse()
#       mot_inverse="".join(list_caracteres)
#       return mot_inverse
# mot_original= "Ordinateur"
# mot_inverse=reverse(mot_original)
  
# print("Mot original: ", mot_original)
# print("Mot inversé: ", mot_inverse)
 
def supprimer_caractère(chaine,caractère):
    return chaine.replace(caractère, "")
chaine_originale= "Balibobalo"
caractère_à_supprimer="o"
chaine_new=supprimer_caractère(chaine_originale,caractère_à_supprimer)
print("Chaine originale :", chaine_originale)
print(f"chaine sans '{caractère_à_supprimer}' :", chaine_new)
      
      
      