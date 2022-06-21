m = input('how much money order cost?')


def tip(a):
    return float(a) * 0.18


def tax(a):
    return float(tip(a)) * 0.2


print('Tips ', tip(m))
print('Taxes ', tax(m))
print('Total ', tax(m) + tip(m))
