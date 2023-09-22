def frecuencias(texto):
    contador_letras = {}

    # Recorrer el texto y contar las letras
    for letra in texto:
        if letra.isalpha():  # Verificar si es una letra
            letra = letra.upper()  # Convertir a mayúscula
            if letra in contador_letras:
                contador_letras[letra] += 1
            else:
                contador_letras[letra] = 1

    return contador_letras

def quitar_acentos(cadena):
    acentuados = "áéíóúÁÉÍÓÚ"
    sin_acentos = "aeiouAEIOU"
    cadena_sin_acentos = cadena

    for i in range(len(cadena)):
        if cadena[i] in acentuados:
            indice = acentuados.index(cadena[i])
            cadena_sin_acentos = cadena_sin_acentos[:i] + sin_acentos[indice] + cadena_sin_acentos[i+1:]

    return cadena_sin_acentos

def reemplazar_unicode8230(cadena):
    # Crear un diccionario de reemplazo UNICODE-8230
    reemplazo_unicode8230 = {
        'A': '\u2022', 'B': '\u2020', 'C': '\u2021', 'E': '\u2026',
        'H': '\u2030', 'I': '\u2032', 'J': '\u2033', 'K': '\u2035',
        'M': '\u203B', 'O': '\u203E', 'P': '\u203F', 'T': '\u2044',
        'X': '\u204A', 'Y': '\u204E',
    }

    # Realizar el reemplazo UNICODE-8230
    for letra, reemplazo in reemplazo_unicode8230.items():
        cadena = cadena.replace(letra, reemplazo)

    return cadena

def main():
    input_file = "texto.txt"
    output_file = "HERALDOSNEGROS_pre.txt"

    with open(output_file, "w", encoding="utf-8") as archivo_salida:
        with open(input_file, "r", encoding="utf-8") as archivo_entrada:
            for linea in archivo_entrada:
                # Ejercicio 1: Sustituir j>i, h>i, ñ>n, k>l, u>v, w>v, y>z
                linea = linea.replace('j', 'i').replace('h', 'i').replace('ñ', 'n').replace('k', 'l').replace('u', 'v').replace('w', 'v').replace('y', 'z')

                # Ejercicio 2: Eliminar las tildes
                linea = quitar_acentos(linea)

                # Ejercicio 3: Convertir todas las letras a mayúsculas
                linea = linea.upper()

                # Ejercicio 4: Eliminar espacios en blanco y signos de puntuación
                linea = ''.join(c for c in linea if not c.isspace() and not c in ".,;:")

                # Ejercicio 5: Reemplazar según UNICODE-8230
                linea = reemplazar_unicode8230(linea)

                # Escribir la línea resultante en el archivo de salida
                archivo_salida.write(linea)

            archivo_salida.write("\n")  # Agregar un salto de línea al final del archivo

            # Obtener el diccionario de conteo de letras
            conteo_letras = frecuencias(linea)

            # Imprimir el diccionario de conteo de letras
            print("Conteo de letras:")
            for letra, cantidad in conteo_letras.items():
                print(f"{letra}: {cantidad}")

            letras_mas_comunes = sorted(conteo_letras.items(), key=lambda x: x[1], reverse=True)[:5]

            # Imprimir las 5 letras más comunes
            print("Las 5 letras más comunes:")
            for letra, cantidad in letras_mas_comunes:
                print(f"{letra}: {cantidad}")

if __name__ == "__main__":
    main()