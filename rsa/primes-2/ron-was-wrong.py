# skrypt do sprawdzenia pojedynczej pary publicznych kluczy i zaszyfrowanych wiadomości
# uruchamiany za pomocą Linuxowego narzędzia GNU Parallel:
#
# $ parallel -j12 python ron-was-wrong.py {1} {2} ::: {1..50} ::: {1..50}
#
# co pozwala na równoległe szukanie odpowiedniej pary, która da flagę

import math
import sys
from pathlib import Path

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

assert len(sys.argv) == 3


def get_contents(idx: int):
    path = Path(__file__).parent
    ct = bytes.fromhex(open(path / f"keys_and_messages/{idx}.ciphertext").read())
    public = RSA.import_key(open(path / f"keys_and_messages/{idx}.pem", "r").read())
    return ct, public


ct1, p1 = get_contents(int(sys.argv[1]))
ct2, p2 = get_contents(int(sys.argv[2]))

p = math.gcd(p1.n, p2.n)


def decrypt(n, e, ct):
    q = n // p
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    key = RSA.construct((n, e, d))
    c = PKCS1_OAEP.new(key)
    print(c.decrypt(ct).decode("utf-8"))


try:
    if p != 1:
        decrypt(p1.n, p1.e, ct1)
        decrypt(p2.n, p2.e, ct2)
except ValueError:
    exit(1)
