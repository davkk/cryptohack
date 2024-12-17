import math
from collections import namedtuple
from hashlib import sha1

from Crypto.Cipher import AES
from sympy import discrete_log

Point = namedtuple("Point", "x y")

# parameters
p = 173754216895752892448109692432341061254596347285717132408796456167143559
D = 529

# generator point
G = Point(
    29394812077144852405795385333766317269085018265469771684226884125940148,
    94108086667844986046802106544375316173742538919949485639896613738390948,
)

# ouput
A = Point(
    x=155781055760279718382374741001148850818103179141959728567110540865590463,
    y=73794785561346677848810778233901832813072697504335306937799336126503714,
)
B = Point(
    x=171226959585314864221294077932510094779925634276949970785138593200069419,
    y=54353971839516652938533335476115503436865545966356461292708042305317630,
)

iv = bytes.fromhex("64bc75c8b38017e1397c46f85d4e332b")
encrypted_flag = bytes.fromhex(
    "13e4d200708b786d8f7c3bd2dc5de0201f0d7879192e6603d7c5d6b963e1df2943e3ff75f7fda9c30a92171bbbc5acbf"
)


def point_addition(P, Q):
    Rx = (P.x * Q.x + D * P.y * Q.y) % p
    Ry = (P.x * Q.y + P.y * Q.x) % p
    return Point(Rx, Ry)


def scalar_multiplication(P, n):
    Q = Point(1, 0)
    while n > 0:
        if n % 2 == 1:
            Q = point_addition(Q, P)
        P = point_addition(P, P)
        n = n // 2
    return Q


# patrzac na kod: assert (A.x**2 - D * A.y**2) % p == 1
# x^2 - Dy^2 = 1 => hiperbola
# [x - sqrt(D) y][x + sqrt(D) y] = 1

# zatem, zamiana zmiennych:
# u = x - sqrt(D) y
# v = x + sqrt(D) y
# uv = 1

u = G.x - int(math.sqrt(D)) * G.y
v = A.x - int(math.sqrt(D)) * A.y

n_a = discrete_log(p, v, u)

shared = scalar_multiplication(B, n_a).x
key = sha1(str(shared).encode("ascii")).digest()[:16]
cipher = AES.new(key, AES.MODE_CBC, iv)

print(cipher.decrypt(encrypted_flag))
