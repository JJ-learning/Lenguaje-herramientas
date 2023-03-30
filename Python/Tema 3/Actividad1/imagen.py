# Importamos la librería matplotlib para poder visualizar las imagenes finales
# pip install matplotlib
import sys


class Imagen:

    def __init__(self, path_to_image):

        # Guardamos la ruta a la imagen inicial
        self.path_to_image = path_to_image

        # Creamos las variables necesarias para la clase imagen
        self.header = None
        self.height = None
        self.width = None
        self.depth = None
        self.image = None
        self.negative_image = None
        self.horizontal_image = None

        # LLamamos a la funcion para leer la imagen
        self.read_image_pmg()
        self.get_horizontal_image()
        self.get_negative_image()

    def read_image_pmg(self):

        # Leemos el fichero en formato binario
        file = open(self.path_to_image, 'rb')

        # Almacenamos la cabecera en una variable de clase leyendo
        # la primera linea
        self.header = file.readline()

        # Almacenamos, leyendo la segundo linea, el numero de columnas y filas
        (self.width, self.height) = [i for i in file.readline().split()]

        # Almacenamos, leyenedo la tercera linea, el mayor nivel de gris posible
        self.depth = file.readline()

        # Creamos una lista vacia para almacenar la imagen
        image = []

        for f in range(int(self.height)):

            row = []

            for c in range(int(self.width)):

                # Utilizamos la funcion ord para decodificar el caracer binario
                row.append(ord(file.read(1)))

            image.append(row)

        file.close()

        # Almacenamos la variable de la función en la variable de clase
        self.image = image

    def save_image(self, type_image):

        try:
            image = self.negative_image if type_image == "n" else self.horizontal_image

            extension_name = "_negativo" if type_image == "n" else "_espejo"

            file = open(self.path_to_image.replace(
                ".pgm", extension_name+".pgm"), "wb")

            file.write(self.header)

            file.write(self.width + b" " + self.height + b"\n")

            file.write(self.depth)

            for f in range(int(self.height)):
                file.write(bytearray(image[f]))

            file.close()

        except:
            print("Error al salvar el fichero")

    def get_negative_image(self):
        image = []

        for f in range(int(self.height)):

            row = []

            for c in range(int(self.width)):

                # Restamos al nivel de gris, el valor del pixel, así, conseguiremos la imagen en negativo
                row.append(int(self.depth) - self.image[f][c])

            image.append(row)

        # Almacenamos la variable de la función en la variable de clase
        self.negative_image = image

    def get_horizontal_image(self):
        image = []

        for f in range(int(self.height)):
            row = []

            for c in range(int(self.width)):

                # Para conseguir la imagen invertida, bastaría con restar a la columna el total de columnas
                # Así, almacenaremos la imagen de manera invertida horizontalmente
                row.append(self.image[f][(int(self.width)-1)-c])

            image.append(row)

        # Almacenamos la variable de la función en la variable de clase
        self.horizontal_image = image


if len(sys.argv) != 3:
    print("Error en los argumentos.")
    print("python imagen.py ruta [n|h]")
    sys.exit()

path_to_file = sys.argv[1]
type_operation = sys.argv[2]

if type_operation != "n" and type_operation != "h":
    print("Error en los argumentos.")
    print("python imagen.py ruta [h(horizontal)|n(negative)]")
    sys.exit()

# Creamos el objeto imagen
imagen = Imagen(path_to_file)

# Guardamos la imagen a introducir
imagen.save_image(type_operation)
