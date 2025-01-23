import random

#t2

Numbers = [int(input("Give ten number: ")) for _ in range(10)]
Strings = [input("Give ten strings: ") for _ in range(10)]

print("original numbers:", Numbers)
print("original strings:", Strings)

Numbers = [random.randint(1, 100) for _ in range(10)]

print("Random numbers:", Numbers)
