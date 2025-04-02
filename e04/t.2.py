class Stats:
    def __init__(self):
        self.count = 0
        self.sum = 0

    def add(self, num):
        self.count += 1
        self.sum += num

    def avg(self):
        return self.sum / self.count if self.count else 0

nums = Stats()
even = Stats()
odd = Stats()

while True:
    n = int(input("Number: "))
    if n == -1:
        break
    nums.add(n)
    (even if n % 2 == 0 else odd).add(n)

print("Sum:", nums.sum, "Avg:", nums.avg())
print("Even sum:", even.sum, "Odd sum:", odd.sum)
