from random import randrange
tah_pocitaca = randrange(3)
tah_hraca = str(input('Zadaj tah: '))

# assigns a string to the randomly generated number
if tah_pocitaca == 0:
    tah_pocitaca = 'kamen'
elif tah_pocitaca == 1:
    tah_pocitaca = 'papier'
else:
    tah_pocitaca = 'noznice'
print('Tah pocitaca: ', tah_pocitaca)

#decides if the player wins or loses the game
if tah_hraca == 'kamen':
    if tah_pocitaca == 'kamen':
        print('Remiza!')
    elif tah_pocitaca == 'papier':
        print('Prehral si!')
    elif tah_pocitaca == 'noznice':
        print ('Vyhral si!')
elif tah_hraca == 'papier':
    if tah_pocitaca == 'papier':
        print('Remiza!')
    elif tah_pocitaca == 'noznice':
        print('Prehral si!')
    elif tah_pocitaca == 'kamen':
        print ('Vyhral si!')
elif tah_hraca == 'noznice':
    if tah_pocitaca == 'noznice':
        print('Remiza!')
    elif tah_pocitaca == 'kamen':
        print('Prehral si!')
    elif tah_pocitaca == 'papier':
        print ('Vyhral si!')
else:
    print('Prepac, poznam iba tieto tri slova : kamen, papier a noznice. Skusis to prosim znova?')