def sum1_a(n):
    s = 1
    for i in range(2, n):
        s += i
    return s


a = int(input('Enter the number'))
print(sum1_a(a))
