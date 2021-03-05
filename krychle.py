# program counts cube surface and volume in centimeters

strana = float(input('Zadaj cislo:'))  #floating number
strana_je_kladna = strana >= 0

if strana_je_kladna:
    print ("Povrch krychle je ", (strana **2)*6 , "cm2")
    print ("Objem krychle je ", strana ** 3, "cm3")
    
else:
    print('Ale no, zadaj kladne cislicko.')