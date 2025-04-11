<<<<<<< HEAD
class Cancion:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
    def __str__(self):
        return f"El titulo es: {self.titulo}\nEl autor es: {self.autor}"
    
    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor
    
    def set_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo
        
    def set_autor(self, nuevo_autor):
        self.autor = nuevo_autor
        
        
grabacion = Cancion("Despues de las 6", "Flaco Spinetta")
print(grabacion)

print(grabacion.get_autor())
print(grabacion.get_titulo())

# Verificar los setters
grabacion.set_autor("Gustavo Cerati")
grabacion.set_titulo("Noche encantadora")

print(grabacion)
print(grabacion.get_autor())
print(grabacion.get_titulo())
=======
class Cancion:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
    def __str__(self):
        # muestra la cancion como texto con titulo y autor
        return f"El titulo es: {self.titulo}\nEl autor es: {self.autor}"
    
    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor
    
    def set_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo
        
    def set_autor(self, nuevo_autor):
        self.autor = nuevo_autor
        
# se crea una cancion y se muestran sus datos        
grabacion = Cancion("Despues de las 6", "Flaco Spinetta")
print(grabacion)

# se imprime el autor y el titulo por separado
print(grabacion.get_autor())
print(grabacion.get_titulo())

# # se cambia el autor y el titulo
grabacion.set_autor("Gustavo Cerati")
grabacion.set_titulo("Noche encantadora")

# se muestran los nuevos datos
print(grabacion)
print(grabacion.get_autor())
print(grabacion.get_titulo())
>>>>>>> 6ac26b88ce9965ff86c7146b36609ca2ee7138db
