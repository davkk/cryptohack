import json
import socket

from Crypto.Util.number import long_to_bytes


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


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("socket.cryptohack.org", 13374))
sock.settimeout(1)

recv_all(sock)

sock.send(json.dumps(dict(option="get_secret")).encode())

secret = json.loads(recv_all(sock))["secret"]

sock.send(json.dumps(dict(option="sign", msg=secret)).encode())

signature = json.loads(recv_all(sock))["signature"]
print(long_to_bytes(int(signature, 16)))
