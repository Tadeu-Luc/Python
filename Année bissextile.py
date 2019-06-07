année= int(input("entrez l'année pour savoir si elle est bisextile ? "))


if (année % 4 == 0): 
    if (année % 100 == 0): 
        if (année % 400 == 0): 
            bissextile = "est" 
        else: 
            bissextile = "n'est pas" 
    else: 
        bissextile = "est" 
else: 
    bissextile = "n'est pas" 

print (année,bissextile,"une année bissextile")
       
    
