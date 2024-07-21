#!/usr/bin/env python



def leer_lista(archivo):
    with open(archivo, 'r') as file:
        return file.read().splitlines()

def unir_listas(lista1, lista2):
    return [nombre + apellido for nombre, apellido in zip(lista1, lista2)]

def guardar_lista(archivo, lista):
    with open(archivo, 'w') as file:
        for item in lista:
            file.write(f"{item}\n")

def main():
    # Leer las listas desde los archivos
    lista1 = leer_lista('../data/list1.txt')
    lista2 = leer_lista('../data/list2.txt')
    
    # Unir las listas
    lista_unida = unir_listas(lista1, lista2)
    
    # Guardar la lista unida en un archivo
    guardar_lista('../data/lista_unida.txt', lista_unida)
    
    # Mostrar la lista unida
    print("Lista unida:", lista_unida)

if __name__ == "__main__":
    main()
