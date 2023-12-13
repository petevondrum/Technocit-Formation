import tkinter

window = tkinter.Tk()

window.title('Jingo Bingo')

window.geometry('600x600')

#window.state('zoomed')

window.configure(bg="pink")

#window['bg'] = "blue"

texte = "C'est le Jingo Bingo!"

paragraphe = tkinter.Label(window, text = texte, font=("American Typewriter", 28, "bold"), fg="red", wraplength= 200, anchor="n", justify="center")

paragraphe.pack()

def on_click():
    print('clic enregistré !')
    
my_button= tkinter.Button(window, text= "Push !", command=on_click)

my_button.pack() 

def print_entered_value():
    value = entry.get()
    print("Ton non âge est: ", value) 
    entry.delete(0,'end')
    
entry = tkinter.Entry(window)
entry.pack()

button = tkinter.Button(window, text="submit", command=print_entered_value)
button.pack()      

window.mainloop()


    
    