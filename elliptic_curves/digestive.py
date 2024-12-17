import json

import requests

# https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm
# "Let z be the L_n leftmost bits of e, where L_n is the bit length of the group order n."
# ustawiam wystarczająco długi username, żeby wejść w rejon który już nie liczy się do sygnatury
username = "a" * 100

sign = requests.get(f"https://web.cryptohack.org/digestive/sign/{username}")
s = sign.json()["signature"]

msg = f'{{"admin": false, "username": "{username}", "admin": true}}'
print(msg)
print(json.loads(msg))

r = requests.get(f"https://web.cryptohack.org/digestive/verify/{msg}/{s}")
print(r.json()["flag"])
