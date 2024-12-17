import json
import socket

import requests

HOST = "socket.cryptohack.org"
PORT = 13398

FLAG = b"crypto{???????????????????????????????????}"

N = 56135841374488684373258694423292882709478511628224823806418810596720294684253418942704418179091997825551647866062286502441190115027708222460662070779175994701788428003909010382045613207284532791741873673703066633119446610400693458529100429608337219231960657953091738271259191554117313396642763210860060639141073846574854063639566514714132858435468712515314075072939175199679898398182825994936320483610198366472677612791756619011108922142762239138617449089169337289850195216113264566855267751924532728815955224322883877527042705441652709430700299472818705784229370198468215837020914928178388248878021890768324401897370624585349884198333555859109919450686780542004499282760223378846810870449633398616669951505955844529109916358388422428604135236531474213891506793466625402941248015834590154103947822771207939622459156386080305634677080506350249632630514863938445888806223951124355094468682539815309458151531117637927820629042605402188751144912274644498695897277


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

_ = sock.recv(1024)

factors = [
    int(factor) ** power
    for factor, power in requests.get(
        f"https://factordb.com/api/https://factordb.com/index.php?query={N}"
    ).json()["factors"]
]


def send(data):
    req = json.dumps(data)
    sock.sendall(req.encode())
    resp = sock.recv(4096).decode()
    return json.loads(resp)


def is_valid(bit):
    for factor in factors:
        if pow(bit, (factor - 1) // 2, factor) != 1:
            return False
    return True


def get_bit(i):
    for _ in range(10):
        response = send(dict(option="get_bit", i=i))
        if "error" in response:
            print(response)
            return None
        bit = int(response["bit"], 16)

        if is_valid(bit):
            return 1
    return 0


flag = []
curr_byte = ""

for i in range(len(FLAG) * 8):
    bit = get_bit(i)
    if bit is None:
        break

    curr_byte = str(bit) + curr_byte

    if len(curr_byte) == 8:
        print(curr_byte, chr(int(curr_byte, 2)))
        flag.append(int(curr_byte, 2))
        curr_byte = ""

sock.close()
print(bytes(flag).decode())
