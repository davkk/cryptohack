import functools

# https://artofproblemsolving.com/wiki/index.php/Chinese_Remainder_Theorem
"""
x === a1 mod d1
x === a2 mod d2
...
x === an mod dn

M = d1 * d2 * ... * dn
Mi = M / di

ai * bi === 1 mod di

zatem: x = sum(ai * bi * yi) mod M
"""

d_arr = [5, 11, 17]
y_arr = [2, 3, 5]

M = functools.reduce(lambda a, b: a * b, d_arr, 1)
x = 0

for yi, di in zip(y_arr, d_arr):
    bi = M // di
    ai = pow(bi, -1, di)
    x += ai * bi * yi

# mod M zeby otrzymac najmniejsze rozwiazanie
print(x % M)
