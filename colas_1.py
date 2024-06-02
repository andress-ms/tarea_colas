"""Ejercicio 1: Implementación de una Cola
Escribe un programa en Python que implemente una cola y realice las siguientes operaciones:
1. Agregar elementos a la cola.
2. Eliminar elementos de la cola.
3. Mostrar el elemento en la parte frontal de la cola sin eliminarlo.
4. Mostrar todos los elementos de la cola."""

class Cola:
    def __init__ (self):
        self.elementos=[]
    
    def esta_vacia(self):
        return len(self.elementos) == 0
        
    def encolar(self, elemento):
        self.elementos.append(elemento)
        print(f"Elemento {elemento} agregado a la cola.")
        
    def desencolar(self):
        if self.esta_vacia():
            print("La cola esta vacia")
            return None
        else:
            return self.elementos.pop(0)
        
    def frente(self):
        if self.esta_vacia():
            print("La cola esta vacia")
            return None
        else:
            return self.elementos[0]
        
    def mostrar_cola(self):
        if self.esta_vacia():
            print("La cola esta vacia")
        else:
            print("Elementos en la cola:", self.elementos)
            
cola = Cola()

while True:
    print("\nOpciones:")
    print("1. Agregar elementos a la cola")
    print("2. Eliminar elementos de la cola")
    print("3. Mostrar el elemento en la parte frontal de la cola")
    print("4. Mostrar todos los elementos de la cola")
    print("5. Salir")
    
    opcion = input("Ingrese la opcion deseada ")
    
    if opcion == '1':
        cantidad = int(input("Ingrese la cantidad de elementos a agregar: "))
        for i in range(cantidad):
            elemento = input(f"Ingrese el elemento {i+1}: ")
            cola.encolar(elemento)
    elif opcion == '2':
        elemento_eliminado = cola.desencolar()
        if elemento_eliminado is not None:
            print(f"Elemento {elemento_eliminado} eliminado de la cola.")
    elif opcion == '3':
        elemento_frontal = cola.frente()
        if elemento_frontal is not None:
            print(f"Elemento en la parte frontal de la cola: {elemento_frontal}")
    elif opcion == '4':
        cola.mostrar_cola()
    elif opcion == '5':
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, ingrese un número válido.")
    