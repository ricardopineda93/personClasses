from datetime import datetime, date
from pprint import pprint

class Person:
    def __init__(self, first_name, last_name, DOB, occupation,
                 gender, middle_name=''):
        self.first_name= first_name.title()
        self.middle_name = middle_name.title()
        self.last_name= last_name.title()
        self.DOB= datetime.strptime(DOB, '%m/%d/%Y').date()
        self.age= self.get_age()
        self.occupation = occupation.title()
        self.gender= gender.title()
        self.languages = []
        self.salary = 0
        self.tax_bracket = self.get_tax_bracket()

    def full_name(self):
        return '{} {} {}'.format(self.first_name, self.middle_name, self.last_name) if self.middle_name!='' \
            else '{} {}'.format(self.first_name, self.last_name)

    def get_age(self):
        today = date.today()
        return today.year - self.DOB.year - ((today.month, today.day) < (self.DOB.month, self.DOB.day))

    def add_language(self, *languages):
        [self.languages.append(languages) for languages in languages]

    def get_tax_bracket(self):
        if self.salary < 50000:
            return 0.25
        elif self.salary <  75000:
            return 0.34
        elif self.salary < 99999:
            return 0.37
        elif self.salary > 100000:
            return 0.40

    @staticmethod
    def is_adult(age):
        return True if age>=18 else False

    @staticmethod
    def yearly_tax_on_salary(salary, tax_bracket):
        return salary * tax_bracket

    @staticmethod
    def take_home_salary(salary, taxes_paid):
        return salary - taxes_paid

    @staticmethod
    def print_profile(obj):
        pprint(obj.__dict__, indent=2)


joel = Person(first_name='Joel', last_name='Dominguez', occupation='Salsa Instructor',
              gender='Male', DOB= '09/07/1963')

jake = Person(first_name='Jacob', last_name='Rayfin', middle_name='Cristian',
              occupation= 'JavaScript Junior Developer', gender='Male', DOB='11/12/1993')

mishka = Person(first_name='Mishka', last_name='Laurenti', occupation='Uber Driver',
                gender='Female', DOB= '03/14/1997')


def who_is_oldest(*obj):
    for o in obj:
        if o.age == max(obj.age for obj in obj):
            return '{} {}'.format(o.first_name, 'is oldest.')
