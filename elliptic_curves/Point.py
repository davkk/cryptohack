from dataclasses import dataclass
from typing import Optional

# E: Y^2 = X^3 + 497X + 1768 mod 9739

A = 497
B = 1768
F = 9739


@dataclass
class Point:
    x: Optional[int] = None
    y: Optional[int] = None

    def __eq__(self, Q: object, /) -> bool:
        if Q is None:
            return False
        assert isinstance(Q, Point)
        P = self
        return P.x == Q.x and P.y == Q.y

    def __neg__(self) -> "Point":
        assert self.x is not None and self.y is not None
        return Point(self.x, -self.y % F)

    def __add__(self, Q: "Point", /) -> "Point":
        P = self
        if P.x is None and P.y is None:
            return Q
        if Q.x is None and Q.y is None:
            return P

        assert P.x is not None and P.y is not None
        assert Q.x is not None and Q.y is not None

        if P == -Q:
            return Point()

        if P == Q:
            m = (3 * P.x**2 + A) * pow(2 * P.y, -1, F)
        else:
            m = (Q.y - P.y) * pow(Q.x - P.x, -1, F)

        x = (m**2 - P.x - Q.x) % F
        y = (m * (P.x - x) - P.y) % F
        return Point(x, y)

    def __rmul__(self, n: int, /) -> "Point":
        assert isinstance(n, int) and n > 0
        assert self.x is not None and self.y is not None

        Q = self
        R = Point()

        while n > 0:
            if n % 2 == 1:
                try:
                    R = R + Q
                except ValueError:
                    continue

            Q += Q
            n //= 2

        return R


if __name__ == "__main__":
    X = Point(5274, 2841)
    Y = Point(8669, 740)

    assert X + Point() == X
    assert Point() + Y == Y

    assert X + Y == Point(1024, 4440)
    assert X + X == Point(7284, 2107)

    X = Point(5323, 5438)
    assert 1337 * X == Point(1089, 6931)
