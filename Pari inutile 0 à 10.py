import random


on=-1
while on!=1:
    x=int (input('entrez votre chiffre pour misez '))

    wow=[]    
    for i in range (0,10):
            wow.append (random.randint (1,10))

    x2=wow.pop(0)
    print (x2)
    if x!=x2:
        print ('vous avez perdu')

    else:
        print ('vous avez gagné')
        on=1
        input()
