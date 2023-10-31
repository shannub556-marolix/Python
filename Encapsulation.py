class Manager:
    def __init__(self):
        self.employee_name='shanmukha'
        self._salary=25000
        self.__experience='2.5-years'

class Emp(Manager):
    def salary_details(self):
        print(self._salary)
    def name(self):
        print(self.employee_name)

m=Manager()
print('Acessing private,public,protected variables from parent class')
print(m.employee_name)
print(m._salary)
print(m._Manager__experience)

e=Emp()
print('accesing protcted and public variables in child class')
print(e._salary)
print(e.employee_name)
print('accesing protcted and public variables in child class by method')
e.salary_details()
e.name()
