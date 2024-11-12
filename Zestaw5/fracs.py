def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)

def reduction(frac):
    num, den = frac

    if den == 0:
        raise ValueError("Mianownik nie może być zerem!!!")

    nwd = gcd(den, num)
    if nwd < 0:
        nwd = -nwd

    if den < 0:
        num, den = -num, -den

    return [num/nwd, den/nwd]

def add_frac(frac1, frac2):         # frac1 + frac2
    num = frac1[0] * frac2[1] + frac2[0] * frac1[1]
    den = frac1[1] * frac2[1]
    return reduction([num, den])

def sub_frac(frac1, frac2):         # frac1 - frac2
    num = frac1[0] * frac2[1] - frac1[1] * frac2[0]
    den = frac1[1] * frac2[1]

    return reduction([num, den])

def mul_frac(frac1, frac2):         # frac1 * frac2
    num = frac1[0] * frac2[0]
    den = frac1[1] * frac2[1]
    return reduction([num, den])

def div_frac(frac1, frac2):         # frac1 / frac2
    num = frac1[0] * frac2[1]
    den = frac1[1] * frac2[0]
    return reduction([num, den])

def is_positive(frac):              # bool, czy dodatni
    return frac[0] * frac[1] > 0

def is_zero(frac):                  # bool, typu [0, x]
    return frac[0] == 0

def cmp_frac(frac1, frac2):         # -1 | 0 | +1
    dif = sub_frac(frac1, frac2)

    if dif[0] > 0:
        return 1
    elif dif[0] < 0:
        return -1
    else:
        return 0

def frac2float(frac):               # konwersja do float
    return frac[0] / frac[1]

# f1 = [-1, 2]      # -1/2
# f2 = [1, -2]      # -1/2 (niejednoznaczność)
# f3 = [0, 1]       # zero
# f4 = [0, 2]       # zero (niejednoznaczność)
# f5 = [3, 1]       # 3
# f6 = [6, 2]       # 3 (niejednoznaczność)