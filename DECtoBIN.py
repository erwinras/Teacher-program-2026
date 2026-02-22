import math
 
# Een functie om naar een (geldig) decimaal getal tussen de 0 en 256 te vragen
def vraagDecimaalGetal():
    # Zo lang de invoer ongeldig is ..
    invoer = -1
    while not (invoer < 256 and invoer >= 0):
        # .. vraag om nieuwe invoer
        invoer = int(input("Geef een positief decimaal getal < 256 :"))
        
    # Geef de (juiste) invoer terug
    return invoer
 
 
# Een functie om een decimaal getal naar binair om te zetten
def decimaalNaarBinair(decimaal):
    # In deze variabele komt de uitvoer
    binair = ""
 
    # Een loop die in machten van 2 terug gaat van 128 naar 2.
    i = 128
    while i > 0:
 
        # Als deze macht (i) 'past' dan moet deze bit 1 zijn
        if (decimaal - i) >= 0:
            decimaal = decimaal - i
            binair = binair + "1"
 
        # En anders 0
        else:
            binair = binair + "0"
            
        # De loop moet stoppen bij 1
        if i == 1:
            break
        
        # Loopvariabele een macht van 2 minder maken
        i = math.floor(i / 2)
 
    # Geef de binaire waarde terug
    return binair
 
 
 
# Hoofdprogramma
print("Welkom bij decimaal naar binair!");
 
# Vraag het decimale getal
decimaal = vraagDecimaalGetal()
 
# Zet dit om naar een binair getal met de functie decimaalNaarBinair
binair = decimaalNaarBinair(decimaal)
 
# Geef de uitkomst weer
print("Het decimale getal " + str(decimaal) + " is binair: " + binair)