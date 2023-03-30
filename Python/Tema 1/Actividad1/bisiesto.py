# Programa 1: Bisiesto
# Juan José Méndez Torrero 
# i42metoj@uco.es

import sys

if __name__ == "__main__":

    # Comprobamos que sólo se pase un argumento
    if len(sys.argv) == 2:

        # Comprobamos que ese argumento es un número
        if sys.argv[1].isnumeric():

            # Recogemos el valor del argumento y lo convertimos a entero
            year = int(sys.argv[1])

            # Si es divisible entre 4, 100 o 400, es bisiesto
            print(True) if not year % 4 and (year % 100 or  not year % 400) else print(False)

        else:

            print("Error: El argumento pasado no es un número")
            sys.exit()
    else:

        print("Error: Los argumentos pasados no son correctos:\n python bisiesto.py [año]")
        sys.exit()