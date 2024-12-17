from dataclasses import dataclass
from typing import Optional, cast

from sympy import sqrt_mod


@dataclass
class Point:
    x: Optional[int] = None
    y: Optional[int] = None

    def __add__(self, other: "Point", /) -> "Point":
        P = self
        Q = other

        if P.x is None and P.y is None:
            return Q
        if Q.x is None and Q.y is None:
            return P

        assert P.x is not None and P.y is not None
        assert Q.x is not None and Q.y is not None

        if P.x == Q.x:
            if P.y == Q.y:
                return P._double()
            return Point()

        alpha = ((Q.y - P.y) * pow(Q.x - P.x, -1, p)) % p
        x = (B * alpha**2 - A - P.x - Q.x) % p
        y = (alpha * (P.x - x) - P.y) % p
        return Point(x, y)

    def __rmul__(self, k: int, /) -> "Point":
        P = self
        assert P.x is not None and P.y is not None

        R0 = Point()
        R1 = P

        for i in reversed(range(k.bit_length())):
            if (k >> i) & 1:
                R0 += R1
                R1 = R1._double()
            else:
                R1 += R0
                R0 = R0._double()

        return R0

    def _double(self) -> "Point":
        P = self
        if P.x is None and P.y is None:
            return P

        assert P.x is not None and P.y is not None

        if P.y == 0:
            return Point()

        alpha = (3 * P.x**2 + 2 * A * P.x + 1) * pow(2 * B * P.y, -1, p) % p
        x = (B * alpha**2 - A - 2 * P.x) % p
        y = (alpha * (P.x - x) - P.y) % p
        return Point(x, y)


if __name__ == "__main__":
    A = 486662
    B = 1
    p = 2**255 - 19

    gx = 9
    gy = cast(int, sqrt_mod(gx**3 + A * gx**2 + gx, p))
    G = Point(gx, gy)

    Q = 0x1337C0DECAFE * G
    print(Q.x)
