from hashlib import sha1

from Crypto.Cipher import AES

p = 1331169830894825846283645180581
a = -35
b = 98
EC = EllipticCurve(GF(p), [a, b])

G = EC(479691812266187139164535778017, 568535594075310466177352868412)
P1 = EC(1110072782478160369250829345256, 800079550745409318906383650948)
P2 = EC(1290982289093010194550717223760, 762857612860564354370535420319)

# znalezienie najmniejszej liczby k, takiej że l | (p^k − 1) => p^k === 1 mod l
k = 1
while (p**k - 1) % EC.order():
    k += 1
print(f"{k=}")

# https://people.cs.nycu.edu.tw/~rjchen/ECC2009/19_MOVattack.pdf
ECpk = EllipticCurve(GF(p**k, "y"), [a, b])

R = ECpk.random_point()
m = R.order()
d = gcd(m, G.order())
T1 = (m // d) * R

Gpk = ECpk(G)
Bpk = ECpk(P2)

w1 = Gpk.weil_pairing(T1, G.order())
w2 = Bpk.weil_pairing(T1, G.order())

n_b = w2.log(w1)

iv = bytes.fromhex("eac58c26203c04f68d63dc2c58d79aca")
encrypted_flag = bytes.fromhex(
    "bb9ecbd3662d0671fd222ccb07e27b5500f304e3621a6f8e9c815bc8e4e6ee6ebc718ce9ca115cb4e41acb90dbcabb0d"
)

x, _ = (P1 * n_b).xy()
print(f"{x=}")

key = sha1(str(x).encode("ascii")).digest()[:16]
cipher = AES.new(key, AES.MODE_CBC, iv)

print(cipher.decrypt(encrypted_flag).decode("utf-8"))
