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
sock.connect(("socket.cryptohack.org", 13371))
sock.settimeout(1)

alice, _ = recv_all(sock).splitlines()
alice = parse_resp(alice)
p = alice["p"]
g = alice["g"]
A = alice["A"]

sock.send(json.dumps(alice).encode("utf-8"))

# nie ma znaczenia co wysyla bob
recv_all(sock)

bob = json.dumps(dict(B=str(0x1)))  # B = A ** 0 = 1
sock.send(bob.encode("utf-8"))

resp = parse_resp(recv_all(sock))

iv = resp["iv"]
encrypted_flag = resp["encrypted_flag"]

sha1 = hashlib.sha1()
sha1.update(str(0x1).encode("ascii"))
key = sha1.digest()[:16]

ciphertext = bytes.fromhex(encrypted_flag)
iv = bytes.fromhex(iv)

cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(ciphertext)

print(plaintext.decode("utf-8"))

sock.close()
