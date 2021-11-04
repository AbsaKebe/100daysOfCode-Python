from datetime import datetime
date_1 = datetime(2021, 10, 20)
date_2 = datetime(2021, 11, 4)
nbofdays=None

if date_2>date_1:
    nbofdays=date_2 - date_1
else:
    nbofdays=date_1 - date_2
    
print(nbofdays.days)