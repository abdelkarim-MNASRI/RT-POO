class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = "Luna"
       
    def vieillir(self):
        self.age += 1
animal = Animal()
    
print(animal.age) 

animal.vieillir()

print(animal.age) 


class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = "Luna"
    
    def vieillir(self):
        self.age += 1
        
    def nommer(self, nom):
        self.prenom = nom
animal = Animal()
animal.nommer("Luna")
print(animal.prenom) 

