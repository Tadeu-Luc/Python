print ("/// Prix d'envoi postale///")
a= int(input("Entrez poids en gramme de la lettre : "))


if(a>0)and(a<20):
    
    print ('Cela fera 0.53 euros pour un envoi')
    
elif (a>=20)and (a<50):
    
    print ('Cela fera 0.70 euros pour un envoi')
    
elif (a>=50):
    
    print ('Cela fera 1.10 euros pour un envoi')

    
else:
    print ('error system')
