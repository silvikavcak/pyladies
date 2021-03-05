# v centimetroch
# strana = input('Zadaj text:')  #string
# strana = int(input('Zadaj cislo:'))  #integer
strana = float(input('Zadaj cislo:'))  #floating number
pi = 3.1415926
strana_je_kladna = strana > 0
if strana_je_kladna:
    print ("Obsah stvorca je ", strana **2, "cm2")
    print ("Obvod stvorca je ", strana * 4, "cm")
    print ("Obsah kruhu je ", pi*(strana **2), "cm2")
    print ("Obvod kruhu je ", 2*pi*strana, "cm2")

else:
    print('Ale no, zadaj kladne cislicko.')