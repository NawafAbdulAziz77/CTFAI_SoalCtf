from Crypto.Util.number import inverse

# RSA public info
n = 3233
e = 17
c = 2790

# Faktorisasi n → p dan q diketahui
p = 61
q = 53

# Hitung phi(n)
phi = (p - 1) * (q - 1)

# Hitung private key d
d = inverse(e, phi)

# Dekripsi pesan
m = pow(c, d, n)

# Output
print("Hasil dekripsi (m):", m)

# Konversi ke ASCII (jika ingin karakter)
try:
    print("Hasil ASCII:", chr(m))
except:
    print("Nilai bukan karakter valid.")
