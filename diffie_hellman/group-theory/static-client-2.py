import hashlib
import json
import socket

from Crypto.Cipher import AES
from sympy import discrete_log, isprime


def recv_all(sock):
    data = ""
    while True:
        try:
            chunk = sock.recv(1024)
            if not chunk:
                break
            data += chunk.decode("utf-8")
        except socket.timeout:
            break
    return data


def parse_resp(message: str):
    return json.loads(message[message.find("{") :])


def smooth_p(length: int):
    mul = 1
    i = 1
    while True:
        mul *= i
        if (mul + 1).bit_length() >= length and isprime(mul + 1):
            return mul + 1
        i += 1


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(("socket.cryptohack.org", 13378))
sock.settimeout(3)

alice, bob, secret, _ = recv_all(sock).splitlines()
alice = parse_resp(alice)
bob = parse_resp(bob)
secret = parse_resp(secret)

p = int(alice["p"], 16)
g = int(alice["g"], 16)
A = int(alice["A"], 16)

iv = bytes.fromhex(secret["iv"])
encrypted = bytes.fromhex(secret["encrypted"])


s_p = smooth_p(p.bit_length())
assert s_p is not None

msg = json.dumps({"p": hex(s_p), "g": hex(g), "A": hex(A)})
sock.send(msg.encode("utf-8"))

# B = g^b mod p
bob, _ = recv_all(sock).splitlines()
bob = parse_resp(bob)

B = int(bob["B"], 16)

b = discrete_log(s_p, B, g)

sha1 = hashlib.sha1()
sha1.update(str(pow(A, b, p)).encode("ascii"))
key = sha1.digest()[:16]

cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(encrypted)

print(plaintext.decode("utf-8"))

sock.close()
