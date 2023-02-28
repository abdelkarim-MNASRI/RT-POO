class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def afficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")
    
    def afficherX(self):
        print(f"Coordonnée x : {self.x}")
    
    def afficherY(self):
        print(f"Coordonnée y : {self.y}")
    
    def changerX(self, nouveauX):
        self.x = nouveauX
    
    def changerY(self, nouveauY):
        self.y = nouveauY

point = Point(3, 4)

point.afficherLesPoints() 
point.afficherX() 
point.afficherY() 

point.changerX(5)
point.changerY(6)

point.afficherLesPoints() 
