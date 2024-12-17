import owiener
from Crypto.Util.number import long_to_bytes

N = 0xB8AF3D3AFB893A602DE4AFE2A29D7615075D1E570F8BAD8EBBE9B5B9076594CF06B6E7B30905B6420E950043380EA746F0A14DAE34469AA723E946E484A58BCD92D1039105871FFD63FFE64534B7D7F8D84B4A569723F7A833E6DAF5E182D658655F739A4E37BD9F4A44AFF6CA0255CDA5313C3048F56EED5B21DC8D88BF5A8F8379EAC83D8523E484FA6AE8DBCB239E65D3777829A6903D779CD2498B255FCF275E5F49471F35992435EE7CADE98C8E82A8BEB5CE1749349CAA16759AFC4E799EDB12D299374D748A9E3C82E1CC983CDF9DAEC0A2739DADCC0982C1E7E492139CBFF18C5D44529407EDFD8E75743D2F51CE2B58573FEA6FBD4FE25154B9964D
e = 0x9AB58DBC8049B574C361573955F08EA69F97ECF37400F9626D8F5AC55CA087165CE5E1F459EF6FA5F158CC8E75CB400A7473E89DD38922EAD221B33BC33D6D716FB0E4E127B0FC18A197DAF856A7062B49FBA7A86E3A138956AF04F481B7A7D481994AEEBC2672E500F3F6D8C581268C2CFAD4845158F79C2EF28F242F4FA8F6E573B8723A752D96169C9D885ADA59CDEB6DBE932DE86A019A7E8FC8AEB07748CFB272BD36D94FE83351252187C2E0BC58BB7A0A0AF154B63397E6C68AF4314601E29B07CAED301B6831CF34CAA579EB42A8C8BF69898D04B495174B5D7DE0F20CF2B8FC55ED35C6AD157D3E7009F16D6B61786EE40583850E67AF13E9D25BE3
c = 0x3F984FF5244F1836ED69361F29905CA1AE6B3DCF249133C398D7762F5E277919174694293989144C9D25E940D2F66058B2289C75D1B8D0729F9A7C4564404A5FD4313675F85F31B47156068878E236C5635156B0FA21E24346C2041AE42423078577A1413F41375A4D49296AB17910AE214B45155C4570F95CA874CCAE9FA80433A1AB453CBB28D780C2F1F4DC7071C93AFF3924D76C5B4068A0371DFF82531313F281A8ACADAA2BD5078D3DDCEFCB981F37FF9B8B14C7D9BF1ACCFFE7857160982A2C7D9EE01D3E82265EEC9C7401ECC7F02581FD0D912684F42D1B71DF87A1CA51515AAB4E58FAB4DA96E154EA6CDFB573A71D81B2EA4A080A1066E1BC3474

# https://cryptohack.gitbook.io/cryptobook/untitled/low-private-component-attacks/wieners-attack
# d = getPrime(256) => small
# d < 1/3 * N^1/4

d = owiener.attack(e, N)
assert d

print(long_to_bytes(pow(c, d, N)).decode("utf-8"))
