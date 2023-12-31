from Libro import *
import numpy as np
import random as rn
libro = Libro()
arreglo_libro = np.array([])
num_random = rn
com = True


def ingresolibro(libros):
    c = False
    while not c:
        try:
            c = libro.setcodigo(input("Ingrese el codigo del libro (ej. AAA-000): "))
        except BaseException as error_cod:
            print(f"Error: {error_cod}")
    libro.titulo = input("Ingrese el titulo del libro: ")
    libro.autor = input("Ingrese el nombre del autor: ")
    c = False
    while not c:
        try:
            c = libro.setprecio(int(input("Ingrese el precio del libro (entre 10000 - 150000): ")))
        except BaseException as error_pre:
            print(f"Error: {error_pre}")
    libro.pais = input("Ingrese país del libro: ")
    c = False
    while not c:
        print("Categoría")
        print("1) Fantasía")
        print("2) Acción")
        print("3) Novela")
        print("4) Ficcción")
        try:
            c = libro.setcategoria(int(input("Ingrese una opcion (1-4): ")))
        except BaseException as error_cat:
            print(f"Error: {error_cat}")
    c = False
    while not c:
        try:
            c = libro.seta_public(int(input("Ingrese año de publicación (no puede ser antes de 1780): ")))
        except BaseException as error_pub:
            print(f"Error: {error_pub}")
    return np.append(libros, libro)


def buscarlibro(buscar):
    c = False
    while not c:
        codigo = input("Ingrese el codigo del libro: ")
        for buscar_libro in buscar:
            if codigo == buscar_libro.codigo:
                print(f"Codigo:\t\t{libro.codigo}")
                print(f"Titulo:\t\t{libro.titulo}")
                print(f"Autor:\t\t{libro.autor}")
                print(f"Precio:\t\t{libro.precio}")
                print(f"País:\t\t{libro.pais}")
                print(f"Categoría:\t\t{libro.categoria}")
                print(f"Año de Publicación:\t{libro.a_public}")
                c = True
                break
            else:
                print("El codigo no se encuentra")


def buscarcategoria(cat):
    categoria = ''
    c_cat = False
    while not c_cat:
        print("Categoría")
        print("1) Fantasía")
        print("2) Acción")
        print("3) Novela")
        print("4) Ficcción")
        try:
            op_cat = int(input("Ingrese categoria (1-4): "))
            match op_cat:
                case 1:
                    categoria = "Fantasía"
                case 2:
                    categoria = "Acción"
                case 3:
                    categoria = "Novela"
                case 4:
                    categoria = "Ficción"
                case _:
                    print("Opcion invalida")
            for lib in cat:
                if categoria == lib.categoria:
                    print(f"Codigo:\t\t\t{libro.codigo}")
                    print(f"Titulo:\t\t\t{libro.titulo}")
                    print(f"Autor:\t\t\t{libro.autor}")
                    print(f"Precio:\t\t\t{libro.precio}")
                    print(f"País:\t\t\t{libro.pais}")
                    print(f"Categoría:\t\t\t{libro.categoria}")
                    print(f"Año de Publicación:\t{libro.a_public}")
                    c_cat = True
        except BaseException as error_cat:
            print(f"Error: {error_cat}")


##def imprimirinforme(arreglo_libro):


def salir():
    print("Cerrando sistema")
    print("Desarrollado por Darío Osorio")
    print("Version 1.2.0")
    return False


while com:
    print("Bienvenido al Sistema de registros de Libreria Mayor")
    print("1) Grabar")
    print("2) Buscar Libro")
    print("3) Imprimir Informe")
    print("4) Salir")
    try:
        op = int(input("Seleccione una opcion (1-4): "))
        match op:
            case 1:
                arreglo_libro = ingresolibro(arreglo_libro)
            case 2:
                buscarlibro(arreglo_libro)
            case 3:
                print("1")
            case 4:
                com = salir()
            case _:
                print("Opcion invalida")
    except BaseException as error:
        print(f"Error: {error}")
