'''
NOMBRE: Clases de Animales
AUTOR: Palafox Collaodo Dara Jazheel. darapc@lcg.unam.mx
DESCRIPCIÓN: Este programa define clases para representar diferentes animales y sus sonidos característicos.
CATEGORÍA: Programación orientada a objetos
'''

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def haz_ruido(self):
        print("AAAAAAAAAAAAH")

class Perro(Animal):
    def haz_ruido(self):
        print("Guau")

class Gato(Animal):
    def __init__(self, nombre, edad, usa_arenero):
        super().__init__(nombre, edad)
        self.usa_arenero = usa_arenero
    
    def haz_ruido(self):
        print("Miau")

mi_perro = Perro("Cloe", 3)
mi_gato = Gato("Millie", 2, True)

mi_perro.haz_ruido()
mi_gato.haz_ruido()

print(vars(mi_perro))
print(vars(mi_gato))
