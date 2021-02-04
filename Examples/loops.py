print()

for x in "banana":
    print(x)
print()

counter = 10
while counter >= 0:
    print(counter)
    counter -=1
else:
    print("Silmukka päättyy \n")

# break ja continue
# break keskeyttää silmukan suorittamisen
counter = 10
index = 0
while counter >= 0:
    if index >= 5:
        break
    print(counter)
    counter -= 1
    index += 1
else:
    print("tätä ei suoriteta koska break")
# continue keskeyttää tämänhetkisen kierroksen suorittamisen 
# ja siirtyy silmukan seuraavalle kierrokselle
start = 0
end = 10

print()
while start <= end:
    start += 1
    if start % 2 != 0: # % module eli jakojäännös
        continue
    print(start)

print()
cars = ["Toyota", "Volvo", "Mazda", "Audi"]
for car in cars:
    print(car)

sequence = range(len(cars))
for index in sequence:
    print(cars[index])

print()
units = {"tank", "soldier", "ship", "plane"}
for unit in units:
    print(unit)