# Convert images to webp

# Importo la utilidad "Image" del administrador de paquetes "PIL"
from PIL import Image
# Importo os para convertir todas las imagenes
import os

# Creo la función para convertir de a uno los archivos que se encuentran en la carpeta "/images"
def convert_to_webp(fileName, path="images/"):

    # Extraigo el tipo de extensión
    extension = fileName.split('.')[-1]
    print('Extrayendo el tipo de extensión...')

    # Extraigo el nombre del archivo SIN la extensión
    fName = fileName.split('.')[0]

    # Abro la imagen con la utilidad de PIL
    img = Image.open(path + fileName)


    # Si la extensión es ".png"
    if extension == "png":
        # Guardo el archivo con su nombre, el tipo de archivo ".webp" y "lossless=True" debido al tipo de archivo ".png"
        img.save((path+fName+".webp"), "webp", lossless=True)
        print('Tipo de extensión: .png')

    # Si la extensión es ".jpg" o ".jpeg"
    elif extension == "jpg" or extension == "jpeg":
        # Guardo el archivo con su nombre, el tipo de archivo ".webp", y la calidad de reducción en 85%
        img.save((path+fName+".webp"), "webp", quality=85)
        print('Tipo de extensión: .jpg')

# Creo la función para convertir todas las imagenes que se encuentran en la carpeta "/images"
def convert_all (path="images/"):
    # Realizo un ciclo para seleccionar las imagenes que estan en esa carpeta
    for root, dirs, files in os.walk(path):
        for imageFile in files:
            if imageFile.endswith(".png") or imageFile.endswith(".jpg") or imageFile.endswith(".jpeg"):
                convert_to_webp(imageFile, root)
                print("Convirtiendo: " + imageFile)
                print('Conversión realizada correctamente.')


# Propiedades de PIL para ejecutar el código
if __name__ == "__main__":
    convert_all()