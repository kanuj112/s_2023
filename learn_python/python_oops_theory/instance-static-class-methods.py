=========================================
==========Instance methods===============
=========================================
1. Instance methods are the most common type of methods in Python classes. These are so called because 
they can access unique data of their instance. If you have two objects each created from a car class, 
then they each may have different properties. They may have different colors, engine sizes, seats, and so on.
2. Instance methods must have self as a parameter, but you don’t need to pass this in every time. 
Self is another Python special term. Inside any instance method, you can use self to access any data or 
methods that may reside in your class. You won’t be able to access them without going through self.
3. Finally, as instance methods are the most common, there’s no decorator needed. Any method you 
create will automatically be created as an instance method, unless you tell Python otherwise.
=======================================
class DecoratorExample:
  """ Example Class """
  def __init__(self):
    """ Example Setup """
    print('Hello, World!')
    self.name = 'Decorator_Example'

  def example_function(self):
    """ This method is an instance method! """
    print('I\'m an instance method!')
    print('My name is ' + self.name)
de = DecoratorExample()
de.example_function()
#Hello, World!
#I'm an instance method!
#My name is Decorator_Example
==================================
class DecoratorExample:
    def __init__(self,aaa):
        print('Hello, World!')
        self.name = aaa
    def example_function(self):
        print('I\'m an instance method!')
        print('My name is ' + self.name)
de = DecoratorExample("fjghufhgtuir")
de.example_function()
# Hello, World!
# I'm an instance method!
# My name is fjghufhgtuir
================================
class DecoratorExample:
    def __init__(self):
        print('Hello, World!')
        self.name = 'Decorator_Example'
    def example_function(self):
        print('I\'m an instance method!')
        print('My name is ' + self.name)
de = DecoratorExample()
de.example_function()
#Hello, World!
#I'm an instance method!
#My name is Decorator_Example

========================================
===========class method=================
========================================
1. the classmethod() method returns a class method for the given function.
2. The syntax of classmethod() method is: classmethod(function)
@classmethod
def func(cls, args...)
3. A class method is a method that is bound to a class rather than its object. 
It doesn't require creation of a class instance, much like staticmethod.
4. Class method works with the class since its parameter is always the class itself.
5. The class method can be called both by the class and its object.
Class.classmethod()
Or even
Class().classmethod()
==================================
6. Create class method using classmethod()
class Person:
    age = 25
    def printAge(cls):
        print('The age is:', cls.age)
Person.printAge = classmethod(Person.printAge)
Person.printAge()
#The age is: 25
=================================
class Person:
    age = 25
    def printAge(aaa):
        print('The age is:', aaa.age)
Person.printAge = classmethod(Person.printAge)
Person.printAge()
#25


==============================
class Person:
    age = 25
    def printAge(self):
        print('The age is:', self.age)
Person.printAge = classmethod(Person.printAge)
Person.printAge()
#The age is: 25
================================
class Person:
    age = 25
    def printAge(cls):
        print('The age is:', cls.age)

    def printAge1(cls):
        print('The age is Printage1:', cls.age)
Person.printAge1 = classmethod(Person.printAge1)
Person.printAge1()
#The age is Printage1: 25
=================================
class Person:
    age = 25
    def printAge(cls):
        print('The age is:', cls.age)

    def printAge(cls):
        print('The age is Printage1:', cls.age)
Person.printAge = classmethod(Person.printAge)
Person.printAge()
#The age is Printage1: 25




==================================
class Person:
    age = 25
    def printAge(cls):
        print('The age is:', cls.age)

    def printAge1(cls):
        print('The age is Printage1:', cls.age)
Person.printAge1 = classmethod(Person.printAge1)
Person.printAge1()
Person.printAge = classmethod(Person.printAge)
Person.printAge()

#The age is Printage1: 25
#The age is: 25


=================================
7. A class method receives the class as implicit first argument, just like an instance 
method receives the instance

class C(object):
    @classmethod
    def fun(cls, arg1, arg2, ...):
       ....
fun: function that needs to be converted into a class method
returns: a class method for function.

8. It can modify a class state that would apply across all the instances of the class. 
=============================
1. Class methods are the third and final OOP method type to know. Class methods know about their class. 
2. They can’t access specific instance data, but they can call other static methods.
3. Class methods don’t need self as an argument, but they do need a parameter called cls. 
4. This stands for class, and like self, gets automatically passed in by Python.
5. Class methods are created using the @classmethod decorator.
=============================
class DecoratorExample:
    def __init__(fvgxfd):
        print('Hello, World!')
    @classmethod
    def example_function(abc):
        print('I\'m a class method!')
        abc.some_other_function()
    @staticmethod
    def some_other_function():
        print('Hello!')
de = DecoratorExample()
de.example_function()
de.some_other_function()

#Hello, World!
#I'm a class method!
#Hello!
#Hello!
=============================
class DecoratorExample:
    def __init__(self):  # either self or anything bdvhfdvghd, if both self and one arg , then intialize 1st parameter also
        print('Hello, World!')
    @classmethod
    def example_function(abc):
        print('I\'m a class method!')
        #abc.some_other_function()
    @staticmethod
    def some_other_function():
        print('Hello!')
de = DecoratorExample()
de.example_function()
de.some_other_function()
# Hello, World!
# I'm a class method!
# Hello!


================================
class DecoratorExample:
    def __init__(self):  # either self or anything bdvhfdvghd, if both self and one arg , then intialize 1st parameter also
        print('Hello, World!')

    def example_function(abc):
        print('I\'m a class method!')
        abc.some_other_function()

    def some_other_function():
        print('Hello!')
de = DecoratorExample()
de.example_function()
de.some_other_function()
# Hello, World!
# I'm a class method!
# TypeError: some_other_function() takes 0 positional arguments but 1 was given

==================================
class DecoratorExample:
    def __init__(self):  # either self or anything bdvhfdvghd, if both self and one arg , then intialize 1st parameter also
        print('Hello, World!')

    def example_function(abc):
        print('I\'m a class method!')
        abc.some_other_function()

    def some_other_function(self):
        print('Hello!')
de = DecoratorExample()
de.example_function()
de.some_other_function
# Hello, World!
# I'm a class method!
# Hello!

===================================
class DecoratorExample:
  """ Example Class """
  def __init__(self):
    """ Example Setup """
    print('Hello, World!') 

  @classmethod
  def example_function(cls):
    """ This method is a class method! """
    print('I\'m a class method!')
    cls.some_other_function()  #for calling static method

  @staticmethod
  def some_other_function():
    print('Hello!')
de = DecoratorExample()
de.example_function()
#Hello, World!
#I'm a class method!
#Hello!
==============================
class DecoratorExample:
  """ Example Class """
  def __init__(self):
    """ Example Setup """
    print('Hello, World!')

  @classmethod
  def example_function(cls):
    """ This method is a class method! """
    print('I\'m a class method!')
    cls.some_other_function()

  #@staticmethod
  def some_other_function():
    print('Hello!')
de = DecoratorExample()
de.example_function()

Hello, World!
I'm a class method!
Hello!
==============================
class DecoratorExample:
    def __init__(self):
        print('Hello, World!')
    @classmethod
    def example_function(cls):
        print('I\'m a class method!')
        cls.some_other_function()
    @staticmethod
    def some_other_function():
        print('Hello!')
de = DecoratorExample()
de.example_function()
# Hello, World!
# I'm a class method!
# Hello!
===============================
class DecoratorExample:
    def __init__(self):
        print('Hello, World!')
    @classmethod
    def example_function(cls):
        print('I\'m a class method!')
        cls.some_other_function()
    @staticmethod
    def some_other_function():
        print('Hello!')
de = DecoratorExample()
de.example_function()
de.some_other_function()
# Hello, World!
# I'm a class method!
# Hello!

6. Class methods are possibly the more confusing method types of the three, but they do have their uses. 
7. Class methods can manipulate the class itself, which is useful when you’re working on larger, more complex projects
====================================
class Person:
    age = 25

    def printAge(cls):
        print('The age is:', cls.age)
# create printAge class method
Person.printAge = classmethod(Person.printAge)
Person().printAge()
Person.printAge()
#The age is: 25
#The age is: 25
=============================
class Person:
    age = 25

    def printAge(cls,abc):
        cls.abc = abc
        print('The age is:', cls.age)
        print('The age is:', cls.abc)
# create printAge class method
Person.printAge = classmethod(Person.printAge)
Person().printAge(20)
Person.printAge(15)
#The age is: 25
#The age is: 20
#The age is: 25
#The age is: 15
=============================
class Person:
    age = 25

    def printAge(cls):
        print('The age is:', cls.age)
# create printAge class method
obj = Person()
obj.printAge()
#25
==================================
class Person:
    age = 25
    print("class person")
    def printAge(cls):
        print('The age is:', cls.age)
# create printAge class method
Person.printAge = classmethod(Person.printAge)
Person().printAge()
Person.printAge(30)
# class person
# The age is: 25
# TypeError: printAge() takes 1 positional argument but 2 were given



=============================
class Person:
    age = 25
    print("class person")
    def printAge(cls):
        print('The age is:', cls.age)
# create printAge class method
Person.printAge = classmethod(Person.printAge)
Person().printAge()
Person.printAge()
#class person
#The age is: 25
#The age is: 25
=============================
class Person:
    age = 25
    print("class person")
    def printAge(cls):
        print('The age is:', cls.age)
# create printAge class method
Person.printAge = classmethod(Person.printAge)
#Person().printAge()
#Person.printAge()
#class person
=============================
class Person:
    age = 25
    print("class person")
    def printAge(cls):
        print('The age is:', cls.age)
# create printAge class method
Person.printAge = classmethod(Person.printAge)
Person().printAge()
Person.printAge()
#class person
#The age is: 25
#The age is: 25
=============================
class abc:
    print("class method")
    age = 20
    def inner(cls):
        print("the age is ",cls.age)
abc.inner = classmethod(abc.inner)
abc.inner()
#class method
#the age is  20
============================
class abc:
    print("class method")
    age = 20
    @classmethod
    def inner(cls,age):
        print("the age is ",age)
abc.inner = classmethod(abc.inner(10))
#class method
#the age is  10
============================
class abc:
    print("class method")
    age = 20
    @classmethod
    def inner(cls,age):
        print("the age is ",age)
        print("the age is ",cls.age)
abc.inner = classmethod(abc.inner(10))
#class method
#the age is  10
#the age is  20
============================
class abc:
    print("class method")
    age = 20
    @classmethod
    def __init__(cls,age):
        print("the age is ",cls.age)
obj = abc(50)
#class method
#the age is  20
============================
class abc:
    print("class method")
    age = 20
    @classmethod
    def __init__(cls,age):
        cls.age = age
        print("the age is ",cls.age)
obj = abc(50)
#class method
#the age is  50
============================
class abc:
    print("class method")
    age = 20
    @classmethod
    def __init__(cls,age):
        cls.age = age
        print("the age is ",cls.age)
        print("the age is ",age)
obj = abc(50)
#class method
#the age is  50
#the age is  50
===========================
class abc:
    print("class method")
    age1 = 20
    @classmethod
    def __init__(cls,age):
        cls.age = age
        print("the age is ",cls.age)
        print("the age is ",age1)
obj = abc(50)
# class method
# the age is  50
# NameError: name 'age1' is not defined
============================
class abc:
    print("class method")
    age = 20
    @classmethod
    def inner(cls,age):
        print("the age is ",age)
abc.inner = classmethod(abc.inner) #it will call only the class, not the method 
#class method
============================
class abc:
    print("class method")
    age = 20
    @classmethod
    def inner(cls,age):
        print("the age is ",age)
abc.inner = classmethod(abc.inner)
abc.inner()
#class method
#the age is  <class '__main__.abc'>
============================
class abc:
    print("class method")
    age = 20
    @classmethod
    def inner(cls,age):
        print("the age is ",age)
abc.inner = classmethod(abc.inner)
abc.inner(30)
#class method
#TypeError: inner() takes 2 positional arguments but 3 were given
============================
class abc:
    print("class abc")
    @classmethod
    def inner(cls,age):
        print("age is ",age)
abc.inner = classmethod(abc.inner(10))
#class abc
#age is  10
============================
class abc:
    print("class abc")
    @classmethod
    def inner(cls,age):
        print("age is ",age)
abc.inner = classmethod(abc.inner)
abc.inner(20)
#class abc
#TypeError: inner() takes 2 positional arguments but 3 were given
============================
class abc:
    print("class abc")
    @classmethod
    def inner(cls,age):
        print("age is ",age)
abc.inner = classmethod(abc.inner)
#class abc
============================
class abc:
    age = 125
    print("class abc")
    @classmethod
    def inner(cls,age):
        print("age is ",cls.age)
abc.inner = classmethod(abc.inner(20))
#class abc
#age is  125
============================
class abc:
    age = 125
    print("class abc")
    @classmethod
    def inner(cls,age):
        print("age is ",cls.age)
abc.inner = classmethod(abc.inner)
abc.inner(20)
#class abc
#TypeError: inner() takes 2 positional arguments but 3 were given


==============================
class outer:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    @classmethod
    def inner01(cls,salary,rollno):
        outer.xyzanything = salary
        outer.rollno1 =  rollno
obj = outer("kumar","anuj")
outer.inner01 = classmethod(outer.inner01(1000,101))
print(outer.rollno1)
print(outer.xyzanything)
#101
#1000
===========================
class outer:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    @classmethod
    def inner01(cls,salary,rollno):
        outer.xyzanything = salary
        outer.rollno1 = rollno
obj = outer("kumar","anuj")
outer.inner01 = classmethod(outer.inner01(1000,101))
print(outer.rollno1)
print(outer.xyzanything)
#101
#1000
===========================
class outer:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    @classmethod
    def inner01(cls,salary,rollno):
        outer.xyzanything = salary
        outer.rollno1 = rollno
obj = outer("kumar","anuj")
outer.inner01 = classmethod(outer.inner01(1000,101))
print(outer.rollno1)
print(outer.xyzanything)
#101
#1000
===========================
class outer:
    @classmethod
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        print(self.firstname)
        print(self.lastname)

    @classmethod
    def inner01(cls,salary,rollno):
        outer.xyzanything = salary
        outer.rollno1 = rollno
obj = outer("kumar","anuj")
outer.inner01 = classmethod(outer.inner01(1000,101))
print(outer.xyzanything)
print(outer.rollno1)
#kumar
#anuj
#1000
#101
===========================
class outer:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    @classmethod
    def inner01(cls,salary,rollno):
        outer.xyzanything = salary
        outer.rollno1 = rollno
obj = outer("kumar","anuj")
outer.inner01(1000,101)
print(outer.xyzanything)
print(obj.xyzanything)
print(outer.rollno1)
print(obj.rollno1)
print(obj.firstname)
print(obj.lastname)

#1000
#1000
#101
#101
#kumar
#anuj
========================================
class outer:

    @classmethod
    def inner01(cls,salary,rollno):
        outer.salary1 = salary
        outer.rollno1 = rollno
        print("roll no is ",rollno)
        print("salary  is ",salary)

    @classmethod
    def inner02(cls,fname,lname):
        outer.fname1=fname
        outer.lname1=lname

outer.inner01 = classmethod(outer.inner01(100,10))

#roll no is  10
#salary  is  100
========================================
class outer:

    @classmethod
    def inner01(self,salary,rollno):
        self.salary1 = salary
        outer.rollno1 = rollno
        print("roll no is ",rollno)
        print("salary  is ",salary)

    @classmethod
    def inner02(cls,fname,lname):
        outer.fname1=fname
        cls.lname1=lname
        print(fname)

outer.inner01 = classmethod(outer.inner01(100,10))
outer.inner02 = classmethod(outer.inner02("kumar","anuj"))


#roll no is  10
#salary  is  100
#kumar
======================================
class outer:

    @classmethod
    def inner01(self,salary,rollno):
        self.salary1 = salary
        outer.rollno1 = rollno
        print("roll no is ",rollno)
        print("salary  is ",salary)

    @classmethod
    def inner02(cls,fname,lname):
        outer.fname1=fname
        cls.lname1=lname
        print(fname)

outer().inner01 = classmethod(outer.inner01(100,10))
outer.inner02 = classmethod(outer.inner02("kumar","anuj"))
# roll no is  10
# salary  is  100
# kumar


========================================
class outer:

    @classmethod
    def inner01(self,salary,rollno):
        self.salary1 = salary
        outer.rollno1 = rollno
        print("roll no is ",rollno)
        print("salary  is ",salary)

    @classmethod
    def inner02(cls,fname,lname):
        outer.fname1=fname
        cls.lname1=lname
        print(fname)
obj = classmethod(outer.inner01(100,10))
obj = classmethod(outer.inner02("kumar","anuj"))

#roll no is  10
#salary  is  100
#kumar
========================================
class outer:

    @classmethod
    def inner01(cls,salary,rollno):
        outer.salary1 = salary
        outer.rollno1 = rollno

    @classmethod
    def inner02(cls,fname,lname):
        outer.fname1=fname
        outer.lname1=lname
obj = outer()
outer.inner01(100,10)
print(outer.salary1)
print(outer.rollno1)
outer.inner02("kumar","anuj")
print(outer.fname1)
print(outer.lname1)

#100
#10
#kumar
#anuj
=========================================
class outer:

    @classmethod
    def inner01(cls,salary,rollno):
        outer.salary1 = salary
        outer.rollno1 = rollno
        print("roll no is ",rollno)
        print("salary  is ",salary)

    @classmethod
    def inner02(cls,fname,lname):
        outer.fname1=fname
        outer.lname1=lname
        print("first name",fname)
        print("last name",lname)

outer.inner01 = classmethod(outer.inner01(100,10))
outer.inner02 = classmethod(outer.inner02("kumar","anuj"))

#roll no is  10
#salary  is  100
#first name kumar
#last name anuj
=========================================
class outer:

    @classmethod
    def inner01(cls,salary,rollno):
        outer.salary1 = salary
        outer.rollno1 = rollno
        print("roll no is ",rollno)
        print("salary  is ",salary)

    @classmethod
    def inner02(cls,fname,lname):
        outer.fname1=fname
        outer.lname1=lname

outer().inner01 = classmethod(outer.inner01(100,10))

#roll no is  10
#salary  is  100

=========================================
===========static method=================
=========================================
1. Static methods are methods that are related to a class in some way, but don’t need to access any class=specific data. 
You don’t have to use self, and you don’t even need to instantiate an instance, you can simply call your method:

class DecoratorExample:
  """ Example Class """
  def __init__(self):
    """ Example Setup """
    print('Hello, World!') 

  @staticmethod
  def example_function():
    """ This method is a static method! """
    print('I\'m a static method!')
 
de = DecoratorExample.example_function()
#I'm a static method!
========================================
class DecoratorExample:
    """ Example Class """
    def __init__(self):
        """ Example Setup """
        print('Hello, World!')

    @staticmethod
    def example_function():
        """ This method is a static method! """
        print('I\'m a static method!')

de = DecoratorExample.example_function()
de1 = DecoratorExample()
# I'm a static method!
# Hello, World!
======================================
class DecoratorExample:
    def __init__(self):
        print('Hello, World!')\
    @staticmethod
    def example_function():
        print('I\'m a static method!')
de = DecoratorExample.example_function()
#I'm a static method!
=======================================
class DecoratorExample:
    def __init__(self):
        print('Hello, World!')\
    @staticmethod
    def example_function():
        print('I\'m a static method!')
de = staticmethod(DecoratorExample.example_function())

#I'm a static method!
===================================

2. The @staticmethod decorator was used to tell Python that this method is a static method.
3. Static methods are great for utility functions, which perform a task in isolation. 
4. They don’t need to (and cannot) access class data. They should be completely self=contained, and only work with data 
passed in as arguments. 
5. You may use a static method to add two numbers together, or print a given string.

========================================
1. A static method does not receive an implicit first argument.

class C(object):
    @staticmethod
    def fun(arg1, arg2, ...):
        ...
returns: a static method for function fun.

2. A static method can’t access or modify class state.
3. It is present in a class because it makes sense for the method to be present in class.

===========================================
class outer:
    @staticmethod
    def inner01(salary,rollno):
        outer.salary1 = salary
        outer.rollno1 = rollno
        print("roll no is ",rollno)
        print("salary  is ",salary)
    @staticmethod
    def inner02(fname,lname):
        outer.fname1=fname
        outer.lname1=lname
        print("fname is ", fname)
        print("lname  is ", lname)
outer.inner01 = staticmethod(outer.inner01(100,10))
outer().inner02 = staticmethod(outer.inner02("kumar","anuj"))

#roll no is  10
#salary  is  100
#fname is  kumar
#lname  is  anuj
=============================================
class outer:
    @staticmethod
    def inner01(salary,rollno):
        outer.salary1 = salary
        outer.rollno1 = rollno
        print("roll no is ",rollno)
        print("salary  is ",salary)
    @staticmethod
    def inner02(fname,lname):
        outer.fname1=fname
        outer.lname1=lname
        print("fname is ", fname)
        print("lname  is ", lname)
obj1 = staticmethod(outer.inner01(100,10))
obj2 = staticmethod(outer.inner02("kumar","anuj"))

#roll no is  10
#salary  is  100
#fname is  kumar
#lname  is  anuj
===========================================
====Class method vs Static Method==========
===========================================
1. A class method takes cls as first parameter while a static method needs no specific parameters.
2. A class method can access or modify class state while a static method can’t access or modify it.
3. In general, static methods know nothing about class state. They are utility type methods that take 
some parameters and work upon those parameters. On the other hand class methods must have class as parameter.
4. We use @classmethod decorator in python to create a class method and we use @staticmethod 
decorator to create a static method in python.
