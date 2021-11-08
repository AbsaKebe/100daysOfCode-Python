import pandas as pd
auto=pd.read_csv("Automobile_data.csv")
auto=auto.groupby('company')
auto= auto['average-mileage'].mean()
print(auto)
