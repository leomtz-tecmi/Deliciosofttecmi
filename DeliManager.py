import os
import json
import sys

mesas_reservadas = []

def MenuManager():
    #Maneja la interfaz del menu
    while True:
        print("\n===== Menú Principal Deliciosoft =====")
        print("1. Anadir reservacion")
        print("2. Mostrar mesas reservadas")
        print("3. Eliminar Reservacion")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            AddTableRes()
        elif opcion == "2":
            ShowTableRes()
        elif opcion == "3":
            DeleteTableRes()
        elif opcion == "4":
            print("Saliendo del programa...")
            sys.exit(0)
        else:
            print("Opción no válida. Intente de nuevo.")

def DeleteTableRes():
    #Elimina una reservacion
    mesa_eliminar = input("\nSeleccione la mesa a eliminar:")
    ShowTableRes()
    del mesas_reservadas[mesa_eliminar]

    print("Se ha eliminado la reservacion")

def ShowTableRes():
    #Muestra las mesas actualmente reservadas
    print(f"Estas son las mesas reservadas:\n {mesas_reservadas}")

def AddTableRes():
    #Se anade una reservacion a una mesa, posteriormente esa mesa se marca como ocupada.
    with open('restaurantinfo.txt', 'r') as archivo:
        datos = json.load(archivo)
        mesas_max = datos["mesas"]
    
    info_reserva = input("A que hora y mesa es la reservacion?")

    if mesas_reservadas.len > mesas_max:
        print("Lo siento, ya no hay mas mesas disponibles")
    else:
        mesas_reservadas.append(info_reserva)
        return

def CreateRestaurant():
    #Se crea el perfil del restaurante; nombre, mesas y capacidad maxima.
    nombre_rest = input("Como se llama tu restaurante?")
    mesas = input("Cuantas Mesas hay en el restaurante? Considerando una mesa = 4 asientos")

    datos_rest = {
        "nombre" : nombre_rest,
        "mesas" : int(mesas)
    }
#Se guarda en un archivo .txt en formato json.
    with open('restaurantinfo.txt', 'w') as text_file:  
        json.dump(datos_rest, text_file, indent=4)

def FirstTimeCheck():
    #Revisa si hay un archivo de restaurante con informacion, solo corre en usuarios nuevos.
    archivo = 'restaurantinfo.txt'
    
    if os.path.getsize(archivo) == 0:
        CreateRestaurant()

    else:
        MenuManager()