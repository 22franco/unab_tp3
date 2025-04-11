<<<<<<< HEAD
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def __str__(self):
        return f"Autor: {self.nombre}"
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nuevo_autor):
        self.nombre = nuevo_autor

class Libro:
    def __init__(self, titulo, autor, ISBN, lugar, fecha_edicion, paginas, edicion, editorial):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.paginas = paginas
        self.lugar = lugar
        self.fecha_edicion = fecha_edicion
        self.edicion = edicion
        self.editorial = editorial
        
    #Metodo para leer la informacion de forma general usando diccionario
    def get_informacion(self, ):
        return {
            'titulo': self.titulo,
            'ISBN': self.ISBN,
            'Lugar': self.lugar,
            'Fecha de Edición': self.fecha_edicion,
            'Paginas': self.paginas,
            'Edición': self.edicion,
            'Editorial': self.editorial
        }
              
    # getters para acceder a la informacion de forma particular
    def get_titulo(self):
        return self.titulo
    
    def get_ISBN(self):
        return self.ISBN
    
    def get_paginas(self):
        return self.paginas
    
    def get_edicion(self):
        return self.edicion
    
    def get_editorial(self):
        return self.editorial
    
    def get_lugar(self):
        return self.lugar
    
    def get_fecha_edicion(self):
        return self.fecha_edicion
    
    
    #setters
    def set_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo
    
    def set_ISBN(self, nuevo_ISBN):
        self.ISBN = nuevo_ISBN
    
    def set_paginas(self, nueva_pagina):
        self.paginas = nueva_pagina
        
    def set_edicion(self, nueva_edicion):
        self.edicion = nueva_edicion
        
    def set_editorial(self, nueva_editorial):
        self.editorial = nueva_editorial
    
    def set_lugar(self, nuevo_lugar):
        self.lugar = nuevo_lugar
    
    def set_fecha_edicion(self, nueva_fecha):
        self.fecha_edicion = nueva_fecha
      
    # Metodo para mostrar la información   
    def __str__(self):
        return f"Titulo: {self.titulo} {self.edicion}\n{self.autor}\nISBN: {self.ISBN}\n{self.editorial} {self.lugar}\n{self.fecha_edicion}\n{self.paginas}"

        
autor = Persona("Liang. Y. Daniel")

biblioteca = Libro("Introduction to Java Programming",autor,"0-13-031997-X", "New Jersey (USA)", 
"Viernes 16 de noviembre de 2001","784 páginas","3a. edición", "Prentice-Hall,")

#Imprime la informacion del libro con el formato solicitado
print(biblioteca)


"""
#Imprime todos los getters
print(biblioteca.get_titulo()) 
print(autor.get_nombre())
print(biblioteca.get_ISBN())  
print(biblioteca.get_paginas())  
print(biblioteca.get_edicion())  
print(biblioteca.get_editorial())  
print(biblioteca.get_lugar())  
print(biblioteca.get_fecha_edicion())  


# defino los setters
biblioteca.set_titulo("Nuevo título de Java")
autor.set_nombre("Jhon Mion")
biblioteca.set_ISBN("1-23-456789-X")
biblioteca.set_paginas("800 páginas")
biblioteca.set_edicion("4a. edición")
biblioteca.set_editorial("New Editorial")
biblioteca.set_lugar("California (USA)")
biblioteca.set_fecha_edicion("Lunes 20 de diciembre de 2021")


# Imprimir la información actualizada con setters
print("\nInformación actualizada con setters:")
print(biblioteca.get_titulo())  
print(autor.get_nombre())
print(biblioteca.get_ISBN())  
print(biblioteca.get_paginas())  
print(biblioteca.get_edicion())  
print(biblioteca.get_editorial())  
print(biblioteca.get_lugar())  
print(biblioteca.get_fecha_edicion()) 
"""
=======
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def __str__(self):
         # muestra el nombre como autor
        return f"Autor: {self.nombre}"
    
    def get_nombre(self):
        # devuelve el nombre de la persona
        return self.nombre
    
    def set_nombre(self, nuevo_autor):
        # cambia el nombre de la persona
        self.nombre = nuevo_autor

class Libro:        # guarda los datos del libro
    def __init__(self, titulo, autor, ISBN, lugar, fecha_edicion, paginas, edicion, editorial):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.paginas = paginas
        self.lugar = lugar
        self.fecha_edicion = fecha_edicion
        self.edicion = edicion
        self.editorial = editorial
        
    # devuelve toda la información del libro en un diccionario
    def get_informacion(self, ):
        return {
            'titulo': self.titulo,
            'ISBN': self.ISBN,
            'Lugar': self.lugar,
            'Fecha de Edición': self.fecha_edicion,
            'Paginas': self.paginas,
            'Edición': self.edicion,
            'Editorial': self.editorial
        }
              
    #metodos para obtener datos especificos
    def get_titulo(self):
        return self.titulo
    
    def get_ISBN(self):
        return self.ISBN
    
    def get_paginas(self):
        return self.paginas
    
    def get_edicion(self):
        return self.edicion
    
    def get_editorial(self):
        return self.editorial
    
    def get_lugar(self):
        return self.lugar
    
    def get_fecha_edicion(self):
        return self.fecha_edicion
    
    
    ## metodos para modificar los datos
    def set_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo
    
    def set_ISBN(self, nuevo_ISBN):
        self.ISBN = nuevo_ISBN
    
    def set_paginas(self, nueva_pagina):
        self.paginas = nueva_pagina
        
    def set_edicion(self, nueva_edicion):
        self.edicion = nueva_edicion
        
    def set_editorial(self, nueva_editorial):
        self.editorial = nueva_editorial
    
    def set_lugar(self, nuevo_lugar):
        self.lugar = nuevo_lugar
    
    def set_fecha_edicion(self, nueva_fecha):
        self.fecha_edicion = nueva_fecha
      
    # Metodo para mostrar la informacion   
    def __str__(self):
        return f"Titulo: {self.titulo} {self.edicion}\n{self.autor}\nISBN: {self.ISBN}\n{self.editorial} {self.lugar}\n{self.fecha_edicion}\n{self.paginas}"

# se crea un autor
autor = Persona("Liang. Y. Daniel")

biblioteca = Libro("Introduction to Java Programming",autor,"0-13-031997-X", "New Jersey (USA)", 
"Viernes 16 de noviembre de 2001","784 páginas","3a. edición", "Prentice-Hall,")

#Imprime la informacion del libro con el formato solicitado
print(biblioteca)


"""
# se imprimen datos individuales usando getters
print(biblioteca.get_titulo()) 
print(autor.get_nombre())
print(biblioteca.get_ISBN())  
print(biblioteca.get_paginas())  
print(biblioteca.get_edicion())  
print(biblioteca.get_editorial())  
print(biblioteca.get_lugar())  
print(biblioteca.get_fecha_edicion())  


# se actualizan los datos del libro y del autor con setters
biblioteca.set_titulo("Nuevo título de Java")
autor.set_nombre("Jhon Mion")
biblioteca.set_ISBN("1-23-456789-X")
biblioteca.set_paginas("800 páginas")
biblioteca.set_edicion("4a. edición")
biblioteca.set_editorial("New Editorial")
biblioteca.set_lugar("California (USA)")
biblioteca.set_fecha_edicion("Lunes 20 de diciembre de 2021")


# se muestran los datos actualizados
print("\nInformación actualizada con setters:")
print(biblioteca.get_titulo())  
print(autor.get_nombre())
print(biblioteca.get_ISBN())  
print(biblioteca.get_paginas())  
print(biblioteca.get_edicion())  
print(biblioteca.get_editorial())  
print(biblioteca.get_lugar())  
print(biblioteca.get_fecha_edicion()) 
"""
>>>>>>> 6ac26b88ce9965ff86c7146b36609ca2ee7138db
