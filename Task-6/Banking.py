# Theme= Basic modle demonstrating how netbanking works in a real-time project
#You can create your bank account with a unique user-id and deposit ,withdrawal, Balance enquiry and Accesing admin panel are the major features 
# Use '123' for admin login 


class Banking:
    def __init__(self):
        print(
            '_____________________________________________________________________WELOCOME TO HELLO BANK______________________________________________________________________')
        print()
        self.admin_login={'password':'123'}
        self.all = [{}]
        self.menu()

    def menu(self):
        while True:
            print('''Our banking services
                            1.New user registration 
                            2.Login into Netbanking
                            3.Contact Branch/Admin
                            4.Admin login
                    For New user press 1 , To login press 2, Contact Branch/Admin press 3, Admin Acess press 4 ''')
            n = input()
            if n == '1':
                self.register()
            elif n == '2':
                self.login()
            elif n == '3':
                self.branch()
            elif n == '4':
                self.admin()
            else:
                print('________________________________ERROR-505__________________________________ ')
                self.menu()

    def register(self):
        self.empdata = {}
        self.id = input('Enter your User-id ')
        for d in self.all:
            if self.id in d:
                print("Sorry user-id Unavailable , Create your user-id again ")
                self.con=True
                break

        else:
            while True:
                self.password = input('Enter your password')
                self.password_2 = input('Re-Enter your password')
                if self.password == self.password_2:
                    self.empdata[self.id] = self.password_2
                    self.empdata['Name'] = input('Enter your full name')
                    self.empdata['Mobile'] = input('Enter your mobile number')
                    self.empdata['Balance'] = 0
                    self.empdata['Cards']='N/A'
                    self.empdata['Loan']='N/A'
                    print(f"{self.empdata.get('Name')} has been registered successfully ")
                    self.all.append(self.empdata)
                    self.con=False
                    e=input('Press any key continue')
                    break
                else:
                    print("Wrong password please enter your password again and Re-Enter your password")
        if self.con:
            self.register()


    def login(self):
        id=input('Enter your user-id')
        password=input('Enter your password')
        for i in range(int(len(self.all))):
            if id in self.all[i]:
                if password==self.all[i].get(id):
                    print('_____________________Logged in succesfully________________')
                    print('''Our banking services
                            1.Show Balance 
                            2.Money withdrawal
                            3.Add money
                            4.Credit card/Debit Card
                            5.Loan 
                            6.Contact Branch
                    For Balance press 1 , To Withdrawal press 2, For Adding money pres 3,For credit card press 4, For loan press 5, To contact branch press 6 ''')
                    n=input()
                    if n=='1':
                        print(self.all[i].get('Balance'))
                        s=input('press any key to continue')
                        break
                    elif n=='2':
                        print(f"your Account Balance: {self.all[i].get('Balance')}")
                        w=int(input('Enter amount to withdrwala'))
                        if w < int(self.all[i].get('Balance')):
                            self.all[i]['Balance']=int(self.all[i].get('Balance'))-w
                            print('---------Amount Withcdrawal Succesfull------------------')
                            print(f"Remaining Balance = {self.all[i].get('Balance')}")
                            s=input('press any key to continue')
                            break
                        else:
                            print('---------------Insufficient Balance in your account----------------- ')
                            s=input('Press any key to continue')
                            break
                    elif n=='3':
                        print(f"your Account Balance: {self.all[i].get('Balance')}")
                        w=int(input('Enter amount to add into your account'))
                        self.all[i]['Balance']=int(self.all[i].get('Balance'))+w
                        print('---------Transaction Succesfull, Amount Succesfully deposited into your account------------------')
                        print(f"Updated  Balance = {self.all[i].get('Balance')}")
                        s=input('press any key to continue')
                        break
                    elif n=='4':
                        print(f"Your cards = {self.all[i].get('Cards')}")
                        print('To update or modify contact Hello Bank')
                        self.branch()
                        s=input('press any key to continue')
                        break
                    elif n=='5':
                        print(f"Your cards = {self.all[i].get('Loan')}")
                        print('To update or modify contact Hello Bank')
                        self.branch()
                        break
                    elif n=='6':
                        self.branch()
                        break
                    else:
                        print('          Invalid Option         ')
                        s=input('Press any key to continue')
                        break
                else:
                    print('--------------------Incorrect Password----------------------')
                    s=input('Press any key to continue')
                    break
        else:
            print('------------------------------------Invalid user-Id----------------------------------')
            s=input('Press any key to continue')





    def branch(self):
        print('''                                            HELLO BANK
                                             GHMC No 337, Svy No 92/1, 92/3 to 18, 123P & 124/1,
                                                        Vinayak Nagar, Gachibowli,
                                                        Hyderabad, Telangana 500032 
                                                            Phone:- 1800 10888
''')
        s=input('press any key to continue')
    
    def admin(self):
            print('------------------------------WELCOME TO ADMIN PANEL------------------------------------------')
            p=input('Enter password to access admin panel')
            if p == self.admin_login.get('password'):
                print('''Select options from dropdown
                                1.customer details by name  
                                2.All customer details 
                                3.Customer details with less minimal balance
                        For Customer details press 1 , To fetch all customers  press 2, TO filter press 3, ''')
                n = input()
                if n=='1':
                    x=input('Enter customer name')
                    for cs in self.all:
                        if x == cs.get('Name'):
                            print(cs)
                            print('-----------------Customer details fetched succesfully--------------- ')
                            s=input('press any key to continue')
                            break
                    else:
                        print('Customer with given name unavailable')
                        s=input('press any key to continue')
                elif n=='2':
                    for cs in self.all:
                        print(cs)
                        print('-----------------Customer details fetched succesfully--------------- ')
                        s=input('press any key to continue')
                            
                elif n=='3':
                    x=input('Enter the margin amount to fetch customers with less than that minimal amount ')
                    for cs in self.all:
                        if int(x)>int(cs.get('Balance')):
                            print(cs)
                    else :
                        print('-----------------Customer details fetched succesfully--------------- ')
                        s=input('press any key to continue')
            else:
                print('----------------------Invalid Password--------------------')
                s=input('press any key to continue')




                
s = Banking()


