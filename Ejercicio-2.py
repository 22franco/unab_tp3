<<<<<<< HEAD
class punto:
    def __init__(self, eje_x, eje_y):
        self.eje_x = eje_x
        self.eje_y = eje_y
        
    def __str__(self):
        return f"El eje X es: {self.eje_x}\nEl eje Y es: {self.eje_y}"
    
    def opuesto(self):
        return f"El opuesto de X es: {-self.eje_x}\nEl opuesto de Y es: {-self.eje_y}"
    
    def modificar_puntos(self, punto_x, punto_y):
        self.eje_x = punto_x
        self.eje_y = punto_y

    
    
plano = punto(2, 4)
print(plano)
print(plano.opuesto()) 
plano.modificar_puntos(5, 6)
print(plano)
=======
class punto:
    def __init__(self, eje_x, eje_y):
        self.eje_x = eje_x
        self.eje_y = eje_y
        
    def __str__(self):
        # devuelve el punto como texto legible
        return f"El eje X es: {self.eje_x}\nEl eje Y es: {self.eje_y}"
    
    def opuesto(self):
        # devuelve los valores opuestos de 'x' e 'y'
        return f"El opuesto de X es: {-self.eje_x}\nEl opuesto de Y es: {-self.eje_y}"
    
    def modificar_puntos(self, punto_x, punto_y):
        # cambia los valores de 'x' e 'y' por otros nuevos
        self.eje_x = punto_x
        self.eje_y = punto_y

    
# se crea un punto y se usan sus funciones    
plano = punto(2, 4)
print(plano)
print(plano.opuesto()) 
plano.modificar_puntos(5, 6)
print(plano)
>>>>>>> 6ac26b88ce9965ff86c7146b36609ca2ee7138db
