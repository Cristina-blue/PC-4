def contar_lineas_codigo(ruta_archivo):
    try:
        
        if not ruta_archivo.endswith('.py'):
            print("El archivo no tiene la extensión .py.")
            return

      
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()

        
        lineas_codigo = [linea for linea in lineas if linea.strip() and not linea.strip().startswith('#')]

     
        print(f"Número de líneas de código: {len(lineas_codigo)}")

    except FileNotFoundError:
        print("El archivo no existe o la ruta es inválida.")

ruta = input("Ingrese la ruta del archivo .py: ")
contar_lineas_codigo(ruta)
