def add_poly(poly1, poly2):         # poly1(x) + poly2(x)
    if len(poly1) > len(poly2):
        poly2 = poly2 + [0] * (len(poly1) - len(poly2))
    elif len(poly1) < len(poly2):
        poly1 = poly1 + [0] * (len(poly2) - len(poly1))

    result = [a + b for a, b in zip(poly1, poly2)]
    return result

def sub_poly(poly1, poly2):         # poly1(x) - poly2(x)
    if len(poly1) > len(poly2):
        poly2 = poly2 + [0] * (len(poly1) - len(poly2))
    elif len(poly1) < len(poly2):
        poly1 = poly1 + [0] * (len(poly2) - len(poly1))

    result = [a - b for a, b in zip(poly1, poly2)]
    return result

def mul_poly(poly1, poly2):         # poly1(x) * poly2(x)
    result = [0] * (len(poly1) + len(poly2) - 1)

    for i, a in enumerate(poly1):
        for j, b in enumerate(poly2):
            result[i + j] += a * b

    return result

def is_zero(poly):                  # bool, [0], [0,0], itp.
    return all(wsp == 0 for wsp in poly)

def eq_poly(poly1, poly2):         # bool, porównywanie poly1(x) == poly2(x)
    while len(poly1) > 1 and poly1[-1] == 0:
        poly1.pop()
    while len(poly2) > 1 and poly2[-1] == 0:
        poly2.pop()

    return poly1 == poly2

def eval_poly(poly, x0):            # poly(x0), algorytm Hornera
    return sum(wsp * (x0 ** i) for i, wsp in enumerate(poly))

def combine_poly(poly1, poly2): pass    # poly1(poly2(x)), trudne!

def pow_poly(poly, n):              # poly(x) ** n
    if n == 0:
        return [1]

    result = poly

    for _ in range(1, n):
        result = mul_poly(result, poly)

    return result

def diff_poly(poly):                # pochodna wielomianu
    return [poly[i] * i for i in range(1, len(poly))]

# p1 = [2, 1]                   # W(x) = 2 + x
# p2 = [2, 1, 0]                # jw  (niejednoznaczność)
# p3 = [-3, 0, 1]               # W(x) = -3 + x^2
# p4 = [3]                      # W(x) = 3, wielomian zerowego stopnia
# p5 = [0]                      # zero
# p6 = [0, 0, 0]                # zero (niejednoznaczność)