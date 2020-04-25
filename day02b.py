# Rå data i filen day02.txt
rawList = open("day02a.txt", "r").read().splitlines() # Lista där varje box är eget segment

# Globala variabler
totalt = 0

for i in range(len(rawList)):
    test = rawList[i].split("x")    # Delar upp varje objekt i tre delar, x som delare
    bow = (int(test[0]) * int(test[1]) * int(test[2])) # Räknar ut arean för längd x bredd x 2 sidor
    temp1 = 0 # Sätter startvärde till 0
    temp2 = 0 # Sätter startvärde till 0
    if int(test[0]) > int(test[1]):
        temp1 = int(test[1])
        temp2 = int(test[0])
#        print("ifsats1 ger temp1 temp2", temp1, temp2)
    else:
        temp1 = int(test[0])
        temp2 = int(test[1])
#        print("elsesats1 ger temp1 temp2", temp1, temp2)

    if int(test[2]) < temp2:
        temp2 = int(test[2])
#        print("ifsats2 ger temp1 temp2", temp1, temp2)
    ribbon = temp1 + temp1 + temp2 + temp2
#    print("ribbon ger", ribbon)
    toti = ribbon + bow
#    print("toti ger", toti)
    totalt += toti
#    print("totalt nu", totalt)

print("Svaret blir: ", totalt) # Skriver ut svaret

"""
Svaret blev 3829537 vilket var för högt
"""
"""
Testfil =
4x23x21
22x29x19
bör ge:
4+4+21+21=50
4x23*21= 1932
22+22+19+19= 82
22*29*19 = 12122
=> 14.186

"""
