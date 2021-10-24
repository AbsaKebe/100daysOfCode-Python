#1ere méthode
a=range(2,102,2)
resultat=[]
for x in a: 
    resultat.append(x)
print(resultat)

#2e méthode
a=range(1,102)
resultat=[]
for x in a:
    if x%2==0:
        resultat.append(x)
print(resultat)