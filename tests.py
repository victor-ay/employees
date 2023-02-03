import datetime

date_now = datetime.datetime.utcnow().date()
date_10_years = datetime.date(year=date_now.year-10,month=date_now.month,day=date_now.day)
print(date_10_years)