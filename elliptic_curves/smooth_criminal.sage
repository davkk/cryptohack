from hashlib import sha1

from Crypto.Cipher import AES

A = 2
B = 3
F = 310717010502520989590157367261876774703
EC = EllipticCurve(GF(F), [A, B])
# y^2 = x^3 + 2x + 3 mod 310717010502520989590157367261876774703

G = EC(
    179210853392303317793440285562762725654,
    105268671499942631758568591033409611165,
)

# # My secret int, different every time!!
# n = randint(1, p)
#
# # Send this to Bob!
# public = double_and_add(G, n)
# print(public)
public = EC(
    280810182131414898730378982766101210916,
    291506490768054478159835604632710368904,
)

# Bob's public key
B = EC(
    272640099140026426377756188075937988094,
    51062462309521034358726608268084433317,
)

n = public.log(G)
S = n * B
print(f"{S=}")

iv = bytes.fromhex("07e2628b590095a5e332d397b8a59aa7")
encrypted_flag = bytes.fromhex(
    "8220b7c47b36777a737f5ef9caa2814cf20c1c1ef496ec21a9b4833da24a008d0870d3ac3a6ad80065c138a2ed6136af"
)


x, y, *_ = S
key = sha1(str(x).encode("ascii")).digest()[:16]
cipher = AES.new(key, AES.MODE_CBC, iv)

print(cipher.decrypt(encrypted_flag).decode("utf-8"))
