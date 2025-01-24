
jono = ["Matti", "Riikka", "Antti", "Jenni", "Anu", "Ville", "Jarno"]
t = 0

print(jono)

jono.remove(jono[0])

Ville = jono.index("Ville")
jono[Ville] = "Anni"
print(jono)

Jarno = jono.index("Jarno")
jono.remove(jono[Jarno])
print(jono)

jono.append("Marjo")
print(jono)

Antti = jono.index("Antti")
jono.append(jono[Antti])
print(jono)