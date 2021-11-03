from datetime import datetime
given_date = datetime(2020, 2, 25)
print(given_date)
asked_date=datetime.strftime(given_date, '%A %d %B %Y')
print(asked_date)