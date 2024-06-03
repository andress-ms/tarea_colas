# Escribe un programa en Python que simule un proceso de procesamiento de datos usando una
# cola. El programa debe realizar las siguientes operaciones:
# 1. Agregar datos a la cola.
# 2. Procesar datos de la cola (por ejemplo, mostrar, modificar o eliminar datos).
# 3. Mostrar el estado final de la cola después del procesamiento

class Cola:
    
    def __init__(self):
        self.cola = []
        
    def agregar(self, dato):
        self.cola.append(dato)
        
    def mostrar(self):
        for i in self.cola:
            print(i)
                 
    def modificar(self, dato, i):
        if self.cola:
            self.cola[i] = dato
        else:
            print("La cola esta vacia")
            
    def eliminar(self):
        if self.cola:
            valor = self.cola.pop(0)
            print(f"Se ha desencolado el valor {valor}")            
        else:
            print("La cola esta vacia")

cola = Cola()
            

while True:
    print("\n1. Agregar un elemento a la cola")
    print("2. Mostrar cola")
    print("3. Modificar un elemento de la cola")
    print("4. Desencolar un elemento de la cola")
    print("5. Salir") 

    opcion = int(input("Ingrese la opcion que desea realizar: "))
    if opcion == 1:
        valor = int(input("Ingrese el valor que desea agregar a la cola: "))
        cola.agregar(valor)
    elif opcion == 2:
        cola.mostrar()
    elif opcion == 3:
        i = int(input("Ingrese la posicion del elemento de la cola que desea modificar: "))
        valor = int(input("Ingrese el nuevo valor del elemento en la cola: "))
        cola.modificar(valor, i-1)    
    elif opcion == 4:
        cola.eliminar()
    elif opcion == 5:
            break