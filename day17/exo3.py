import pandas as pd
auto = pd.read_csv("Automobile_data.csv")
auto = auto.groupby(['company']).get_group("toyota")
print(auto)