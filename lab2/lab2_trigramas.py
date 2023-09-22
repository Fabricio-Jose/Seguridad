def quitar_acentos(cadena):
    acentuados = "áéíóúÁÉÍÓÚ"
    sin_acentos = "aeiouAEIOU"
    cadena_sin_acentos = cadena

    for i in range(len(cadena)):
        if cadena[i] in acentuados:
            indice = acentuados.index(cadena[i])
            cadena_sin_acentos = cadena_sin_acentos[:i] + sin_acentos[indice] + cadena_sin_acentos[i+1:]

    return cadena_sin_acentos

def encontrar_trigramas(texto):
    trigramas = {}  # Diccionario para almacenar trigramas y sus posiciones
    distancias = {}  # Diccionario para almacenar distancias entre trigramas

    for i in range(len(texto) - 2):
        trigrama = texto[i:i+3]  # Obtener el trigrama actual
        if trigrama in trigramas:
            # Si el trigrama ya ha sido visto, calcula la distancia
            distancia = i - trigramas[trigrama]
            if trigramas[trigrama] not in distancias:
                distancias[trigramas[trigrama]] = []  # Inicializar lista de distancias
            distancias[trigramas[trigrama]].append(distancia)
        else:
            # Si es la primera vez que se ve el trigrama, registra su posición
            trigramas[trigrama] = i

    return distancias

def main():
    input_file = "texto.txt"
    output_file = "HERALDOSNEGROS_pre.txt"

    with open(output_file, "w", encoding="utf-8") as archivo_salida:
        with open(input_file, "r", encoding="utf-8") as archivo_entrada:
            texto = archivo_entrada.read()  # Leer el texto completo

            # Ejercicio 1: Sustituir j>i, h>i, ñ>n, k>l, u>v, w>v, y>z
            texto = texto.replace('j', 'i').replace('h', 'i').replace('ñ', 'n').replace('k', 'l').replace('u', 'v').replace('w', 'v').replace('y', 'z')

            # Ejercicio 2: Eliminar las tildes
            texto = quitar_acentos(texto)

            # Ejercicio 3: Convertir todas las letras a mayúsculas
            texto = texto.upper()

            # Ejercicio 4: Eliminar espacios en blanco y signos de puntuación
            texto = ''.join(c for c in texto if not c.isspace() and not c in ".,;:")

            # Encontrar trigramas y distancias
            distancias = encontrar_trigramas(texto)

            # Escribir el resultado en el archivo de salida
            archivo_salida.write(texto + "\n")

            # Imprimir distancias entre trigramas
            print("Distancias entre trigramas:")
            for posicion, distancias_lista in distancias.items():
                trigrama = texto[posicion:posicion+3]
                print(f"{trigrama}: {', '.join(map(str, distancias_lista))}")

if __name__ == "__main__":
    main()