print("hello world")


#Dit is commentaar

x = 3 # een integer --> een geheel getal
y = 5.5 # een float --> punt
z = "3" # een string --> aanhalingstekens

print("x is van het type" + str((type(x))))
print(type(y))
print(type(z))


#naam = input ("tik uw naam in")
#print(naam)

print("een tekst met \"quotes rond\" python 3 escape caracters")

#oef 1
print("huyghe")
print("thibault")
print("thibault.huyghe@student.howest.be")

#oef 2
print("labo basic programming\n \t labo week 1 \n \t \t Kennismaking met \“Python\" \n \t \t Werken met variabelen \n labo basic programming \n \t Labo week2  ")

#oef 3
naam = input("Geef je naam in")
voornaam= input("Geef je voornaam in")
leeftijd = input("Geef je leeftijd in")

print("voornaam is" + voornaam + "naam is " + naam + "leeftijd is " + leeftijd )
# beter is FORMAT
print("je voornaam is : {1}: je naam is: {2} :je leeftijd is :{3}".format(voornaam,naam,leeftijd))

# oef 4
basis = input("Geef de basis van de driehoek op:")
hoogte= input("Geef de hoogte van de driehoek op:")

print("De oppervlakte bedraagt" , basis+hoogte)