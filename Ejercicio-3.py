<<<<<<< HEAD
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x}, {self.y})"

class Linea:
    def __init__(self, punto_a, punto_b):
        self._punto_a = punto_a
        self._punto_b = punto_b

              
    def mueve_derecha(self, distancia):
        self._punto_a.x += distancia
        self._punto_b.x += distancia
     
    def mueve_izquierda(self, distancia):
        self._punto_a.x -= distancia
        self._punto_b.x -= distancia
        
    def mueve_arriba(self, distancia):
        self._punto_a.y += distancia
        self._punto_b.y += distancia
        
    def mueve_abajo(self,distancia):
        self._punto_a.y -= distancia
        self._punto_b.y -= distancia
        
        
    
    def __str__(self):
        return f"Línea de {self._punto_a} a {self._punto_b}"
    
    
punto1 = Punto(1,2)
punto2 = Punto(3,4)

linea = Linea(punto1,punto2)
print(linea)

linea.mueve_derecha(3)
print(linea)

linea.mueve_izquierda(1)
print(linea)

linea.mueve_arriba(2)
print(linea)

linea.mueve_abajo(3)
print(linea)
=======
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        # muestra el punto como texto (x, y)
        return f"({self.x}, {self.y})"

class Linea:
    def __init__(self, punto_a, punto_b):
        # guarda los dos puntos que forman la linea
        self._punto_a = punto_a
        self._punto_b = punto_b

              
    def mueve_derecha(self, distancia):
        # mueve la linea a la derecha sumando a x
        self._punto_a.x += distancia
        self._punto_b.x += distancia
     
    def mueve_izquierda(self, distancia):
        # mueve la linea a la izquierda restando a x
        self._punto_a.x -= distancia
        self._punto_b.x -= distancia
        
    def mueve_arriba(self, distancia):
        # mueve la linea hacia arriba sumando a y
        self._punto_a.y += distancia
        self._punto_b.y += distancia
        
    def mueve_abajo(self,distancia):
        # mueve la linea hacia abajo restando a y
        self._punto_a.y -= distancia
        self._punto_b.y -= distancia
        
        
    
    def __str__(self):
        # muestra la liinea como texto con sus dos puntos
        return f"Línea de {self._punto_a} a {self._punto_b}"
    
# se crean dos puntos y una linea entre ellos
punto1 = Punto(1,2)
punto2 = Punto(3,4)

# se mueve la linea en diferentes direcciones
linea = Linea(punto1,punto2)
print(linea)

linea.mueve_derecha(3)
print(linea)

linea.mueve_izquierda(1)
print(linea)

linea.mueve_arriba(2)
print(linea)

linea.mueve_abajo(3)
print(linea)
>>>>>>> 6ac26b88ce9965ff86c7146b36609ca2ee7138db
