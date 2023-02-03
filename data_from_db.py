import csv
import os

from django.db.models import Count

os.environ["DJANGO_SETTINGS_MODULE"] = 'employees.settings'

import django
django.setup()

from employees_app.models import *


def get_person_name_by_id(person_id: int) -> str:
    """
    Given person id, return string that represents person full name
    :param person_id:
    :return:
    """
    person = Person.objects.get(id = person_id)
    return f"{person.first_name} {person.last_name}"


def get_people_by_age(age: int) -> list[Person]:
    """
    Given age in years, return list of persons of this age
    :param age:
    :return:
    """
    # if today is 2/02/2023 , age = 10 years old: 2/02/2013 > birth_date < 2/02/2014
    date_now = datetime.datetime.utcnow().date()
    date_from = datetime.date(year=date_now.year - age-1, month=date_now.month, day=date_now.day)
    date_till = datetime.date(year=date_now.year - age, month=date_now.month, day=date_now.day)


    all_persons = Person.objects.all().filter(birth_date__gt=date_from,birth_date__lt=date_till)
    # print(f"date_from: {date_from} , date_till : {date_till}\n")



    return all_persons


def get_people_cnt_by_gender(gender: str) -> list[Person]:
    """
    Given the gender, return list of people of this gender
    :param gender:
    :return:
    """
    return Person.objects.all().filter(gender__iexact=gender)


def get_companies_by_country(country: str) -> list[str]:
    """
    Given country name, return list of companies' names in this country
    :param country:
    :return:
    """
    return Company.objects.all().filter(country__iexact = country)


def get_company_employees(company_id: int, current_only: bool) -> list[Person]:
    """
    Given company id, return list of persons who work(ed) for this company
    :param company_id:
    :param current_only: if True, return only people who are currently work in the company
    :return:
    """
    if current_only:
        return Person.objects.filter(id__in=Company.objects.get(id=1).employee_set.filter(is_current_job=True).values_list('person_id'))

    return Person.objects.filter(id__in=Company.objects.get(id=1).employee_set.all().values_list('person_id'))


def get_person_jobs(person_id: int) -> list[dict[str, str]]:
    """
    Given person_id, return list of dictionaries that map from company name to job title
    :param person_id:
    :return:
    """
    ret_val = []
    # emp = Company.objects.values('company_name').annotate(job_title='employeess__job_title')
    req_comp_title = Company.objects.filter(employee__person__exact=person_id).values('company_name','employee__job_title')
    for req in req_comp_title:
        ret_val.append({req['company_name'] : req['employee__job_title']})
    return ret_val


if __name__ == '__main__':

    # print(get_people_cnt_by_gender(gender='male'))

    print(get_people_by_age(age=38))




