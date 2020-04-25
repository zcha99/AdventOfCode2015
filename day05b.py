rawList = open("day05.txt", "r").read().splitlines() # Lista där varje rad är eget segment
goodString = 0 # sätter startvärde för antal good strings

print("Total number of strings: ", len(rawList))
# Här påbörjas en loop för varje textrad
for i in range(len(rawList)):
    pair1 = '00' # En sträng för att jämföra till crit2
    crit1 = False # Om i == i+2 (loop måste vara len - 2)
    crit2 = False # Kollar om värdet i pair1 finns på två ställen i samma sträng
    santaString = rawList[i]

    # Loop för att jämföra två intilliggande värde i strängen.
    # Används för både crit2 och naughty
    for i in range(int(len(santaString)-2)):

        # Tar fram om samma bokstav finns med en annan emellan
        if santaString[i] == santaString[i+2]:
            crit1 = True    
        
    # Loop för att kolla om två intilliggande tecken återfinns i samma rad.
    for i in range(int(len(santaString)-1)):
        pair1 = santaString[i:i+2]
        temp = []  # Ny lista för att kunna kolla crit2
        tempSanta = santaString[i:]  # Gör en ny sträng av det som är kvar att kolla av santaString
        for i in range(int(len(tempSanta)-2)):
            temp.append(tempSanta[i+2:i+4])
            i += 1
        for i in range(int(len(temp))):
            if pair1 == temp[i]:
                crit2 = True      

    # Kollar om en rad är god, dvs crit1 och crit 2 = True
    if crit1 == True:
        if crit2 == True:
             goodString += 1
        
crit1 = False # Nollställ variablerna mellan varje loop
crit2 = False
pair1 = '00'

print("Number of good strings: ", goodString)

