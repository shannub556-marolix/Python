class Company:
    def equip(self):
        print('Laptop:- Macbook pro 2023-16/M2')

class Employee(Company):
    def display(self):
        self.equip()
        print('myself shanmukha and i have access to acessories like' )

e=Employee()
e.equip()
e.display()