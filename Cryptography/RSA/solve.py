from Crypto.Util.number import getPrime, long_to_bytes, bytes_to_long
import gmpy2

exec(open("output.txt", "r").read())

tot = (p - 1) * (q - 1)
d = gmpy2.invert(e, tot)

m = pow(c, d, n)

print(long_to_bytes(m))
