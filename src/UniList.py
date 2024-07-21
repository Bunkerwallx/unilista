#!/usr/bin/env python



# src/UniList.py

def leer_lista(archivo):
    with open(archivo, 'r') as file:
        return file.read().splitlines()

def unir_listas(*listas):
    return ["".join(elementos) for elementos in zip(*listas)]

def guardar_lista(archivo, lista):
    with open(archivo, 'w') as file:
        for item in lista:
            file.write(f"{item}\n")

def main():
    # Solicitar el número de listas a unir
    num_listas = int(input("Ingrese el número de listas a unir (máximo 5): "))
    
    # Verificar que el número de listas sea válido
    if num_listas < 1 or num_listas > 5:
        print("Número inválido. Debe ingresar un número entre 1 y 5.")
        return

    # Leer las listas desde los archivos especificados
    listas = []
    for i in range(1, num_listas + 1):
        archivo = input(f"Ingrese el nombre del archivo para la lista {i} (por ejemplo, 'data/list1.txt'): ")
        listas.append(leer_lista(archivo))
    
    # Unir las listas
    lista_unida = unir_listas(*listas)
    
    # Guardar la lista unida en un archivo
    guardar_lista('data/lista_unida.txt', lista_unida)
    
    # Mostrar la lista unida
    print("Lista unida:", lista_unida)

if __name__ == "__main__":
    main()
