import random
import string
import time

text = "word " * 30000
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=20))

for _ in range(500):
    pos = random.randint(0, len(text))
    text = text[:pos] + random_string + text[pos:]

times = []
for _ in range(200):
    start_time = time.time()
    text = text.replace(random_string, "NEWSTRING")
    end_time = time.time()
    times.append(end_time - start_time)

average_time = sum(times) / len(times)
print(f"Average time: {average_time} seconds")

#c part

def replace_text(text, old_str, new_str):
    return text.replace(old_str, new_str)

text = "word " * 30000
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=20))

for _ in range(500):
    pos = random.randint(0, len(text))
    text = text[:pos] + random_string + text[pos:]

times = []
for _ in range(200):
    start_time = time.time()
    text = replace_text(text, random_string, "NEWSTRING")
    end_time = time.time()
    times.append(end_time - start_time)

average_time = sum(times) / len(times)
print("Average time:", average_time)
