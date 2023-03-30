# Programa 2: Similares
# Juan José Méndez Torrero 
# i42metoj@uco.es

import sys
import re

def is_fraction(fraction):

    return True if re.search("\d*/\d*", fraction) else False


if __name__ == "__main__":

    # Comprobamos que sólo se pase un argumento
    if len(sys.argv) == 4:

        frac_1 = sys.argv[1]

        frac_2 = sys.argv[2]

        operation = int(sys.argv[3])

        if is_fraction(frac_1) and is_fraction(frac_2) and operation in [1,2,3,4]:

            # Suma
            if operation == 1:

                denom_1 = frac_1.split("/")[1]

                denom_2 = frac_2.split("/")[1]

                if denom_1 != denom_2:

                    print("Error: Los denominadores han de ser iguales")

                    sys.exit()
                
                numerator = float(frac_1.split("/")[0]) + float(frac_2.split("/")[0])

                print("{0}/{1}".format(str(numerator), denom_1))
            
            # Resta
            elif operation == 2:
                denom_1 = frac_1.split("/")[1]

                denom_2 = frac_2.split("/")[1]

                if denom_1 != denom_2:

                    print("Error: Los denominadores han de ser iguales")

                    sys.exit()
                
                numerator = int(frac_1.split("/")[0]) - int(frac_2.split("/")[0])

                print("{0}/{1}".format(str(numerator), denom_1))

            # Multiplication
            elif operation == 3:

                denominator = int(frac_1.split("/")[1]) * int(frac_2.split("/")[1])
                
                numerator = int(frac_1.split("/")[0]) * int(frac_2.split("/")[0])

                print("{0}/{1}".format(str(numerator), denominator))

            # Division
            elif operation == 4:

                denominator = int(frac_1.split("/")[1]) * int(frac_2.split("/")[0])
                
                numerator = int(frac_1.split("/")[0]) * int(frac_2.split("/")[1])

                print("{0}/{1}".format(str(numerator), denominator))
        
        else:
            print("Error: Los argumentos pasados no son fracciones del tipo num/den")
            sys.exit()

    else:

        print("Error: Los argumentos pasados no son correctos:\n python fracciones.py [fracción1] [fracción2] [operacion]")
        sys.exit()