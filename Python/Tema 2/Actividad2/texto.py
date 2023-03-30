from collections import Counter
from collections import defaultdict
import collections
import re


class Texto:
    def __init__(self, texto) -> None:
        self.texto = texto

        self.palabras = re.split(
            "[;,.\ ]", self.texto.replace("\n", "").replace(":", "").strip()
        )

        # Eliminamos todos los espacios vacios
        self.palabras = list(filter(("").__ne__, self.palabras))

        self.palabra_long = defaultdict(str)

    def numero_palabras(self):

        # Dividimos las palabras por separadores
        return sum(Counter(self.palabras).values())

    def numero_palabras_may_min(self):

        min_may_dict = defaultdict(str)

        min_may_dict["minusculas"] = 0
        min_may_dict["primera_mayuscula"] = 0
        min_may_dict["mayusculas"] = 0

        for palabra in self.palabras:
            if palabra.isupper():
                min_may_dict["mayusculas"] += 1
            if palabra.islower():
                min_may_dict["minusculas"] += 1
            else:
                min_may_dict["primera_mayuscula"] += 1

        return min_may_dict

    def palabras_por_tamanio(self):

        for palabra in self.palabras:

            if len(palabra) not in self.palabra_long.keys():
                self.palabra_long[len(palabra)] = 1

            elif len(palabra) in self.palabra_long.keys():
                self.palabra_long[len(palabra)] += 1

        self.palabra_long = collections.OrderedDict(sorted(self.palabra_long.items()))

        return self.palabra_long

    def total(self):

        freq = defaultdict(int)

        for val, key in self.palabra_long.items():
            freq[key] = val / len(self.palabras)

        return freq

    def dividido(self, divisor):

        freq = defaultdict(int)

        for key, val in Counter(self.palabras).items():
            freq[key] = val / len(self.palabras)

        return freq[divisor]

    def num_palabra_frase(self):

        total_frases = defaultdict(str)

        frases = re.split("[.]", self.texto.replace("\n", "").strip())

        for fra in frases:

            total_frases[fra] = len(
                list(
                    filter(
                        ("").__ne__,
                        re.split(
                            "[;,.\ ]", fra.replace("\n", "").replace(":", "").strip()
                        ),
                    )
                )
            )

        return total_frases
