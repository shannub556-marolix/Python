print('-----------------------------------------------------Welcome to Hosipital management------------------------------------------------------')

class Hospital:
    def __init__(self):
        print(
            '_____________________________________________________________________WELOCOME TO Apollo Hospital______________________________________________________________________')
        print()
        self.all = [{}]
        self.menu()

    def menu(self):
        while True:
            print('''Our services
                            1.Patient registration 
                            2.Get all patient details 
                            3.Search Patient by id
                            4.Delete patient details by id
                            5.update patient details by id
                    For Registartion press 1 , To get all patient details press 2, Fetch patient details press 3, Delete Patient press 4, Update Patient details press 5 ''')
            n = input()
            if n == '1':
                self.register()
            elif n == '2':
                self.all_patient()
            elif n == '3':
                self.search()
            elif n == '4':
                self.delete()
            elif n == '5':
                self.update()
            else:
                print('________________________________ERROR-505__________________________________ ')
                s=input('press any key to continue')
                

    def register(self):
        self.empdata = {}
        self.id = input('Create your Patient-id ')
        for d in self.all:
            if self.id == d.get('id'):
                print("Sorry user-id Unavailable , Create your user-id again ")
                self.con=True
                break

        else:
            self.empdata['id'] = self.id        
            self.empdata['Name'] = input('Enter your full name')
            self.empdata['Mobile'] = input('Enter your mobile number')
            self.empdata['Age'] = input('Enter your Age')
            self.empdata['Gender']=input('Enter your Gender M/F')
            self.empdata['Health-issue']=input('Enter your issue')
            print(f"{self.empdata.get('Name')} has been registered successfully ")
            self.all.append(self.empdata)
            self.con=False
            e=input('Press any key continue')
        if self.con:
            self.register()                    
            


    def all_patient(self):
        for d in self.all:
            print(d.items())
        else:
            print('-----------------Patient details fetched succesfully--------------- ')
            s=input('press any key to continue')
            
                        
        


    def search(self):
        x=input('Enter the id of patient that you want to search')
        for d in self.all:
            if x == d.get('id'):
                print(d.items())
                print('-----------------Patient details fetched succesfully--------------- ')
                s=input('press any key to continue')
                break
        else:
            print('Patient with given id not found')
            s=input('press any key to continue')


    def delete(self):
        x=input('Enter the id of patient that you want to delete')
        for d in range(int(len(self.all))):
            if x == (self.all[d]).get('id'):
                self.all.pop(d)
                print('-----------------Patient details deleted succesfully--------------- ')
                s=input('press any key to continue')
                break
        else:
            print('Patient with given id not found')
            s=input('press any key to continue')


    def update(self):
        x=input('Enter the id of patient that you want to update')
        for d in range(int(len(self.all))):
            if x == (self.all[d]).get('id'):
                print('''Select option to update that paticular details of a patient
                            1.Name 
                            2.Age 
                            3.Gender
                            4.Mobile
                            5.Health issue
                    For Name press 1 , To update age press 2, Update Gender press 3, Update mobile press 4, Update Health Diagnotics press 5 ''')
                n=input()
                if n=='1':
                    self.all[d]['Name']=input('Enter your updated Name')
                elif n=='2':
                    self.all[d]['Age']=input('Enter your updated Age')
                elif n=='3':
                    self.all[d]['Gender']=input('Enter your updated Gender')
                elif n=='4':
                    self.all[d]['Mobile']=input('Enter your updated mobile number')
                elif n=='5':
                    self.all[d]['Health-issue']=input('Enter your updated Health-issue')
                else:
                    print('________________________________ERROR-505__________________________________ ')
                    s=input('press any key to continue')
                    break
                print('-----------------Patient details deleted succesfully--------------- ')
                s=input('press any key to continue')
                break
        else:
            print('Patient with given id not found')
            s=input('press any key to continue')



s=Hospital()