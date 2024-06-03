# Desarrolla un programa en Python que simule un sistema de gestión de tareas pendientes
# utilizando una cola. El programa debe permitir:
# 1. Agregar tareas pendientes a la cola.
# 2. Marcar una tarea como completada y eliminarla de la cola.
# 3. Mostrar la próxima tarea a realizar.
# 4. Mostrar todas las tareas pendientes en la cola.

class Cola:
    
    def __init__(self):
        self.cola = []
        
    def agregar(self, dato):
        self.cola.append(dato)
        
    def mostrar(self):
        for i in self.cola:
            print(i)
                 
    def mostrar_prox(self):
        if self.cola:
            print(f"\nLa proxima tarea es: {self.cola[1]}")
        else:
            print("La cola esta vacia")
            
    def obtener_curso(self):
        if self.cola:
            return self.cola[0]
        else:
            return None
         
    def eliminar(self):
        if self.cola:
            valor = self.cola.pop(0)
            print(f"La tarea '{valor}' se ha marcado como completada.")            
        else:
            print("La cola esta vacia")

cola = Cola()
            

while True:
    if cola.obtener_curso() is not None:
        print(f"\nTarea en curso: {cola.obtener_curso()}")
        
    print("\n1. Agregar una tarea a la cola")
    print("2. Marcar como terminada la tarea en curso")
    print("3. Mostrar proxima tarea")
    print("4. Mostrar todas las tareas pendientes")
    print("5. Salir") 

    opcion = int(input("Ingrese la opcion que desea realizar: "))
    if opcion == 1:
        valor = input("Ingrese la tarea que desea agregar a la cola: ")
        cola.agregar(valor)
    elif opcion == 2:
        cola.eliminar()
    elif opcion == 3:
        cola.mostrar_prox()
    elif opcion == 4:
        cola.mostrar()
    elif opcion == 5:
            break