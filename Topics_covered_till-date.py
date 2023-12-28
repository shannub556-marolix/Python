'''
what is python
who discovered python
mostly which companies use python
features of python 
    easy to learn
    free and opensource
    high level programming language
    platform independent
    dynamically typed
    interpreted language
    extension library
identifiers rules
    cannot start with number
    special characters not allowec except '_'
    keywords cannot be used as identifiers
Datatypes
    integer,boolen,float,complex
    string,list,set,tuple,dictonary
operatots
    arthematic operators
    relational operators
    logical operators
input/output
conditional statements
iterative statements
    for loop 
    while loop
github and gitbash
    push to origin main and to edit files in same repsository
string
    indexing, slicing
    in, not in (operator)
    replace method
    split method
    len method
    adding two strings(+), string replication(*)
    strip method
    comparing two strings
    find method
    index method
    join method
    startswith()
    endswith()
    Case Convertions
        Upper method
        lower method
        title method
        captialize method
        swap case method
    isalnum() 
    isalpha()
    isdigit()
    islowe()
    isupper()
    isspace()
list
    list declaration, and creation
    eval input method
    accesing elements in a list
    replacing a element (indexing)
    while and for loop
    len 
    count
    index method
    append method
    insert method
    extend method
    pop method
    remove method
    reverse method
    sort method(natural order)
    aliasing and cloning of list (temporary variable concept)
    mathematical operations on list
        list replication(*)
        list concatination(+)
    comparing list objects (==,>,<,!=)
    membership operator
    clear method(it will reomve all elements from list in existing location)
    nested list (a list inside a list)
    list comprehension (simplest form of syntax in list, terinary operator)
    removing duplicates in a given list
    creating a list using for loop
tuple
    accesing elements in tuple(index,slicing)
    len method
    sort method
    count method
    index method
    min method
    tuple comprehension
dictonary
    add items in a dictonary
    accesing items in dictonary
        dictonary.items() , to get all items in dictonary
        dictonary.keys() , to get all keys in dictonary
        dictonary.values(), to get all values in dictonary
        dictonary[key] , to get value assigned to that key in dictonary
    del dictonary[key] , to delete that given key and value
    del dictonary , it will delete entire dictonary
    dictonary.clear() , it delete items in dictonary
    get method , to get value of given key
    pop method , it will remove tha key value pair and return that value
    popitem method, it removes last key value pair and return's it in the form of tuple
    

Functions
    how to create a function
    Advantages of function
    Types of arguments
        positonal arguments
        keyword arguments
        Default arguments (giving a default value for a positional arguments)
        variable length arguments
        variable length keyword arguments
    local and global variable 
recursions
lamda Functions
filter function
map function
reduce Function
nested function 
modules in python
membership aliasing 
math module
    sqrt() 
    ceil() 
    floor()
packages in python 
    
oops 
    Introduction to oops concept
        what is class and objects
        how to define class 
        how to create objects
        variables and methods in oops
        reference  variable 
    constructor (__init__)
        what is constructor
        why and what happens when we call constructor
    types of variable
        instance variable = variable which are intialized at the time of object creation   
            how to declare and in how many ways we can declare   
            how to delete 
            how to access and how to modify
        static/class variable= values which remains same from object to object are called static or class variable
            how to declare and in how many ways we can declare   
            how to delete 
            how to access and how to modify
        local variable = variable which are declared inside methods and that are deleted after execution 
            how to declare and in how many ways we can do that
            how to delete 
            where can we acces and modify
    types of methods 
        instance method= we declare instance variables iniside method and if we pass first variable as self 
        class method = we declare static variable inside method and pass cls as first variable and will decorate that method with classmethod using decorator
        static method = we wont pass cls or slef as first variable and we decorate that method with static method using decoarter
    inner class 
            similar to that nested loops and all , it is same it will be having class and inside we will be having another class 
    Difference b/w Constructor and method
        
    Inheritance = 
        types of Inheritance
            Single Inheritance
            multiple Inheritance
            multi-level Inheritance
            herichical Inheritance
            hybrid Inheritance(combination of single , multiple, and multilevel)
            cycle Inheritance(But python does'nt support this type)

        super method  in Inheritance
            #We can acess parent class constructor,methods and attributes from child class by using an inbuilt method called super()
                #imp points about super():
                # case1:from child class we are not allowed to access parent class instance variables by using super(),compulasary we shud use self only
                # but we can access parent class static variables by using super()
                #
                # case2:from child class constructor and instance method,we can access parent class constucter,instance method,static method and class method by using super()
                #
                #case3:from child,class method we cannot access parent class instance methods and constructors by using super() directly(but indirectly possible).but we can access parent class static and class methods
                #       In special case we can access them by using this synatx: super(child-class_name,cls).m2(cls)
                #
                #case4:from child class, static method we cannot access anything by using
                #       but in special case we can access static method by using this syntax: super(child-class_name,child-class_name).m3()
                
    Polymorphism
        Executing the same thing in different way like, '+' is concatination in terms of string and addition interms of integers
        Overloading : Python supports Operator Overloading('+')
        Overridding : python supports Method and constructor Overridding 
    
    Abstarction 
        Hiding the implimentation part and showing only the required essential part is known as Abstarction
        A class having one or more abstarct method then we call it as abstract class 
        From the Module abc, we need to import ABC,abstractmethod and inherit the class with ABC and decorate the method with @abstractmethod , then it becomes abstarct class
        and we can't create object for abstarct class 
    
    Encapsulation
        Restricting the access , to prevent accidental damage of data by making it has private, public, protected
        public: access anywhere inside and outside the class without having any restrictions 
        protected(_variable) : can be accessed within the class and the derived class and outside of that class and derived class 
        private(__variable) : can be accessed within class and can't be accessed anywhere in the class ,child class or outside the class
                  *But in a alternative way we can access private variables outside the class by "syntax: ref-obj._class-name__variable-name"
        
Exception handling 
    exceptions are nothing but errors, which is an unexpected event that occurs during the programm execution
    exceptions can be handled by using these two machenism
    1.logial implementation
    2.try except block
    3.finally block

##############DJANGO
what is django
how does it works
MVT architecture(model,view,template)
    Model: Models.py file contains the database connections , where we store and retrive data from database 
    Views: views.py file contains the functionalities and the logic, which is an API(application progarmm interface)
    Template: templates.py contains the templates
creating project and application in django
rendering html file and accesing that data admin panel
saving data in database and retriving it from database
Adding multiple paths and html pages to our project
Http methods
    GET-retrive/Read
    POST-creating
    Update/Patch-updating
    delete-delete
Http Response status code
    Informational responses (100-199)
    Successful responses (200-299)
    Redirection messages (300-399)
    Client error responses (400-499)
    Server error responses (500-599)
Serilizers 
REST API(Django restframework)
Requests and Responses 
CURD(create, update, Read, Delete) operations 
Creating users and generating tokens for that user
Authentication and Authirization (Token Based Authentication)
Installing and initializing Postgresql

        


'''