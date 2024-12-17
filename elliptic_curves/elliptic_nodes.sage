from Crypto.Util.number import long_to_bytes

p = 4368590184733545720227961182704359358435747188309319510520316493183539079703

# G
gx = 8742397231329873984594235438374590234800923467289367269837473862487362482
gy = 225987949353410341392975247044711665782695329311463646299187580326445253608

# Q
qx = 2582928974243465355371953056699793745022552378548418288211138499777818633265
qy = 2421683573446497972507172385881793260176370025964652384676141384239699096612

# uklad dwoch rownan: y^2 === x^3 + a*x + b
# gy^2 === gx^3 + a*gx + b => b = gy^2 - gx^3 - a*gx mod p
# qy^2 === qx^3 + a*qx + (gy^2 - gx^3 - a*gx) mod p
# qy^2 - gy^2 + gx^3 - qx^3 === a*(qx - gx) mod p
# zatem: a === (qy^2 - gy^2 + gx^3 - qx^3) * (qx - gx)^-1 mod p
a = ((qy**2 - gy**2 + gx**3 - qx**3) * pow((qx - gx), -1, p)) % p
b = (gy**2 - gx**3 - a * gx) % p

# error: singular curve
# EC = EllipticCurve(GF(p), [a, b])
# 4a^3 + 27b^2 == 0 => nie spelnia warunku na elliptic curve

# https://ask.sagemath.org/question/48982/sagemath-refuses-to-load-singular-curve/
F.<x> = GF(p)[]
f = x ^ 3 + a * x + b
_, (s, _) = f.roots() # podwojny pierwiastek => punkt osobliwy
print(f"{s=}")

# przesuniecie by punkt osobliwy stal sie (0, 0)
f = f.subs(x=x + s)
print(f"{f=}")
# funkcja o postaci: y^2 = x^2 * (x + 305179796174210822247618473361747316085422620437271958999235012896334193460)

(c, _), *_ = f.roots()
m = GF(p)(-c).square_root()

gx = (gx - s) % p
qx = (qx - s) % p

# mapowanie do formy multiplikatywnej: (x, y) -> (y + sqrt(c)*x) / (y - sqrt(c)*x)
u = (gy + m * gx) / (gy - m * gx)
v = (qy + m * qx) / (qy - m * qx)

d = discrete_log(v, u)
print(long_to_bytes(d).decode("utf-8"))
