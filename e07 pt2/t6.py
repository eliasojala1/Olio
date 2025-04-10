import re

pattern = r"^H"
string = "Hello, World!"
result = re.match(pattern, string)

if result:
    print("The word starts with H")
else:
    print("No match at the start")

pattern = r"o"
string = "Hello, World!"
result = re.search(pattern, string)

if result:
    print("Found letter o")
else:
    print("No letter o found")

pattern = r"o"
string = "Hello, World!"
result = re.sub(pattern, "0", string)

print(result)