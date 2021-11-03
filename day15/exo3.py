from datetime import datetime
given_date = "(2020,2,25)"
print(given_date)
asked_date=datetime.strptime(given_date, '%d %m %y %H:%M:%S')
print(asked_date)