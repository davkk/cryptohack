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
sock.connect(("socket.cryptohack.org", 13373))
sock.settimeout(1)

alice, _, secret, _ = recv_all(sock).splitlines()
alice = parse_resp(alice)
secret = parse_resp(secret)

p = alice["p"]
g = alice["g"]
A = alice["A"]

# uzycie A jako g: g^b = A^b (mod p) = klucz
msg = json.dumps({"p": p, "g": A, "A": "0x01"})
sock.send(msg.encode("utf-8"))

bob, _ = recv_all(sock).splitlines()
bob = parse_resp(bob)

B = int(bob["B"], 16)

iv = bytes.fromhex(secret["iv"])
encrypted = bytes.fromhex(secret["encrypted"])

sha1 = hashlib.sha1()
sha1.update(str(B).encode("ascii"))
key = sha1.digest()[:16]

cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(encrypted)

print(plaintext.decode("utf-8"))

sock.close()
