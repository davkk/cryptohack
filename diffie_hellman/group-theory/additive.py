import hashlib
import json
import socket

from Crypto.Cipher import AES


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


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("socket.cryptohack.org", 13380))
sock.settimeout(1)

alice, bob, secret = recv_all(sock).splitlines()
alice = parse_resp(alice)
bob = parse_resp(bob)
secret = parse_resp(secret)

p = int(alice["p"], 16)
g = int(alice["g"], 16)
A = int(alice["A"], 16)

B = int(bob["B"], 16)

iv = bytes.fromhex(secret["iv"])
encrypted = bytes.fromhex(secret["encrypted"])

# A = a g  % p
# A g^-1 = a g g^-1  % p
# A g^-1 = a  % p

a = (A * pow(g, -1, p)) % p
shared = (B * a) % p

sha1 = hashlib.sha1()
sha1.update(str(shared).encode("ascii"))
key = sha1.digest()[:16]

cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(encrypted)

print(plaintext.decode("utf-8").strip())

sock.close()
