#1e méthode 
import random
des=[1,2,3,4,5,6]
for i in des:
    lancers=random.choice(des)
    print(lancers)

#2e méthode 
lancers = []
for _ in range(6):
    lancers.append(random.choice(range(1,7)))
print(lancers)