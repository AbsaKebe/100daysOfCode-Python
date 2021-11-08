import pandas as pd
auto=pd.read_csv("Automobile_data.csv")
auto=auto.sort_values('price', ascending =False)
print(auto)