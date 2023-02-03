import csv
import os

os.environ["DJANGO_SETTINGS_MODULE"] = 'employees.settings'

import django
django.setup()

from employees_app.models import *


def load_all_companies_to_db():
    with open('data_csv/companies.csv', 'r') as fh:
        csv_companies = csv.DictReader(fh)

        for company in csv_companies:
            db_company = Company(
                                id = company['id'],
                                company_name = company['company_name'],
                                country = company['country'],
                                city = company['city'],
                                address=company['address'],
                                phone_num=company['phone_num'],
                                 )
            db_company.save()


def load_all_persons_to_db():
    with open('data_csv/persons.csv', 'r') as fh:
        csv_persons = csv.DictReader(fh)


        for person in csv_persons:
            db_person = Person(
                                 id = person['id'],
                                 first_name=person['first_name'],
                                 last_name=person['last_name'],
                                 personal_email=person['personal_email'],
                                 gender=person['gender'],
                                 birth_date=datetime.datetime.strptime(person['birth_date'], '%m/%d/%Y')
                                 )
            db_person.save()


def load_all_employees_to_db():
    with open('data_csv/employees.csv', 'r') as fh:
        csv_employees = csv.DictReader(fh)

        for employee in csv_employees:
            db_employee = Employee(
                                 id = employee['id'],
                                 person_id=employee['person_id'],
                                 company_id=employee['company_id'],
                                 job_title=employee['job_title'],
                                 is_current_job=employee['is_current_job'].capitalize(),
                                 company_email=employee['company_email']
                                 )
            db_employee.save()


def delete_all_persons_from_db():
    Person.objects.all().delete()


def delete_all_companies_from_db():
    Company.objects.all().delete()


def delete_all_employees_from_db():
    Employee.objects.all().delete()


def delete_all_object_from_db():
    delete_all_employees_from_db()
    delete_all_persons_from_db()
    delete_all_companies_from_db()


if __name__ == '__main__':
    load_all_companies_to_db()
    load_all_persons_to_db()
    load_all_employees_to_db()
    # delete_all_object_from_db()