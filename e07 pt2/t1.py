from functools import reduce

#map example

def map_lambda(x):
    return list(map(lambda a: a + 1, x))

def map_for(x):
    y = []
    for a in x:
        y.append(a + 1)
    return y

#filter example

def filter_lambda(x):
    return list(filter(lambda a: a > 5, x))

def filter_for(x):
    y = []
    for a in x:
        if a > 5:
            y.append(a)
    return y

#reduce example

def reduce_lambda(x):
    return reduce(lambda a, b: a + b, x)

def reduce_for(x):
    y = 0
    for a in x:
        y = y + a
    return y

#sorted example

def sorted_lambda(x):
    return sorted(x, key=lambda a: len(a))

def sorted_for(x):
    return sorted(x, key=len)

#Testing environment

numbers = [1, 4, 5, 8]
words = ["word", "a", "example"]

print(map_lambda(numbers))
print(map_for(numbers))

print(filter_lambda(numbers))
print(filter_for(numbers))

print(reduce_lambda(numbers))
print(reduce_for(numbers))

print(sorted_lambda(words))
print(sorted_for(words))