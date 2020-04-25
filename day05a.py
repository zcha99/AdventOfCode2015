rawList = open("day05.txt", "r").read().splitlines() # Lista där varje rad är eget segment
naughtyString = 0 # Sätter startvärde för antal naughty strings
goodString = 0 # sätter startvärde för antal good strings

print("Total number of strings: ", len(rawList))
# Här påbörjas en loop för varje textrad
for i in range(len(rawList)):
    naughty = 0
    vowel = 0
    crit1 = False
    crit2 = False
    santaString = rawList[i]

    # Loop för att jämföra två intilliggande värde i strängen.
    # Används för både crit2 och naughty
    for i in range(int(len(santaString)-1)):

        # Tar fram dubbelbokstäver, ett av två kriterier som behövs för good
        if santaString[i] == santaString[i+1]:
            crit2 = True    
        
        # Kollar om någon av naughty-combinationerna finns i strängen
        if santaString[i:i+2] == 'ab':
            naughty = 1
        elif santaString[i:i+2] == 'cd':
            naughty = 1
        elif santaString[i:i+2] == 'pq':
            naughty = 1
        elif santaString[i:i+2] == 'xy':
            naughty = 1
 
    # Loop för att kolla om antalet vokaler är 3 eller mer dvs crit 1
    for i in range(int(len(santaString))):
        if vowel < 3:
            if santaString[i] == 'a':
                vowel += 1
                if vowel == 3:
                    crit1 = True
            elif santaString[i] == 'e':
                vowel += 1
                if vowel == 3:
                    crit1 = True
            elif santaString[i] == 'i':
                vowel += 1
                if vowel == 3:
                    crit1 = True
            elif santaString[i] == 'o':
                vowel += 1
                if vowel == 3:
                    crit1 = True
            elif santaString[i] == 'u':
                vowel += 1
                if vowel == 3:
                    crit1 = True

    # Kollar om en rad är god, dvs crit1 och crit 2 = True
    if naughty == 1:
        naughtyString += 1
    elif crit1 == True:
        if crit2 == True:
             goodString += 1
        
crit1 = False
crit2 = False
naughty = 0

print("Number of naughty strings: ", naughtyString)
print("Number of good strings: ", goodString)

