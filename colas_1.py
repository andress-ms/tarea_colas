"""Ejercicio 1: Implementación de una Cola
Escribe un programa en Python que implemente una cola y realice las siguientes operaciones:
1. Agregar elementos a la cola.
2. Eliminar elementos de la cola.
3. Mostrar el elemento en la parte frontal de la cola sin eliminarlo.
4. Mostrar todos los elementos de la cola."""

class Cola:
    def __init__ (self, elemento):
        self.elemento = elemento