print()
a = 10
b = 20

# Vertailuoperaattoreita

# == yhtäsuuruusvertailu
if a == b:
    print(a, "equals", b)   # sep-parametrillä voidaan määritellä erotinmerkki
else:
    print(a, "does not equal", b)

# != erisuuruusvertailu
if a != b:
    print(a, "does not equal", b)
else:
    print(a, "equals", b)

if not a == b:
    print(a, "does not equal", b)
else:
    print(a, "equals", b)

# and
if a < 30 and b < 30:
    print(a, "and", b, "are both smaller than 30")

# pienempi, suurempi
if a < b:
    print(a, "is less than", b)
elif a > b:
    print(b, "is less than", a)
else:
    print(a, "equals", b)

# <= , >=
if a <= b:
    print(a, "is less than or equals", b)
else:
    print(b, "is less than or equals", a)

# vertailun tulos muuttujaan
result = a == b
print(result)

if result:
    print(a, "equals", b)
else:
    print(a, "does not equal", b)

print()
# pythonissa ei switch-case rakennetta

