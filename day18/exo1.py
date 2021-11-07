import pandas as pd 
auto = pd.read_csv("Automobile_data.csv")
#auto.count(axis=0, level= "company")
print(auto["company"].value_counts())