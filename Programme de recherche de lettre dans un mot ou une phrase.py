
print('/// Programme de recherche de lettre dans un mot ou une phrase///')
e=input('Entrez la lettre recherchée : ') 
x=input('Entrez un mot pour savoir le nombre de '+str(e)+' dedans : ') 
if x.count('e')>=1:
    x=x.count('e')
    print ('votre mot comporte '+str(x)+' lettre(s) e')
else:
    print ('il n\'y a pas de  '+str(e)+'  dans ce mot')
