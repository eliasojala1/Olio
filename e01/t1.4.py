#t4

def main():
    count = 0
    while True:
        number = int(input("give a number, 0=stop"))
        if number == 0:
            break
        if number < 0:
            count += 1
    print("number of negative numers:", count)
    
main()