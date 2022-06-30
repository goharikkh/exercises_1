m = input('how much money order cost?')


def tip(a):
    return float(a) * 0.18


def tax(a):
    return float(tip(a)) * 0.2


print(f'Tips {tip(m):.2f}$')
print(f'Taxes {tax(m):.2f}$')
print(f'Total {tip(m) + tax(m):.2f}$')
