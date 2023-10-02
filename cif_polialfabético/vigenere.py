def mod27_vigenere_encrypt(plain_text, key):
    # Definimos el alfabeto a utilizar, incluyendo el espacio
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
    encrypted_text = []
    
    # Aseguramos que tanto el texto como la clave solo contengan caracteres válidos
    plain_text = plain_text.upper()
    key = key.upper()
    
    key_index = 0
    for char in plain_text:
        # Verificamos si el caracter está en nuestro alfabeto
        if char in alphabet:
            # Calculamos el índice del nuevo caracter cifrado
            text_index = alphabet.index(char)
            key_index_mod = alphabet.index(key[key_index % len(key)])
            encrypted_index = (text_index + key_index_mod) % 27
            
            encrypted_text.append(alphabet[encrypted_index])
            
            key_index += 1  # Avanzamos al siguiente caracter de la clave
        else:
            # Si el caracter no está en nuestro alfabeto, lo añadimos tal cual
            encrypted_text.append(char)
    
    return ''.join(encrypted_text)


def main():
    print("Cifrador de Vigenere modulo 27 (A-Z + espacio)")
    plain_text = input("Introduce el texto a cifrar: ")
    key = input("Introduce la clave: ")
    
    if not key or not all(char.isalpha() or char.isspace() for char in key):
        print("La clave no puede estar vacía y solo puede contener letras y espacios")
        return
    
    encrypted_text = mod27_vigenere_encrypt(plain_text, key)
    print("Texto cifrado: ", encrypted_text)


if __name__ == "__main__":
    main()