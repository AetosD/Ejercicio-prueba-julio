from datetime import datetime


class Libro:
    codigo = ''
    titulo = ''
    autor = ''
    precio = 0
    pais = ''
    categoria = ''
    a_public = 0

    def __init__(self):
        self.codigo = 'AAA-000'
        self.titulo = 'S/T'
        self.autor = 'S/A'
        self.precio = 0
        self.pais = 'S/P'
        self.categoria = 'S/C'
        self.a_public = 0

    def setcodigo(self, codigo):
        if codigo[0:3].isalpha() and codigo[3:4] == '-' and codigo[4:7].isdigit():
            self.codigo = codigo
            return True
        else:
            print("Formato de codigo incorrecto")
            return False

    def setprecio(self, precio):
        if 10000 <= precio <= 150000:
            self.precio = precio
            return True
        else:
            print("El valor ingresado no es valido")
            return False

    def setcategoria(self, op_cat):
        match op_cat:
            case 1:
                self.categoria = "Fantasía"
                return True
            case 2:
                self.categoria = "Acción"
                return True
            case 3:
                self.categoria = "Novela"
                return True
            case 4:
                self.categoria = "Ficción"
                return True
            case _:
                print("Opcion invalida")
                return False

    def seta_public(self, fecha):
        if 1780 <= fecha <= datetime.now().year:
            self.a_public = fecha
            return True
        else:
            print("La fecha ingresada no es valida")
            return False
