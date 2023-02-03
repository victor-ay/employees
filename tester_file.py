import csv
import datetime
import re

# t = '+972-54-18'

# print(re.findall('[0-9\-\+]',t))

# max_age = 10
#
# date_now = datetime.datetime.now().date()
# year_min = date_now.year - max_age
#
# date_min = datetime.date(year=year_min,month=date_now.month, day=date_now.day)
#
# print(date_min)

# with open('data_csv/companies.csv', 'r') as fh:
#     comp = csv.DictReader(fh,fieldnames=
#                    ['id','company_name','country','city','address','phone_num'])
#
#     for elem in comp:
#         print(elem['id'],elem['company_name'],elem['country'],elem['address'],elem['phone_num'])

with open('data_csv/persons.csv', 'r') as fh:
    csv_persons = csv.DictReader(fh, fieldnames=
    ['id', 'first_name', 'last_name', 'personal_email', 'gender', 'birth_date'])

    for person in csv_persons:
        print(person['id'],person['first_name'],
                             person['last_name'],
                             person['personal_email'],
                             person['gender'],
                             person['birth_date'],
              datetime.datetime.strptime(person['birth_date'], '%m/%d/%Y')
)

print( datetime.datetime.strptime('11/24/1990', '%m/%d/%Y'))

x = ''.ca