from random import randrange
tvar = randrange(3)

if tvar == 0:
    tvar = 'trojuholnik'
elif tvar == 1:
    tvar = 'stvorec'
else:
    tvar = 'koliesko'
print(tvar)