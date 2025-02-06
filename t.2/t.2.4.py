def factorials(n):
    luvut = {}
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i
        luvut[i] = fact

    return luvut

k = factorials(5)
print(k[1])
print(k[3])
print(k[5])