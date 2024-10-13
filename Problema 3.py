import requests
import shutil
import zipfile
import os


url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

image_name = "imagen_descargada.jpg"

response = requests.get(url, stream=True)
if response.status_code == 200:
    with open(image_name, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    print(f"Imagen descargada y guardada como {image_name}")
else:
    print("No se pudo descargar la imagen.")
del response

zip_name = "imagen_comprimida.zip"
with zipfile.ZipFile(zip_name, 'w') as zip_file:
    zip_file.write(image_name)
    print(f"Imagen comprimida en el archivo {zip_name}")

with zipfile.ZipFile(zip_name, 'r') as zip_file:
    zip_file.extractall("imagen_descomprimida")
    print(f"Imagen descomprimida en la carpeta 'imagen_descomprimida'")
