import pandas as pd
auto = pd.read_csv("Automobile_data.csv")
#auto = auto.max(['company']).get_group('volvo')
auto = auto.groupby(['company'])
auto = auto['price'].max()
print(auto)