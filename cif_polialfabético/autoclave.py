alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def cifrar_autoclave(texto_claro, clave):
    texto_cifrado = []
    # Inicia con la clave y luego se extenderá con el propio mensaje en claro.
    clave_extendida = clave
    
    for i in range(len(texto_claro)):
        # Si hemos llegado al final de la clave_extendida, añadimos caracteres del texto_claro a la clave_extendida
        if i >= len(clave_extendida):
            clave_extendida += texto_claro[i]
        
        # Encuentra los índices de los caracteres en el alfabeto y los suma, modulo la longitud del alfabeto
        indice_texto_claro = alfabeto.index(texto_claro[i])
        indice_clave_extendida = alfabeto.index(clave_extendida[i])
        
        indice_cifrado = (indice_texto_claro + indice_clave_extendida) % 26
        texto_cifrado.append(alfabeto[indice_cifrado])
        
    return ''.join(texto_cifrado)

texto_claro = 'HABIAUNAVEZ'
clave = 'CIRCO'
texto_cifrado = cifrar_autoclave(texto_claro, clave)

print(texto_cifrado)  # Debería imprimir: LOGOCFTKG