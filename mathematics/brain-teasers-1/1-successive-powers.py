import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


powers = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]
primes = [p for p in range(100, 1000) if is_prime(p)]

for p in primes:
    try:
        x = (powers[1] * pow(powers[0], -1, p)) % p
        for i in range(2, len(powers)):
            x_curr = (powers[i] * pow(powers[i - 1], -1, p)) % p
            if x == x_curr:
                print(f"crypto{{{p},{x}}}")
                break
    except ValueError:
        pass
