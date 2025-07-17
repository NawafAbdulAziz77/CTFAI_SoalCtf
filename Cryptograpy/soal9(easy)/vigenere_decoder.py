def vigenere_decrypt(ciphertext, key):
    decrypted_text = ""
    key_length = len(key)
    key = key.lower()
    key_index = 0  # index terpisah hanya untuk huruf

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % key_length]) - ord('a')
            base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            decrypted_text += decrypted_char
            key_index += 1  # geser hanya jika char alphabet
        else:
            decrypted_text += char

    return decrypted_text


# Contoh penggunaan
ciphertext = "Rijvs Uyqvo"
key = "CTF"
plaintext = vigenere_decrypt(ciphertext, key)
print("Decrypted Text:", plaintext)
