"""Crea un programa en Python que simule una cola circular con las siguientes operaciones:
1. Agregar elementos a la cola circular.
2. Eliminar elementos de la cola circular.
3. Mostrar el elemento en la parte frontal de la cola circular sin eliminarlo.
4. Mostrar todos los elementos de la cola circular."""

class ColaCircular:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.cola = [None] * tamaño
        self.frente = self.final = -1
        self.elementos_adicionales = []
        
    def encolar(self, elemento):
        if (self.final + 1) % self.tamaño == self.frente:
            print("La cola está llena")
            self.elementos_adicionales.append(elemento)
        elif self.frente == -1:
            self.frente = self.final = 0
            self.cola[self.final] = elemento
        else:
            self.final = (self.final + 1) % self.tamaño
            self.cola[self.final] = elemento
            
    def desencolar(self):
        if self.frente == -1:
            print("La cola esta vacia")
        else:
            print("Elemento desencolado:", self.cola[self.frente])
            if self.frente == self.final:
                self.frente = self.final = -1
            else:
                self.frente = (self.frente + 1) % self.tamaño
            
            if self.elementos_adicionales:
                elemento = self.elementos_adicionales.pop(0)
                self.encolar(elemento)
            
    def ver_frente(self):
        if self.frente == -1:
            print("La cola esta vacia")
        else:
            print("El elemento al frente de la cola es:", self.cola[self.frente])
            
    def mostrar(self):
        if self.frente == -1:
            print("La cola está vacia")
        else:
            print("Elementos de la cola circular:")
            if self.final >= self.frente:
                for i in range(self.frente, self.final + 1):
                    print(self.cola[i], end=" ")
                print()
            else:
                for i in range(self.frente, self.tamaño):
                    print(self.cola[i], end=" ")
                for i in range(0, self.final + 1):
                    print(self.cola[i], end=" ")
                print()


def obtener_lista_elementos(tamaño_cola):
    elementos = []
    for _ in range(tamaño_cola):
        elemento = input(f"Ingrese el elemento {len(elementos) + 1}/{tamaño_cola} para encolar (o presione Enter para terminar): ")
        if elemento == "":
            break
        elementos.append(elemento)
    return elementos

if __name__ == "__main__":
    tamaño_cola = int(input("Ingrese el tamaño de la cola circular: "))
    cola = ColaCircular(tamaño_cola)

    while True:
        print("\nOpciones:")
        print("1. Encolar elementos")
        print("2. Desencolar elemento")
        print("3. Ver elemento en frente")
        print("4. Mostrar todos los elementos")
        print("5. Salir")
        
        opcion = int(input("Ingrese la opción deseada: "))
        
        if opcion == 1:
            elementos = obtener_lista_elementos(tamaño_cola - (cola.final - cola.frente))
            for elemento in elementos:
                cola.encolar(elemento)
        elif opcion == 2:
            cola.desencolar()
        elif opcion == 3:
            cola.ver_frente()
        elif opcion == 4:
            cola.mostrar()
        elif opcion == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opcion inválida.")