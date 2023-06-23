from Crypto.Util.number import getPrime, long_to_bytes, bytes_to_long

FLAG = b'ForestyHC{knowing_basic_of_RSA_calculation_1af53a}'

p = getPrime(512)
q = getPrime(512)

m = bytes_to_long(FLAG)
n = p * q
e = 65537

c = pow(m, e, n)

print(f'{p = }')
print(f'{q = }')
print(f'{n = }')
print(f'{e = }')
print(f'{c = }')

# decrypt

# import gmpy2

# tot = (p - 1) * (q - 1)
# d = gmpy2.invert(e, tot)

# m = pow(c, d, n)

# print(long_to_bytes(m))