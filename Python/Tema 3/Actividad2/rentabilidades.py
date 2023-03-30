# Juan José Méndez Torrero i42metoj@uco.es
# Importamos las librerias necesarias
import os
import sys
import zipfile
import xml.sax
import pandas as pd
import numpy as np
import datetime

# Creamos la clase que se encargará de leer el fichero odt
class ODTContentHandler(xml.sax.ContentHandler):
    """
    Reads content.xml from the odt and extracts all the text inside text:p
    tags"""

    def __init__(self):
        self._buffer = ""
        self._paragraphCount = 0

    def startElement(self, name, attrs):
        if name == "text:p":
            self._paragraphCount += 1
        if name == "text:h":
            self._paragraphCount += 1
            self._buffer += "^"

    def characters(self, ch):
        if self._paragraphCount > 0:
            self._buffer += ch

    def endElement(self, name):
        if name == "text:p":
            self._paragraphCount -= 1
            self._buffer += "\n"
        if name == "text:h":
            self._paragraphCount -= 1
            self._buffer += "^"
            self._buffer += "\n"


# Comprobamos los valores pasados por agumentos
if len(sys.argv) != 2:
    print("Error en los argumentos.")
    print("python imagen.py ruta_carpeta")
    sys.exit()

path_to_folder = sys.argv[1]

final_data = pd.DataFrame()

# Recorremos el path introducido
for path, _, files in os.walk(path_to_folder):

    for fi in files:

        # Detectamos si el fichero termina con la extension odt
        if fi.endswith(".odt"):

            # Descomprimos el fichero odt
            myfile = zipfile.ZipFile(path + "/" + fi)

            # Leemos el contenido xml
            data = myfile.open("content.xml").read()

            # Creamos los objetos parser y handler para desencriptar el fichero xml
            parser = xml.sax.make_parser()
            handler = ODTContentHandler()
            parser.setContentHandler(handler)
            parser.parse(myfile.open("content.xml"))
            data = handler._buffer.encode("ascii", "replace")

            # Eliminamos posibles saltos de linea
            data = str(data).split("\\n\\n")

            for dt in data:
                
                if "Fecha de cierre" in dt:

                    # Recogemos el resultado
                    resultado = int(dt.split("? ")[0].split(" ")[-1])

                    # Recogemos la fecha de cierre
                    fecha_cierre = dt.split("? ")[1].split(" ")[-1]

                    # Calculamos el numero de dias desde la fecha inicio a la fecha de cierre
                    num_dias = datetime.datetime.strptime(fecha_cierre, '%Y-%m-%d') - datetime.datetime.strptime("2017-01-01", '%Y-%m-%d')

                    # Calculamos el tir en porcetage
                    tir = (np.power((resultado/10000), (365.25/num_dias.days)) - 1) * 100

                    # Guardamos todo en un pandas Series
                    data_ser = pd.Series([fi, resultado, fecha_cierre, num_dias.days, tir])

                    # Añadimos la fila al data frame final
                    final_data = final_data.append(data_ser, ignore_index=True)

# Cambiamos el nombre de las columnas del DF
final_data.columns = ["nombre_fichero", "resultado", "fecha_cierre", "duracion_dias", "tir"]

# Abrimos el fichero en modo lectura
f = open(path_to_folder + ".csv", "w")

# Escribimos en el fichero cada una de las lineas del DF separadas por comas
for index, row in final_data.iterrows():

    f.write(",".join([str(x) for x in row.values]))
    f.write("\n")

# Añadimos una fila en blanco
f.write("\n")

# Escribimos la rentabilidad media
f.write("Rentabilidad media: " + str(np.mean(final_data["tir"])))

# Cerramos el fichero
f.close()
