# import math

# print(math.factorial(5))

# from math import factorial

# n = int(input("utiliser un nombre \n"))

# def fonction(number):
#     print(factorial(number))

# fonction(n)


# from math import factorial,sqrt

# print(factorial (5))
# print(sqrt (9))

# from math import pi

# r= int(input("choisir valeur rayon r: "))
# p=2*pi*r
# print(f"le périmètre du cercle de rayon {p}")


# from math import pi

# r= int(input("choisir valeur rayon r: "))
# p=2*pi*r
# print("le périmètre du cercle de rayon" + str(p))


# from datetime import datetime, timedelta

# date_today=datetime.now().date()

# new_date=date_today + timedelta(days=7)

# print(new_date.strftime("%d/%m/%Y"))

from datetime import datetime, timedelta

date_today=datetime.now()

new_hour= date_today + timedelta(hours=3)

print(new_hour.strftime("%H:%M"))

