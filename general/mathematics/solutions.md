# General - Mathematics

1. Greatest Common Divisor

```bash
$ go run ./gcd.go 66528 52920
1512
```

2. Extended GCD

```bash
$ go run ./extended-gcd.go 26513 32321
10245 -8404
```

Wynik to min(10245, -8404) = -8404.

3. Modular arithmetic 1

```bash
$ python
>>> 11 % 6
5
>>> 8146798528947 % 17
4
```

Wynik to min(5, 4) = 4.

4. Modular arithmetic 2

Małe twierdzenie Fermata: a^(p-1) % p = 1.
Zatem: 273246787654^65536 % 65537 = 1.

Weryfikacja:

```bash
$ python
>>> 273246787654 ** 65536 % 65537
1
```

5. Modular Inverting

Szukam takiej liczby `d`, że 3 * `d` ≡ 1 (mod 13). Oznacza to, że gdy pomnożę 3 przez `d`, wynik powinien dać resztę 1 przy dzieleniu przez 13.

Mogę wykorzystać Małe twierdzenie Fermata, które mówi, że jeśli pomnoży się dowolną liczbę `g` przez siebie `p`-1 razy, wynikiem będzie 1 (mod p).

3 ^ (12) ≡ 1 (mod 13)
3 ^ (13-1) ≡ 1 (mod 13)

3 ^ (13-1) * 3^(-1) ≡ 3^(-1) (mod 13)
3 ^ (13-2) * 3 * 3^(-1) ≡ 3^(-1) (mod 13)

3 ^ (13-2) ≡ 3^(-1) (mod 13)

Teraz wystarczy obliczyć, np. za pomocą `bc`:
```bash
$ bc <<< "3 ^ 11 % 13"
9
```

Zatem `d` = 9, ponieważ 3 * 9 = 27 ≡ 1 (mod 13).
