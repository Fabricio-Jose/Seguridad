from collections import Counter
import math
import string

alfabeto = string.ascii_uppercase + 'Ñ'
texto_cifrado = "MAXYHGAVAPUUGZHEGZQOWOBNIPQKRNNMEXIGONIICUCAWIGCTEAGMNOLRSZJNLWÑAWWIGLDDZSNIZDNBIXGZLAYMXNCVEKIETMOEOPBEWPTNIXCXUIHMECXLNOCECYXEÑQPBWUFANIICNJIKISCZUAILBGSOANKBFWUAYWNSCHLCWYDZHDZAQVMPTVGFGPVAJWFVPUOYMXCWERVLQCZWECIFVITUZSNCZUAIKBFMNALIEGLBSZLQUXNOHWOCGHNYWNQKDANZUDIFOIMXNPHNUWQOKLMVBNNKRMKONDPDPNMIKAWOXMEEIVEKGBGSFHVADWPGOYMHOIUEEIPGOLENZBSCHAGKQTZDRNMÑNWTUZIÑCMÑAXKQUWDLVANNIHLÑCQÑWGEHIPGZDTZTNNWÑEEWFUMGIÑXNTWXNVIXCZOAZSOQUVENDNFWUSZYHGLRACPGGUGIYWHOTRMZUGQQDDZIZFWHVVSHCUGOGIFKBXAXPBOBRDVDUCMVTKGIKDRSZLUQSDVPMXVIVEYMFGTEANIMQLHLGPQOHRYWCFEWFOISNNPUAYINNÑXNÑPGKWGOILQGAFOILQTAHEIIDWMNEÑXNEPRCVDQTURSK"

# Frecuencias de las letras en el español
frec_esp = {
    'E': 13.72, 'A': 12.53, 'O': 8.69, 'I': 6.25, 'S': 7.2, 'N': 6.71,
    'R': 6.87, 'U': 2.93, 'L': 4.97, 'T': 4.34, 'C': 4.63, 'D': 5.86,
    'M': 3.15, 'P': 2.51, 'Y': 1.09, 'F': 0.69, 'B': 1.49, 'V': 1.05,
    'G': 1.0, 'H': 1.18, 'Q': 0.88, 'Z': 0.47, 'J': 0.44, 'Ñ': 0.31,
    'X': 0.22, 'W': 0.01, 'K': 0.02
}

# Función para calcular el MCD de una lista de números
def mcd(lista):
    resultado = lista[0]
    for num in lista[1:]:
        resultado = math.gcd(resultado, num)
    return resultado

# 1. Buscar secuencias repetidas y calcular distancias
secuencias = {}
for i in range(len(texto_cifrado)):
    for j in range(3, 6):  # Longitud de las secuencias a buscar
        secuencia = texto_cifrado[i:i + j]
        if secuencia in secuencias:
            secuencias[secuencia].append(i - secuencias[secuencia][-1])
        else:
            secuencias[secuencia] = [i]

# Filtrar secuencias con una sola aparición
distancias = []
for sec, posiciones in secuencias.items():
    if len(posiciones) > 1:
        distancias.extend(posiciones[1:])

# 2. Calcular el MCD de las distancias
longitud_clave_probable = mcd(distancias)
print("Longitud probable de la clave:", longitud_clave_probable)

# 3. Análisis de frecuencia para deducir la clave
clave_probable = ""
for i in range(longitud_clave_probable):
    bloque = texto_cifrado[i::longitud_clave_probable]
    frecuencias = Counter(bloque)
    suma_shifts = 0
    for letra, frec in frecuencias.items():
        suma_shifts += frec * alfabeto.index(letra)
    shift = suma_shifts % 27
    clave_probable += alfabeto[shift]
print("Clave probable:", clave_probable)