from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

ciphertext_hex = "a0dc551be4713b334c76bce5d8d68ed416d3e701ca9a5bc989221a3a69fa6ac0fcfc9291055d5ef5b6b1b2d46cf7341c"
ciphertext = bytes.fromhex(ciphertext_hex)

key = b"PolinesCTF2025!!"
cipher = AES.new(key, AES.MODE_ECB)
plaintext_padded = cipher.decrypt(ciphertext)

try:
    print("Hasil decode:", plaintext_padded.decode())
except:
    print("Gagal decode. Kemungkinan bukan ASCII.")
