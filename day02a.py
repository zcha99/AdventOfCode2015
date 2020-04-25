# Rå data i filen day02.txt
rawList = open("day02a.txt", "r").read().splitlines() # Lista där varje box är eget segment

# Globala variabler
totalt = 0

for i in range(len(rawList)):
    test = rawList[i].split("x")    # Delar upp varje objekt i tre delar, x som delare
    a1 = (int(test[0]) * int(test[1])) * 2 # Räknar ut arean för längd x bredd x 2 sidor
    a2 = (int(test[0]) * int(test[2])) * 2 # Räknar ut arean för längd x höjd x 2 sidor
    a3 = (int(test[1]) * int(test[2])) * 2 # Räknar ut arean för bredd x höjd x 2 sidor
    temp = a1   # Sätter ena sidans area som startpunkt 
    if a1 > a2:     # Kollar om sida två är mindre än 1, isf byter vi temp
        temp = a2
    if temp > a3: # Kollar om sida 3 är mindre än temp, isf byter vi
        temp = a3

    a4 = temp / 2 # Reservpappret skall bara vara 1 av minsta sidan, så delar temp med 2 eftersom temp är två sidor

    tot = a1 + a2 + a3 + a4 # Räknar ut totalt behov för objektet rawList[i]
    totalt += tot # Uppdaterar totala behovet med behovet för denna körning

print(totalt) # Skriver ut svaret
    

