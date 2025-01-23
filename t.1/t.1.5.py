#t5

def main():
    neg_int = 0
    even_int = 0
    while True:
        number = int(input("give a number, 0=stop"))
        if number == 0:
            break
        if number < 0:
            neg_int += 1
        if number % 2 == 0:
            even_int += 1
    print("number of negative numers:", neg_int)
    print("number of negative numers:", even_int)
    
main()