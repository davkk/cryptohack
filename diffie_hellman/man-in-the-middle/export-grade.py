import hashlib
import json
import socket

from Crypto.Cipher import AES
from sympy import discrete_log


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
sock.connect(("socket.cryptohack.org", 13379))
sock.settimeout(1)

recv_all(sock)

# {"supported": ["DH1536", "DH1024", "DH512", "DH256", "DH128", "DH64"]}
sock.send(json.dumps({"supported": ["DH64"]}).encode("utf-8"))

bob, _ = recv_all(sock).splitlines()
bob = parse_resp(bob)

sock.send(json.dumps(bob).encode("utf-8"))

alice, bob, secret = recv_all(sock).splitlines()
alice = parse_resp(alice)
bob = parse_resp(bob)
secret = parse_resp(secret)

p = int(alice["p"], 16)
g = int(alice["g"], 16)
A = int(alice["A"], 16)
B = int(bob["B"], 16)

iv = bytes.fromhex(secret["iv"])
encrypted_flag = bytes.fromhex(secret["encrypted_flag"])

a = discrete_log(p, A, g)
secret = pow(B, a, p)

sha1 = hashlib.sha1()
sha1.update(str(secret).encode("ascii"))
key = sha1.digest()[:16]

cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(encrypted_flag)

print(plaintext.decode("utf-8"))

sock.close()
