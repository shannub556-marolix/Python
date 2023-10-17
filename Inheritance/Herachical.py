class Company:
    def equip(self):
        print('Welcome to marolix')


class laptop(Company):
    def lap(self):
        self.equip()
        print('Laptop:- Macbook pro 2023-16/M2')


class bonus(Company):
    def bonus(self):
        self.equip()
        print('Your bonus will be $35k per annum')


c = laptop()
c1 = bonus()
c.lap()
c1.bonus()