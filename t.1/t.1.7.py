#7

def main():
    maxValue = int(input("Give the max number: "))

    terms = []
    term = 3
    while term <= maxValue:
        terms.append(term)
        term += 3

    termsCount = len(terms)
    sumCount = sum(terms)
    squared = sum(i ** 2 for i in terms)

    print("count of terms:", termsCount)
    print("sum of terms:", sumCount)
    print("squared terms:", squared)

main()