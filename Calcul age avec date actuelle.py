import datetime

date = datetime.datetime.now()
actuel=date.year

a= int (input('entrez votre année de naissance :'))

rep= (actuel)-(a)

print ('vous avez '+ str(rep) + ' ans')
