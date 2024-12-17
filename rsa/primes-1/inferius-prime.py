from Crypto.Util.number import long_to_bytes
from factordb.factordb import FactorDB

n = 984994081290620368062168960884976209711107645166770780785733
e = 65537
ct = 948553474947320504624302879933619818331484350431616834086273

f = FactorDB(n)
f.connect()

p, q = f.get_factor_list()

d = pow(e, -1, (p - 1) * (q - 1))
m = pow(ct, d, n)

print(long_to_bytes(m).decode("utf-8"))
