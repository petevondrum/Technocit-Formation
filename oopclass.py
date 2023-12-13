class Person:
    espèce_type = "Homo Sapiens"
    
    def __init__(self, Prénom, age, anniversaire):
        self.prénom = Prénom
        self.age = age
        self.anniversaire = anniversaire
        
    def dire_bonjour(self):
        return f"Bonjour! {self.prénom}"    
    
    def is_the_person_adult(self):
        adult_person = self.age >= 18
        if self.age >= 18:
            return f"{self.prénom} est majeur.e"
        else:
            return f"{self.prénom} est mineur.e"
    
        
pers1 = Person("Louis",42, 1981)
pers2 = Person("Aurore", 43, 1980)

print(pers1.prénom)
print(pers2.espèce_type)

pers1.age = 43

print(pers1.age)
print(pers1.dire_bonjour())
print(pers1.is_the_person_adult())    
        
        
#exercice      
class Employee(Person):
    
    def __init__(self, Prénom, age, anniversaire, salaire_par_mois, métier):
        self.prénom = Prénom
        self.age = age
        self.anniversaire = anniversaire
        self.salaire_par_mois = salaire_par_mois
        self.métier = métier
    def salaire_annuel (self):
        return self.salaire_par_mois*12
    
pers3 = Employee("Benoit", 32, 1991, 2500, "plombier")
print(pers3.salaire_annuel())
        
# super = va chercher la version de la méthode du parent