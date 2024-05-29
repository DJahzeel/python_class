'''
NOMBRE: Clases de Animales
AUTOR: Palafox Collaodo Dara Jazheel. darapc@lcg.unam.mx
DESCRIPCIÓN: Este programa define clases para representar diferentes animales y sus sonidos característicos.
CATEGORÍA: Programación orientada a objetos
'''

class Animal:
    """
    Clase base para representar un animal.
    """
    def __init__(self, nombre, edad):
        """
        Inicializa un objeto Animal con un nombre y edad.
        
        Args:
            nombre (str): El nombre del animal.
            edad (int): La edad del animal.
        """
        self.nombre = nombre
        self.edad = edad
    
    def haz_ruido(self):
        """
        Método para imprimir el sonido genérico de un animal.
        """
        print("AAAAAAAAAAAAH")

class Perro(Animal):
    """
    Clase que representa a un perro, hereda de la clase Animal.
    """
    def haz_ruido(self):
        print("Guau")

class Gato(Animal):
    """
    Clase que representa a un gato, hereda de la clase Animal.
    """
    def __init__(self, nombre, edad, usa_arenero):
        super().__init__(nombre, edad)
        self.usa_arenero = usa_arenero
    
    def haz_ruido(self):
        """
        Método para imprimir el maullido de un gato.
        """
        print("Miau")

mi_perro = Perro("Cloe", 3)
mi_gato = Gato("Millie", 2, True)
# Llamadas a los métodos haz_ruido() de las instancias
mi_perro.haz_ruido()
mi_gato.haz_ruido()
# Imprimir los atributos
print(vars(mi_perro))
print(vars(mi_gato))
