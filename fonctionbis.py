#fonctions exercices

#1

# def reverse(chaine):
#     return chaine[::-1]
# original_chain= "Mieux","cher"
# reverse_chain= reverse(original_chain)
# print(original_chain)
# print(reverse_chain)

#ou
  
# def reverse(mot):
#       list_caracteres= list(mot)
#       list_caracteres.reverse()
#       mot_inverse="".join(list_caracteres)
#       return mot_inverse
# mot_original= "Ordinateur"
# mot_inverse=reverse(mot_original)
  
# print("Mot original: ", mot_original)
# print("Mot inversé: ", mot_inverse)

#2
 
# def supprimer_caractère(chaine,caractère):
#     return chaine.replace(caractère, "")
# chaine_originale= "Balibobalo"
# caractère_à_supprimer="o"
# chaine_new=supprimer_caractère(chaine_originale,caractère_à_supprimer)
# print("Chaine originale :", chaine_originale)
# print(f"chaine sans '{caractère_à_supprimer}' :", chaine_new)

# # correction exercices

# #1

# string_to_reverse = 'ordinateur'
# second_string_to_reverse ="fenêtre"

# def reverse_string(word):
#      reverse_string = reversed(word)
#      return "".join(reverse_string)
# print(reverse_string(string_to_reverse))
# print(reverse_string(second_string_to_reverse))
    
#3

# def contient_alphabet(chaine):
#     chaine=chaine.lower()
#     for lettre in 'abcdefghijklmnopqrstuvwxyz':
#         if lettre not in chaine:
#             return False
#         return True  
# chaine_test1="abcdefghijklmnopqrstuvwxyz"
# chaine_test2= "Jingo Bingo"

# print(contient_alphabet(chaine_test1))
# print(contient_alphabet(chaine_test2))
# if contient_alphabet(chaine_test1):
#     print("Toutes les lettres sont dans l'alphabet")
# else:
#     print("t'as foiré")    
    
# correction exercice 2

# def remove_one_character(word, char):
#     list_word = list(word)
#     for i in list_word:
#         if i == char:
#             list_word.remove(i)
#     return "".join(list_word)  
# print(remove_one_character('exercice', 'e'))  

#ou

# def remove_one_character(word, char):
#     list_word = list(word)
#     while list_word.count(char) > 0 :
#         list_word.remove(char)
#     return "".join(list_word)

# print(remove_one_character('exercice', 'e'))      
               
# correction exercice 3

alphabet = "abcdefghijklmnopqrstuvwxyz"

def check_alphabet(word):
    print(alphabet)
    for letter in alphabet:
        print(letter)
        if letter not in word:
            print(word)
            return False
    return True
check_word = 'abcdefghijklmnopqrstuvwxyz'
is_in_alphabet=check_alphabet(check_word)

if is_in_alphabet:
    print(f"{check_word} contains all the alphabet") 
else:
    print(f"{check_word} does NOT contain all the alphabet")               
                