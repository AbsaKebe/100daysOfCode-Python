import pandas as pd 
Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
prix = pd.DataFrame(Car_Price)
nbchv = pd.DataFrame(car_Horsepower)
fusion = prix.merge(nbchv, on="Company")
print(fusion)
