from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = b"PolinesCTF2025!!"
plaintext = b"PolinesCTF{AES_ECB_IS_NOT_SECURE}.\n"
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

print(ciphertext.hex())
