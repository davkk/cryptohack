from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# premorial primes = M is the product of the first n primes
# M = 2 * 3 * ... * P_n

# używam narzędzia https://github.com/RsaCtfTool/RsaCtfTool, który ma w sobie zaimplementowany atak ROCA

# sage@4ca4d005b902:/home/davkk/university/cryptohack$ sage -python RsaCtfTool/RsaCtfTool.py --publickey rsa/primes-2/key.pem --private --attack roca
# ['rsa/primes-2/key.pem']
#
# [*] Testing key rsa/primes-2/key.pem.
# [*] Performing roca attack on rsa/primes-2/key.pem.
# [*] Attack success with roca method !
#
# Results for rsa/primes-2/key.pem:
#
# Private key :
private = """-----BEGIN RSA PRIVATE KEY-----
MIIBNwIBAAJATKIe3jfj1qY7zuX5Eg0JifAUOq6RUwLzRuiru4QKcvtW0Uh1KMp1
GVt4MmKDiQksTok/pKbJsBFCZugFsS3AjQIDAQABAkAWskVWJ1NxdVZtVqtH71iN
4+752k3sOgl3TN3f8aFuoDFcsVOhBl1M47fhsEipW7R965M0sfqIYWKVrEEIzPYB
AiEAqv4siv7LdoZFvQM+kqO9r5Vm/C1h7aRMUJMw2E65VEECIHK7CwdH6LNamIfB
Ku01HD7zUrtTHYN2oNi6OSIUsSlNAiAeI+92ELOMkN56ErhU4Mfuy0b77IP2f590
FH3novjIAQIgTlug9KAQNi6x7kXn44paeEQHRRlHFvp2cI7/Zl9rgCECIDAdO53F
Ak/kxhopjCnmRmQ58+dJi/svVt01wuVZyGh8
-----END RSA PRIVATE KEY-----"""

key = RSA.import_key(private)
cipher = PKCS1_OAEP.new(key)
plaintext = cipher.decrypt(
    bytes.fromhex(
        "249d72cd1d287b1a15a3881f2bff5788bc4bf62c789f2df44d88aae805b54c9a94b8944c0ba798f70062b66160fee312b98879f1dd5d17b33095feb3c5830d28"
    )
)

print(plaintext.decode("utf-8"))
