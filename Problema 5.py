class Tabla_Multiplicar:
    def __init__(self, numero):
        self.numero = numero
        self.nombre_fichero = f"tabla-{numero}.txt"

    def guardar_tabla(self):
        try:
            with open(self.nombre_fichero, 'w') as archivo:
                for i in range(1, 11):
                    archivo.write(f"{self.numero} x {i} = {self.numero * i}\n")
            print(f"Tabla del {self.numero} guardada en {self.nombre_fichero}")
        except Exception as e:
            print(f"Error al escribir en el archivo: {e}")

    def mostrar_tabla(self):
        try:
            with open(self.nombre_fichero, 'r') as archivo:
                print(archivo.read())
        except FileNotFoundError:
            print(f"El archivo {self.nombre_fichero} no existe.")

    def mostrar_linea(self, linea):
        try:
            with open(self.nombre_fichero, 'r') as archivo:
                lineas = archivo.readlines()
                if 1 <= linea <= len(lineas):
                    print(lineas[linea - 1].strip())
                else:
                    print(f"La tabla tiene solo {len(lineas)} líneas.")
        except FileNotFoundError:
            print(f"El archivo {self.nombre_fichero} no existe.")


def menu():
    while True:
        print("\nMenú:")
        print("1. Guardar tabla de multiplicar")
        print("2. Leer y mostrar tabla de multiplicar")
        print("3. Leer y mostrar línea de una tabla de multiplicar")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            try:
                numero = int(input("Ingrese un número entre 1 y 10: "))
                if 1 <= numero <= 10:
                    tabla = Tabla_Multiplicar(numero)
                    tabla.guardar_tabla()
                else:
                    print("El número debe estar entre 1 y 10.")
            except ValueError:
                print("Debe ingresar un número entero.")

        elif opcion == '2':
            try:
                numero = int(input("Ingrese un número entre 1 y 10: "))
                if 1 <= numero <= 10:
                    tabla = Tabla_Multiplicar(numero)
                    tabla.mostrar_tabla()
                else:
                    print("El número debe estar entre 1 y 10.")
            except ValueError:
                print("Debe ingresar un número entero.")

        elif opcion == '3':
            try:
                numero = int(input("Ingrese un número entre 1 y 10: "))
                if 1 <= numero <= 10:
                    linea = int(input("Ingrese el número de la línea que desea ver (1-10): "))
                    if 1 <= linea <= 10:
                        tabla = Tabla_Multiplicar(numero)
                        tabla.mostrar_linea(linea)
                    else:
                        print("El número de línea debe estar entre 1 y 10.")
                else:
                    print("El número debe estar entre 1 y 10.")
            except ValueError:
                print("Debe ingresar números enteros.")

        elif opcion == '4':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida, por favor seleccione una opción entre 1 y 4.")


menu()
