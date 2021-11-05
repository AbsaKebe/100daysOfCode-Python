import pandas as pd
auto = pd.read_csv("Automobile_data.csv")
auto = auto[["company = toyota"]]
print(auto.head())