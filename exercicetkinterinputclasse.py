import tkinter

window = tkinter.Tk()

window.title('Classe of 23')

window.geometry('600x600')

window.configure(bg="blue")

texte = "This was 23's Class!"
paragraphe = tkinter.Label(window, text=texte, font=("American Typewriter", 28, "bold"), fg="red", wraplength=200, anchor="n", justify="center")
paragraphe.pack()

# Liste pour stocker les personnes de la classe
liste_personnes = []

def ajouter_personne():
    nom_personne = entry.get()

    if nom_personne:
        liste_personnes.append(nom_personne)
        paragraphe["text"] = f"Dernière personne ajoutée : {nom_personne}"
        entry.delete(0, 'end')

def supprimer_derniere_personne():
    if liste_personnes:
        dernier_element = liste_personnes.pop()
        paragraphe["text"] = f"Dernière personne supprimée : {dernier_element}"

# Bouton pour ajouter une personne
button_ajouter = tkinter.Button(window, text="Ajouter Personne", command=ajouter_personne)
button_ajouter.pack()

# Bouton pour supprimer la dernière personne ajoutée
button_supprimer = tkinter.Button(window, text="Supprimer Dernière Personne", command=supprimer_derniere_personne)
button_supprimer.pack()

window.mainloop()



    
    