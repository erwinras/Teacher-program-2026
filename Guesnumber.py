from random import randint
 
ondergrens = int(input("Geef een getal voor de ondergrens: "))
bovengrens = int(input("Geef een getal voor de bovengrens: "))
computerGetal = randint(ondergrens,bovengrens)
gameover = False
aantalKeer = 0
aantalKeerMax = 8
 
while not gameover:
    aantalKeer += 1
    gebruikerGetal = int(input("#" + str(aantalKeer) + ": Raad een getal tussen de " + str(ondergrens) + " en de " + str(bovengrens) + ": "))
 
    if bovengrens < gebruikerGetal:
        print("Dat is geen handige keuze, veel te hoog!\n")
 
    elif ondergrens > gebruikerGetal:
        print("Dat is geen handige keuze, veel te laag!\n")
 
    elif computerGetal < gebruikerGetal:
        print("Het getal van de computer is kleiner!\n")
        bovengrens = gebruikerGetal
 
    elif computerGetal > gebruikerGetal:
        print("Het getal van de computer is groter!\n")
        ondergrens = gebruikerGetal
 
    else:
        print("\nJe hebt het geraden!")
        gameover = True
 
    if aantalKeer == aantalKeerMax:
        print("\nGamer over!")
        gameover = True