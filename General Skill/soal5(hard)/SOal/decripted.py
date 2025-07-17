import base64

# Baca pesan terenkripsi dari file
with open('encrypted_message.txt', 'r') as file:
    encrypted_message = file.read()

# Dekripsi pesan menggunakan Base64
decoded_message = base64.b64decode(encrypted_message).decode('utf-8')

# Cetak pesan yang telah didekripsi
print(decoded_message)
