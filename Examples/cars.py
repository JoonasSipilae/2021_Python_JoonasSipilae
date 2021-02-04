# Dictionary sisältää avain-arvo -pareja. Avaimien on oltava yksilöllisiä.
# Arvoja indeksoidaan avaimilla

# brandKey = "brand"
# modelKey = "model"
# yearKey = "year"
# priceKey = "price"
# colorKey = "color"

carInfo = {
    "brand": "Toyota", 
    "model": "Corolla", 
    "year": 2010, 
    "price": 6502.15
}
print(carInfo)

carInfo["color"] = "red"
print(carInfo)  # arvon lisäys dictionaryyn

carInfo["year"] = 2011
print(carInfo) # arvon vaihtaminen

# datan tallentaminen
price = carInfo["price"]
print(price)
print()


# Avain-arvo -parit poistetaan pop-funktiolla
color = carInfo.pop("color")
print(color)

color = carInfo.pop("color", "N/A") # Määritetään default-väriksi N/A. Jos avainta
# ei löydy. palautetaan oletusarvo jos sellainen on välitetty funktiolle parametrina (???)
# jos oletusta ei ole välitetty, Python nostaa virheen.
print(color)

