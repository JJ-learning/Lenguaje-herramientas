import sys

if __name__ == "__main__":

    message = sys.argv[1].upper().replace(" ", "*")

    type_cypher = sys.argv[2]

    # Cifrado cesar
    if len(sys.argv) == 4:

        table_cesar = {
                "*": 0,
                "A": 1,
                "B": 2,
                "C": 3,
                "D": 4,
                "E": 5,
                "F": 6,
                "G": 7,
                "H": 8,
                "I": 9,
                "J": 10,
                "K": 11,
                "L": 12,
                "M": 13,
                "N": 14,
                "O": 15,
                "P": 16,
                "Q": 17,
                "R": 18,
                "S": 19,
                "T": 20,
                "U": 21,
                "V": 22,
                "W": 23,
                "X": 24,
                "Y": 25,
                "Z": 26,
                "(": 27,
                ")": 28,
                ",": 29,
                "?": 30,
                "!": 31
            } 

        private_key = int(sys.argv[3])

        new_message=""

        # Reemplazar caracter no conocido por *
        for letter in message:

            if letter not in table_cesar.keys():
                new_message += "*"
            
            else:
                new_message += letter

        # Cifrar
        if type_cypher == "c":

            message_cypher = ""

            for letter in new_message:

                new_letter = (table_cesar[letter] + private_key) % 32

                for key in table_cesar.keys():

                    if new_letter == table_cesar[key]:

                        message_cypher += key

            print(message_cypher)

        # Descifrar
        elif type_cypher == "d":

            message_decypher = ""

            for letter in message:

                value = table_cesar[letter] - private_key

                if value >= 0:
                    new_letter = value % 32
                
                else:
                    new_letter = value + 32
                
                for key in table_cesar.keys():

                    if new_letter == table_cesar[key]:

                        message_decypher += key

            print(message_decypher)

    # Cifrado diccionario
    elif len(sys.argv) == 3:
        table_dict = {
            "*": "J",
            "A": "B",
            "B": "S",
            "C": "Y",
            "D": "K",
            "E": "A",
            "F": "R",
            "G": "M",
            "H": "C",
            "I": "W",
            "J": "E",
            "K": "*",
            "L": "(",
            "M": "?",
            "N": "Z",
            "O": "Q",
            "P": "!",
            "Q": "X",
            "R": ")",
            "S": "V",
            "T": ",",
            "U": "H",
            "V": "F",
            "W": "D",
            "X": "U",
            "Y": "P",
            "Z": "T",
            "(": "O",
            ")": "N",
            ",": "G",
            "?": "L",
            "!": "I"
        } 
        
        new_message=""

        # Reemplazar caracter no conocido por *
        for letter in message:

            if letter not in table_dict.keys():
                new_message += "*"
            
            else:
                new_message += letter

        # Cifrar
        if type_cypher == "c":

            message_cypher = ""

            for letter in new_message:

                message_cypher += table_dict[letter]

            print(message_cypher)

        # Descifrar
        elif type_cypher == "d":
            
            # Invertimos el diccionario
            table_dict_inverted =  {y: x for x, y in table_dict.items()}

            message_decypher = ""

            for letter in new_message:

                message_decypher += table_dict_inverted[letter]

            print(message_decypher)
    
    else:
        print("Error en los argumentos de entrada")