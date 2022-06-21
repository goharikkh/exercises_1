l1 = input('how many bottles with less than a litre capacity do you have?')
l2 = input('How many bottles with capacities greater than a litre do you have?')


def bottle(a, b):
    return float(a) * 0.10 + float(b) * 0.25


print(bottle(l1, l2), '$')
