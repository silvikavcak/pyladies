# program counts cube surface and volume in centimeters

strana = 2852    #integer
strana_je_kladna = strana >= 0    #positive integer

if strana_je_kladna:
    print ("Povrch krychle je ", (strana **2)*6 , "cm2")    #counts cube surface
    print ("Objem krychle je ", strana ** 3, "cm3")    #counts cube volume
    
else:
    print('Ale no, zadaj kladne cislicko.')