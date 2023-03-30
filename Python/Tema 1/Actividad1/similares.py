# Programa 2: Similares
# Juan José Méndez Torrero 
# i42metoj@uco.es

import sys

if __name__ == "__main__":

    # Comprobamos que sólo se pase un argumento
    if len(sys.argv) == 3:

        # Recogemos el primer argumento
        right_str = sys.argv[1]

        # Recogemos el segundo argumento
        left_str = sys.argv[2]

        # Comprobamos, en minúscula, si son iguales, al no se caseSensitive
        print("Iguales") if right_str.lower() == left_str.lower() else print("Diferentes")
    
    else:

        print("Error: Los argumentos pasados no son correctos:\n python similares.py [palabra1] [palabra2]")
        sys.exit()