import hashlib

from Point import Point

Q_A = Point(815, 3190)
S = 1829 * Q_A

data = str(S.x)
print(hashlib.sha1(data.encode("utf-8")).hexdigest())
