import pandas as pd
GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}

japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}

Allemand = pd.DataFrame(GermanCars)
Japonais = pd.DataFrame(japaneseCars)
pays = pd.concat([Allemand,Japonais], keys=['Allemand', 'Japonais'])
print(pays)