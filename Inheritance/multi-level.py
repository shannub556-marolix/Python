class Company:
    def equip(self):
        print('Laptop:- Macbook pro 2023-16/M2')

class Food(Company):
    def food(self):
        self.equip()
        print('Your food coupon will be having recharge of $3000')
    
class Employee(Food):
    def display(self):
        self.equip()
        self.food()
        print('myself shanmukha and i have access to acessories like' )

e=Employee()
e.equip()
e.display()
e.food()