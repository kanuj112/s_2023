===============================
constructor :==================
===============================
1. A constructor is a special kind of method that Python calls when it 
instantiates an object using the definitions found in your class
2. The name of a constructor is always the same, __init__()
3. The constructor can accept arguments when necessary to create the object
4. When you create a class without a constructor, Python automatically creates a default constructor
for you that doesn’t do anything.
5. Every class must have a constructor, even if it simply relies on the default constructor. 
6. Constructor can be parameterized and non=parameterized as well. 
7. A constructor is a class function that begins with double underscore (__). 
8. The name of the constructor is always the same __init__()

========================
__init__ :
========================
"__init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts.
This method called when an object is created from the class and it allow the class to initialize the 
attributes of a class.

========================
self:
========================
In the init method, self refers to the newly created object; in other class methods, 
it refers to the instance whose method was called.

==============================
parameterized constructors:
==============================
1. The parameterized constructors are used to set custom value for instance variables
that can be used further in the application.
2. constructor with parameters is known as parameterized constructor.
==============================
class Student:  
    # Constructor = parameterized  
    def __init__(self, name):  
        print("This is parametrized constructor")  
        self.name = name  
    def show(self):  
        print("Hello",self.name)  
student = Student("irfan")  
student.show()  
op==>
This is parametrized constructor
Hello irfan
===============================
class Student:
    # Constructor = parameterized
    def __init__(self, name):
        print("This is parametrized constructor")
        self.anything = name
    def show(self):
        print("Hello",self.anything)
student = Student("irfan")
student.show()
# This is parametrized constructor
# Hello irfan
==============================
class Student:
    # Constructor = parameterized
    def __init__(self, name):
        print("This is parametrized constructor")
        self.name = name
    def show(self):
       print("Hello",self.name)
student = Student("irfan")
student.show()
#This is parametrized constructor
#Hello irfan
===============================
class Student:
    # Constructor = parameterized
    def __init__(self, name):
        print("This is parametrized constructor")
        self.name = name
    def show(self):
        print("Hello",name) #error
student = Student("irfan")
student.show()
#error  (NameError: name 'name' is not defined)
===============================
class Student:
    # Constructor = parameterized
    def __init__(self, name):
        print("This is parametrized constructor")
        self.name = name
        print(name)
        print(self.name)
    def show(self):
        print("Hello",name) #error
student = Student("irfan")
student.show()
# This is parametrized constructor
# irfan
# irfan
# NameError: name 'name' is not defined
=====================================
class Student:
    # Constructor = parameterized
    def __init__(self, name):
        print("This is parametrized constructor")
        self.name = name
        print(name)
        print(self.name)
    def show(self):
        print("Hello",self.name) #error
student = Student("irfan")
student.show()
# This is parametrized constructor
# irfan
# irfan
# Hello irfan
=====================================
class outer():
    def __init__(self,name):
        print("this is parametrised constructor")
        self.name = name

    def inner(self):
        print(self.name)
obj1 = outer("anuj") #parametrised constructor
obj1.inner()
#this is parametrised constructor
#anuj
=================================
class outer():
    def __init__(self,name):
        print("this is parametrised constructor")
        self.name = name

    def inner():
        print(self.name)
obj1 = outer("anuj") #parametrised constructor
obj1.inner()
# this is parametrised constructor
# TypeError: inner() takes 0 positional arguments but 1 was given
===============================
class outer():
    def __init__(self,name):
        print("this is parametrised constructor")
        self.name = name

    def inner(self):
        print(self.name)
obj1 = outer("anuj") #parametrised constructor
obj1.inner()
# this is parametrised constructor
# anuj
================================
class outer():
    def __init__(self,name):
        print("this is parametrised constructor")
        self.name = "aaa"

    def inner():
        print(self.name)
obj1 = outer("anuj") #parametrised constructor
obj1.inner()
#error  TypeError: inner() takes 0 positional arguments but 1 was given
===================================
class outer():
    def __init__(self,name):
        print("this is parametrised constructor")
        self.name = "aaa"
        print(name)
        print(self.name)

    def inner(self):
        print(self.name)
obj1 = outer("anuj") #parametrised constructor
obj1.inner()
# this is parametrised constructor
# anuj
# aaa
# aaa
========================================
Non Parameterized Constructor:
========================================
1. This constructor doesn’t accept any arguments.

class Student:  
    # Constructor = non parameterized  
    def __init__(self):  
        print("This is non parametrized constructor")  
    def show(self,name):  
        print("Hello",name)  
student = Student()  
student.show("irfan")  
op==>
This is non parametrized constructor
Hello irfan
========================================
class Student:
    # Constructor = non parameterized
    def __init__(self):
        print("This is non parametrized constructor")
    def show(self,abc):
        self.name = abc
        print("Hello",self.name)
student = Student()
student.show("irfan")
#This is non parametrized constructor
#Hello irfan
========================================
class Student:
    # Constructor = non parameterized
    def __init__(self):
        print("This is non parametrized constructor")
    def show(self,name):
        print("Hello",self.name) #(AttributeError: 'Student' object has no attribute 'name')
student = Student()
student.show("irfan")
#This is non parametrized constructor
#error
==========================================
When we do not declare a constructor:
====================================
class DemoClass:
    num = 101

    # a method
    def read_number(self):
        print(self.num)
# creating object of the class
obj = DemoClass()
# calling the instance method using the object obj
obj.read_number()
op==>101
===================================
class DemoClass:
    num = 101

    # a method
    def read_number():
        print(self.num)
# creating object of the class
obj = DemoClass()
# calling the instance method using the object obj
obj.read_number()
#TypeError: read_number() takes 0 positional arguments but 1 was given
==============================
class DemoClass:
   global num  #Global means it can be called with simply "num"
   num = 101
   def read_number(self):
        print(num)
# creating object of the class
obj = DemoClass()
# calling the instance method using the object obj
obj.read_number()
#101
============================
class DemoClass:
    global num  #Global means it can be called with simply "num"
    num = 101
    def read_number(self):
        print(num)
        print(self.num)
# creating object of the class
obj = DemoClass()
# calling the instance method using the object obj
obj.read_number()
#101
#AttributeError: 'DemoClass' object has no attribute 'num'
====================================
class DemoClass:
   global num
   num = 101
   def read_number(self,num):
       print(num)
       print(self.num)

obj = DemoClass()
obj.read_number(10)
#10
#error AttributeError: 'DemoClass' object has no attribute 'num'
====================================
class DemoClass:
   #global num
   num = 101
   def read_number(self,num):
       print(num)
       print(self.num)
obj = DemoClass()
obj.read_number(10)
#10
#101
===================================
class DemoClass:
    #global num
    num1 = 101
    def read_number(self,num):
        print(num)
        print(self.num1)
        #print(self.num) #error
obj = DemoClass()
obj.read_number(10)
# 10
# 101
====================================
class DemoClass:
    num = 101 #No global means it can be called with self.num

    # a method
    def read_number(self,num):
        print(self.num)
        print(num)
# creating object of the class
obj = DemoClass()
# calling the instance method using the object obj
obj.read_number(10)
#101
#10
===================================
When we declare a constructor:
===================================
class DemoClass:
    num = 101
    # non=parameterized constructor
    def __init__(self):
        self.num = 999
    # a method
    def read_number(self):
        print(self.num)
# creating object of the class
obj = DemoClass()
# calling the instance method using the object obj
obj.read_number()
op==>999
=====================================
class DemoClass:
    num = 101
    # non=parameterized constructor
    def __init__(self):
        print("aaa")
        #self.num = 999
    # a method
    def read_number(self):
        print(self.num)
# creating object of the class
obj = DemoClass()
# calling the instance method using the object obj
obj.read_number()
#aaa
#101
=====================================
class DemoClass:
    global num
    num = 101
    # non=parameterized constructor
    def __init__(self):
        self.num = 999
    # a method
    def read_number(self):
        print(num)
# creating object of the class
obj = DemoClass()
# calling the instance method using the object obj
obj.read_number()
#101
=====================================
class DemoClass:
    global num
    num = 101
    # non=parameterized constructor
    def __init__(self):
        self.num = 999
    # a method
    def read_number():
        print(num)
# creating object of the class
obj = DemoClass()
# calling the instance method using the object obj
obj.read_number()
#TypeError: read_number() takes 0 positional arguments but 1 was given
====================================
class DemoClass:
    global num
    num = 101
    # non=parameterized constructor
    def __init__(self):
        self.num = 999
    # a method
    def read_number(self,anything):
        self.abc = anything
        print(self.abc)
        print(self.num)
        print(num)
# creating object of the class
obj = DemoClass()
# calling the instance method using the object obj
obj.read_number(100)
#100
#999
#101
=====================================
class DemoClass:
    num = 101
    # non=parameterized constructor
    def __init__(self):
        self.num = 999
    # a method
    def read_number(self,num):
        print(self.num)
        print(num)
# creating object of the class
obj = DemoClass()
# calling the instance method using the object obj
obj.read_number(20)
#999
#20
=====================================
class DemoClass:
    global num
    num = 101
    # non=parameterized constructor
    def __init__(self):
        self.num = 999
    # a method
    def read_number(self,num):
        print(self.num)
        print(num)
# creating object of the class
obj = DemoClass()
# calling the instance method using the object obj
obj.read_number(20)
#999
#20
===============================
class DemoClass:
    num = 101
    def __init__(self):
        pass
        #self.num = 999
    def read_number(self,num):
        print(self.num)
        print(num)
obj = DemoClass()
obj.read_number(20)
#101
#20
=====================================
Parameterized constructor example:
=====================================
class DemoClass:
    num = 101
    # parameterized constructor
    def __init__(self, data):
        self.num = data
    # a method
    def read_number(self):
        print(self.num)
# creating object of the class
# this will invoke parameterized constructor
obj = DemoClass(55)
# calling the instance method using the object obj
obj.read_number()
# creating another object of the class
obj2 = DemoClass(66)
# calling the instance method using the object obj
obj2.read_number()
op==>
55
66
========================================
class DemoClass:
    num1 = 101
    # parameterized constructor
    def __init__(self, data):
        self.num = data
        #print(num1) error
        print(self.num1)
    # a method
    def read_number(self):
        print(self.num)
# creating object of the class
# this will invoke parameterized constructor
obj = DemoClass(55)
# calling the instance method using the object obj
obj.read_number()
# creating another object of the class
obj2 = DemoClass(66)
# calling the instance method using the object obj
obj2.read_number()
#101
#55
#101
#66
=============================
class DemoClass:
    num1 = 101
    # parameterized constructor
    def __init__(self, data):
        self.num = data
        print(self.num1)
        print(self.num)
    # a method
    def read_number(self):
        print(self.num)
obj = DemoClass(55)
obj.read_number()
obj2 = DemoClass(66)
obj2.read_number()
#101
#55
#55
#101
#66
#66
=============================
#non parametrised constructor

class outer():
    def __init__(self):
        print("this is non parametrised constructor")
        #self.name = name

    def inner(self,name):
        #print(self.name) #it will give error AttributeError: 'outer' object has no attribute 'name'
        print(name)

obj1 = outer() #non parametrised constructor
obj1.inner("anuj")
#this is non parametrised constructor
#anuj
===============================
class outer():
    def __init__(self,name):
        print("this is non parametrised constructor")
        self.name = name
    def inner(self,name):
        print(self.name) #it will give error AttributeError: 'outer' object has no attribute 'name'
        print(name)
obj1 = outer("anuj") #non parametrised constructor
obj1.inner("aannuujj")

#this is non parametrised constructor
#anuj
#aannuujj
===============================
class outer():
    def __init__(self,name):
        print("this is non parametrised constructor")
        self.abc = name

    def inner(self):
        print(self.abc)
        #print(name) #it will give error AttributeError: 'outer' object has no attribute 'name'
obj1 = outer("xdjcbnd") #non parametrised constructor
obj1.inner()
#this is non parametrised constructor
#xdjcbnd
===========================
class abc:
    def inner(self):
        print("abc")
    def inner1(self,name):
        print(name)

obj1 = abc()
obj1.inner()
obj1.inner1("anuj")
#abc
#anuj
==========================
class abc:
    def __init__(self,name):
        self.name = name
        print("name",name)

    def __init__(self,roll):
        self.roll = roll
        print("roll",roll)
obj = abc(101)
#roll 101
==================================
