print()
# Muuttujien määrittäminen
m1 = 12345
m2 = "Pälä Pälä"
print(m1)
print(m2)
print()

# Python on dynaamisesti tyypitetty kieli
# Muuttujan tyyppi päätellään ajon aikana, kun muuttujanalustava rivi suoritetaan
# Muuttujan tyypin pystyy muuttamaan määrittämällä muuttuja uudelleen
m1 = "Tekstiä" # Muuttuja muuttui Int -> String
print(m1)

m1 = 1              # Integer, kokonaisluku
m2 = "Pälä Pälä"    # String, merkkijono
m3 = 1,2            # Float, desimaaliluku
m4 = True           # Boolean, totuusarvo (T/F)
print()

# Matikkaa
nro1 = 2
nro2 = 4
tulos = 0

tulos = nro1 + nro2
print(tulos)

#tulos = tulos - nro1
tulos -= nro1 # Simplex
print(tulos)  # 6 - 2
#vastaavasti    +=    -=    *=    /=    kaikki tekevät laskun ja sijoituksen

tulos = nro1 / nro2
print(tulos)
# tulos float vaikka nro1 ja nro2 kumpikin Int.
# tulos = nro1 // nro 2 Tämä palauttaa Integer.

# Python on vahvasti tyypitetty kieli
muuttuja1 = 10
muuttuja2 = "Tekstiä"

# Esim eri tyyppisten muuttujien yhteenlasku ei ole mahdollista
# print(muuttuja2 + muuttuja1)

# Koodaajan vastuullaon suorittaa tyyppimuunnos
# Alla oleva koodi muuttaa int -> str
print(muuttuja2 + str(muuttuja1))
print()

# Lainausmerkit
print("Tulostuuko tämä?")    # ok
print('Tulostuuko tämä?')    # ok
print('Tämä on "lainaus"')   # ok
print("Tämä on \"lainaus\"") # ok
print()

# lainausmerkit voidaan merkitä kenoviivalla, jolloin se tulkitaan kuuluvan osaksi merkkijonoa
print("rivi \nrivi2")   # \n on rivinvaihto

Longtext = "quick brown fox jumps over the lazy dog \
quick brown fox jumps over the lazy dog \
quick brown fox jumps over the lazy dog \
quick brown fox jumps over the lazy dog \
quick brown fox jumps over the lazy dog"
print(Longtext)

# Tyyppimuunnoksia
# int muuttaa integeriksi
# float muuttaa desimaaliksi
# str muuttaa stringiksi

print(bool(0))  # kaikki paitsi 0 on true
print()

# if elif else
number1 = 2
number2 = 10

if number2 > number1:
    print("eka on suurempi kuin toka")
elif number1 > number2:
    print("toka on suurempi kuin eka")
else:
    print("numerot ovat yhtä suuret")
print("ohjelma päättyy")

# Käyttäjän syöte
print("Anna sana")
syote = input()
print("Käyttäjän syötti sanan " + syote)
