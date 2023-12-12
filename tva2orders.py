achat1 = 500
achat2 = 1426

def calculate_tva(fullprice):
    tva = (fullprice/100)*21
    return tva

tva_achat1 = calculate_tva(achat1)
tva_achat2 = calculate_tva(achat2)
sum_tva = tva_achat1 + tva_achat2
#écrire un string avec f (format)
print(f"lapremière tva est {tva_achat1}")
#écrire un string avec la concaténation
print("La deuxième tva est " + str(tva_achat2))
print(f"La somme des 2 est {sum_tva}")