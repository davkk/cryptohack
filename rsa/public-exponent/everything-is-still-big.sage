from __future__ import print_function
import time

from Crypto.Util.number import long_to_bytes

N = 0xB12746657C720A434861E9A4828B3C89A6B8D4A1BD921054E48D47124DBCC9CFCDCC39261C5E93817C167DB818081613F57729E0039875C72A5AE1F0BC5EF7C933880C2AD528ADBC9B1430003A491E460917B34C4590977DF47772FAB1EE0AB251F94065AB3004893FE1B2958008848B0124F22C4E75F60ED3889FB62E5EF4DCC247A3D6E23072641E62566CD96EE8114B227B8F498F9A578FC6F687D07ACDBB523B6029C5BBEECD5EFAF4C4D35304E5E6B5B95DB0E89299529EB953F52CA3247D4CD03A15939E7D638B168FD00A1CB5B0CC5C2CC98175C1AD0B959C2AB2F17F917C0CCEE8C3FE589B4CB441E817F75E575FC96A4FE7BFEA897F57692B050D2B
e = 0x9D0637FAA46281B533E83CC37E1CF5626BD33F712CC1948622F10EC26F766FB37B9CD6C7A6E4B2C03BCE0DD70D5A3A28B6B0C941D8792BC6A870568790EBCD30F40277AF59E0FD3141E272C48F8E33592965997C7D93006C27BF3A2B8FB71831DFA939C0BA2C7569DD1B660EFC6C8966E674FBE6E051811D92A802C789D895F356CEEC9722D5A7B617D21B8AA42DD6A45DE721953939A5A81B8DFFC9490ACD4F60B0C0475883FF7E2AB50B39B2DEEEDAEFEFFFC52AE2E03F72756D9B4F7B6BD85B1A6764B31312BC375A2298B78B0263D492205D2A5AA7A227ABAF41AB4EA8CE0E75728A5177FE90ACE36FDC5DBA53317BBF90E60A6F2311BB333BF55BA3245F
c = 0xA3BCE6E2E677D7855A1A7819EB1879779D1E1EEFA21A1A6E205C8B46FDC020A2487FDD07DBAE99274204FADDA2BA69AF73627BDDDCB2C403118F507BCA03CB0BAD7A8CD03F70DEFC31FA904D71230AAB98A10E155BF207DA1B1CAC1503F48CAB3758024CC6E62AFE99767E9E4C151B75F60D8F7989C152FDF4FF4B95CEED9A7065F38C68DEE4DD0DA503650D3246D463F504B36E1D6FAFABB35D2390ECF0419B2BB67C4C647FB38511B34EB494D9289C872203FA70F4084D2FA2367A63A8881B74CC38730AD7584328DE6A7D92E4CA18098A15119BAEE91237CEA24975BDFC19BDBCE7C1559899A88125935584CD37C8DD31F3F2B4517EEFAE84E7E588344FA5

# sprawdzenie czy d spelnia warunek na atak Weinera (d < 1/3 * N^1/4)
# https://cryptohack.gitbook.io/cryptobook/untitled/low-private-component-attacks/boneh-durfee-attack
# => mniej ograniczajacy warunek: d < N^0.292


# Atak Boneh-Durfee
# wykorzystanie małego d
# redukcja macierzy do znalezienia klucza prywatnego

# === źródło: https://github.com/mimoo/RSA-and-LLL-attacks/blob/master/boneh_durfee.sage
def remove_unhelpful(BB, monomials, bound, current):
    # end of our recursive function
    if current == -1 or BB.dimensions()[0] <= 7:
        return BB

    # we start by checking from the end
    for ii in range(current, -1, -1):
        # if it is unhelpful:
        if BB[ii, ii] >= bound:
            affected_vectors = 0
            affected_vector_index = 0
            # let's check if it affects other vectors
            for jj in range(ii + 1, BB.dimensions()[0]):
                # if another vector is affected:
                # we increase the count
                if BB[jj, ii] != 0:
                    affected_vectors += 1
                    affected_vector_index = jj

            # level:0
            # if no other vectors end up affected
            # we remove it
            if affected_vectors == 0:
                print("* removing unhelpful vector", ii)
                BB = BB.delete_columns([ii])
                BB = BB.delete_rows([ii])
                monomials.pop(ii)
                BB = remove_unhelpful(BB, monomials, bound, ii-1)
                return BB

            # level:1
            # if just one was affected we check
            # if it is affecting someone else
            elif affected_vectors == 1:
                affected_deeper = True
                for kk in range(affected_vector_index + 1, BB.dimensions()[0]):
                    # if it is affecting even one vector
                    # we give up on this one
                    if BB[kk, affected_vector_index] != 0:
                        affected_deeper = False
                # remove both it if no other vector was affected and
                # this helpful vector is not helpful enough
                # compared to our unhelpful one
                if affected_deeper and abs(bound - BB[affected_vector_index, affected_vector_index]) < abs(bound - BB[ii, ii]):
                    print("* removing unhelpful vectors", ii, "and", affected_vector_index)
                    BB = BB.delete_columns([affected_vector_index, ii])
                    BB = BB.delete_rows([affected_vector_index, ii])
                    monomials.pop(affected_vector_index)
                    monomials.pop(ii)
                    BB = remove_unhelpful(BB, monomials, bound, ii-1)
                    return BB
    # nothing happened
    return BB

def boneh_durfee(pol, modulus, mm, tt, XX, YY):
    # substitution (Herrman and May)
    PR.<u, x, y> = PolynomialRing(ZZ)
    Q = PR.quotient(x*y + 1 - u) # u = xy + 1
    polZ = Q(pol).lift()

    UU = XX*YY + 1

    # x-shifts
    gg = []
    for kk in range(mm + 1):
        for ii in range(mm - kk + 1):
            xshift = x^ii * modulus^(mm - kk) * polZ(u, x, y)^kk
            gg.append(xshift)
    gg.sort()

    # x-shifts list of monomials
    monomials = []
    for polynomial in gg:
        for monomial in polynomial.monomials():
            if monomial not in monomials:
                monomials.append(monomial)
    monomials.sort()

    # y-shifts (selected by Herrman and May)
    for jj in range(1, tt + 1):
        for kk in range(floor(mm/tt) * jj, mm + 1):
            yshift = y^jj * polZ(u, x, y)^kk * modulus^(mm - kk)
            yshift = Q(yshift).lift()
            gg.append(yshift) # substitution

    # y-shifts list of monomials
    for jj in range(1, tt + 1):
        for kk in range(floor(mm/tt) * jj, mm + 1):
            monomials.append(u^kk * y^jj)

    # construct lattice B
    nn = len(monomials)
    BB = Matrix(ZZ, nn)
    for ii in range(nn):
        BB[ii, 0] = gg[ii](0, 0, 0)
        for jj in range(1, ii + 1):
            if monomials[jj] in gg[ii].monomials():
                BB[ii, jj] = gg[ii].monomial_coefficient(monomials[jj]) * monomials[jj](UU,XX,YY)

    # check if determinant is correctly bounded
    det = BB.det()
    bound = modulus^(mm*nn)
    if det >= bound:
        print("We do not have det < bound. Solutions might not be found.")
        print("Try with highers m and t.")
    else:
        print("det(L) < e^(m*n) (good! If a solution exists < N^delta, it will be found)")

    BB = BB.LLL()

    # transform vector i & j -> polynomials 1 & 2
    found_polynomials = False

    for pol1_idx in range(nn - 1):
        for pol2_idx in range(pol1_idx + 1, nn):
            # for i and j, create the two polynomials
            PR.<w,z> = PolynomialRing(ZZ)
            pol1 = pol2 = 0
            for jj in range(nn):
                pol1 += monomials[jj](w*z+1,w,z) * BB[pol1_idx, jj] / monomials[jj](UU,XX,YY)
                pol2 += monomials[jj](w*z+1,w,z) * BB[pol2_idx, jj] / monomials[jj](UU,XX,YY)

            # resultant
            PR.<q> = PolynomialRing(ZZ)
            rr = pol1.resultant(pol2)

            # are these good polynomials?
            if rr.is_zero() or rr.monomials() == [1]:
                continue
            else:
                print("found them, using vectors", pol1_idx, "and", pol2_idx)
                found_polynomials = True
                break
        if found_polynomials:
            break

    if not found_polynomials:
        print("no independant vectors could be found. This should very rarely happen...")
        return 0, 0

    rr = rr(q, q)

    # solutions
    soly = rr.roots()

    if len(soly) == 0:
        print("Your prediction (delta) is too small")
        return 0, 0

    soly = soly[0][0]
    ss = pol1(q, soly)
    solx = ss.roots()[0][0]

    return solx, soly

delta = .18
m = 4

t = int((1-2*delta) * m)
X = 2*floor(N^delta)
Y = floor(N^(1/2))

P.<x,y> = PolynomialRing(ZZ)
A = int((N+1)/2)
pol = 1 + x * (A + y)

solx, soly = boneh_durfee(pol, e, m, t, X, Y)

assert solx > 0

d = int(pol(solx, soly) / e)
# ===

print(long_to_bytes(pow(c, d, N)).decode("utf-8"))

