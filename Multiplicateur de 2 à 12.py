print('/// Programme mutliplicateur de chiffre ///')
def multi(x):
    n=1
    for i in range (2,12) :
        n=n+1
        y=x*n
        print(y)

def calc():
    x=100
    while x>12:                             #entrer dans une boucle
        x=int(input('Entrez le multiplcateur (de 2 à 12) : '))
        multi(x)



calc()
