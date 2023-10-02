# Definir la clave y el texto
#clave = "ELINGENIOSOHIDALGO"
clave = 'POSITIVO'
#texto_claro = """En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un
#hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor. Una olla de algo más vaca que carnero, salpicón las más noches, duelos y quebrantos los sábados, lentejas los viernes, algún palomino de añadidura los domingos, consumían las tres partes de su hacienda. El resto della concluían sayo de velarte, calzas de velludo para las fiestas con sus pantuflos de lo mismo, los días de entre semana se honraba con su vellori de lo más fino. Tenía en su casa una ama que pasaba de los cuarenta, y una sobrina que no llegaba a los veinte, y un mozo de campo y plaza, que así ensillaba el rocín como tomaba la podadera."""
texto_claro = 'Creer que es posible es el paso número uno hacia el  éxito. Despertarse y pensar en algo positivo puede cambiar el transcurso de todo el día. No eres lo suficientemente viejo como para no iniciar un nuevo camino hacia tus sueños. Levántate cada mañana creyendo que vas a vivir el mejor día de tu vida'
# Función para cifrar con Vigenere mod 191
def cifrar_vigenere(texto, clave):
    texto_cifrado = []
    len_clave = len(clave)
    for i, char in enumerate(texto):
        # Obtiene los valores ASCII de los caracteres del texto y de la clave
        ascii_texto = ord(char)
        ascii_clave = ord(clave[i % len_clave])
        #print(i)
        #print(ascii_texto)
        #print(ascii_clave)
        #print('--------------------------------')

        # Cifra en modulo 191
        ascii_cifrado = (ascii_texto + ascii_clave) % 191
        texto_cifrado.append(chr(ascii_cifrado))
    return ''.join(texto_cifrado)

# Cifrar el texto
texto_cifrado = cifrar_vigenere(texto_claro, clave)
print(texto_cifrado)