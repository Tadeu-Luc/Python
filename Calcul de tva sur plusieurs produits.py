import random

#prg
nbliste=int(input('Entrez le nombre de valeur que vous voulez passer aux prix toutes taxes comprises : '))
prixht=[random.randrange(0,1) for i in range(nbliste)]
prixttc=[random.randrange(0,1) for i in range(nbliste)]
x=0
tax=0
cpt=0


while x==0:
    if (cpt)<(nbliste):
        tax=float(input('Entrez la taxe à appliquer entre 2.10% et 20%: '))
        prixht[cpt]=tax
        if tax <= 20 :
            print ('la tax est de '+ str(tax)+' et le prix ht est de '+ str (prixht[cpt]))
            prixttc[cpt]=float(prixht[cpt]*(tax/100))
            print (prixttc)

        else :
            while (tax)>20:
                print ('vous avez fait une erreur sur la taxe veuillez ressayer ')
                tax=float(input('entrez la taxe à appliquer entre 2.10% et 20%: '))
                prixttc[cpt]=float (prixht[cpt]*(tax/100))
                prixht[cpt]=tax

                        
    else:
        x=1

        
    print ('les prix hors taxe que vous avez renseigner sont :',(prixht))
    print ('et la conversion')
    print ('les prix convertis donnent', (prixttc))      
    cpt=cpt+1

            
    
