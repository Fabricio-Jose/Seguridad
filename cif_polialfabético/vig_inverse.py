alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '

def desencriptar_vigenere(texto_cifrado, clave):
    texto_claro = ''
    for i in range(len(texto_cifrado)):
        # Obtiene los índices en el alfabeto del caracter cifrado y del caracter de la clave
        indice_cifrado = alfabeto.index(texto_cifrado[i])
        indice_clave = alfabeto.index(clave[i % len(clave)])
        
        # Calcula el índice del caracter en claro y lo añade al resultado
        indice_claro = (indice_cifrado - indice_clave) % 27
        texto_claro += alfabeto[indice_claro]
        
    return texto_claro

texto_cifrado = 'IZLQOD'
clave = 'SOL'
texto_claro = desencriptar_vigenere(texto_cifrado, clave)

print(texto_claro) 