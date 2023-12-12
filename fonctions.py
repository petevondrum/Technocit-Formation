# def average(number_1, number_2):
#     average = (number_1 + number_2) / 2
#     return average

# result = average(3, 8)
# print(result)

# def ajouter_un(nombre):
#     nombre += 5
#     return nombre
# age = 25
# result_age = ajouter_un(age)
# print(result_age)

# def add_identity (name,year_born):
#     age = 2050 - year_born
#     print (f"Bonjour, je m'appelle {name}, en 2050 j'aurais {age}")

# add_identity ("Pierrino", 1980) 

n = 0

while n<10 or n>20:
    n = int(input("donner un nombre en 10 et 20 "))

    if n<10:
        print("plus grand!")
    if n>20:
        print("plus petit!")

print("bien joué!")
