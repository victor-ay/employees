import datetime

from django.core.validators import *
from django.db import models


def person_min_birth_date() -> datetime.datetime.date:
    max_age = 120
    date_now = datetime.datetime.now().date()
    year_min = date_now.year - max_age
    date_min = datetime.date(year=year_min, month=date_now.month, day=date_now.day)
    return date_min


def person_max_birth_date() -> datetime.datetime.date:
    min_age = 14
    date_now = datetime.datetime.now().date()
    year_min = date_now.year - min_age
    date_max = datetime.date(year=year_min, month=date_now.month, day=date_now.day)
    return date_max


class Person(models.Model):
    first_name = models.CharField(db_column='first_name', max_length=256, null=False, blank=False)
    last_name = models.CharField(db_column='last_name', max_length=256, null=False, blank=False)
    personal_email = models.EmailField(db_column='personal_email', max_length=256, null=False, blank=False)
    gender = models.CharField(db_column='gender', max_length=256, null=False, blank=False,
                              choices=[('Male','Male'),
                                       ('Female','Female'),
                                       ('Agender','Agender'),
                                       ('Bigender','Bigender'),
                                       ('Polygender','Polygender'),
                                       ('Genderfluid','Genderfluid')
                                       ]
                              )
    birth_date = models.DateField(db_column='birth_date', null=False, blank=False,
                                  validators=[
                                      MinValueValidator(person_min_birth_date),
                                      MaxValueValidator(person_max_birth_date)
                                  ])


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'persons'


class Company(models.Model):
    company_name = models.CharField(db_column='company_name', max_length=256, null=False, blank=False)
    country = models.CharField(db_column='country', max_length=256, null=False, blank=False)
    city = models.CharField(db_column='city', max_length=256, null=False, blank=False)
    address = models.CharField(db_column='address', max_length=1024, null=False, blank=False)
    phone_num = models.CharField(db_column='phone_num', max_length=32, null=False, blank=False,
                                 validators=[RegexValidator(regex='[0-9\-\+]')])

    persons = models.ManyToManyField(Person, through='Employee')

    def __str__(self):
        return f"{self.company_name}"

    class Meta:
        db_table = 'companies'


class Employee(models.Model):

    job_title = models.CharField(db_column='job_title', max_length=256, null=False, blank=False)
    is_current_job = models.BooleanField(db_column='is_current_job', null=False, blank=False)
    company_email = models.EmailField(db_column='company_email', max_length=256, null=True, blank=True)
    person = models.ForeignKey(Person, on_delete=models.RESTRICT)
    company = models.ForeignKey(Company, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.person}, {self.is_current_job}"
    class Meta:
        db_table = 'employees'