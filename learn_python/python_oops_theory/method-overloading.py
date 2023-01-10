===========================================
==============method overloading===========
===========================================
1. Like other languages (for example method overloading in C++) do, python does not supports method overloading.
We may overload the methods but can only use the latest defined method.
2. Method overloading. In Python you can define a method in such a way that there are multiple ways to call it. 
Given a single method or function, we can specify the number of parameters ourself. Depending on the function 
definition, it can be called with zero, one, two or more parameters.
3. In Python you can define a method in such a way that there are multiple ways to call it.
Given a single method or function, we can specify the number of parameters ourself.
Depending on the function definition, it can be called with zero, one, two or more parameters.
This is known as method overloading. Not all programming languages support method overloading, but Python does.
==================================
# First product method. 
# Takes two argument and print their 
# product 
==================================
def product(a, b): 
    p = a * b 
    print(p) 
# Second product method 
# Takes three argument and print their 
# product 
def product(a, b, c): 
    p = a * b*c 
    print(p) 
# Uncommenting the below line shows an error     
# product(4, 5) 
# This line will call the second product method 
product(4, 5, 5) 
#100
=================================
def product(a, b):
    p = a * b
    print(p)
def product(a, b, c):
    p = a * b*c
    print(p)
#product(4, 5)
product(4, 5,10)
#200
=================================
def add(datatype, *args): 
    # if datatype is int 
    # initialize answer as 0 
    if datatype =='int': 
        answer = 0
    # if datatype is str 
    # initialize answer as '' 
    if datatype =='str': 
        answer ='' 
    # Traverse through the arguments 
    for x in args: 
        # This will do addition if the  
        # arguments are int. Or concatenation  
        # if the arguments are str 
        answer = answer + x 
    print(answer) 
add('int', 5, 6) 
# String 
add('str', 'Hi ', 'Geeks') 
#11
#Hi Geeks
=======================================
def add(datatype, *args):
    if datatype =='int':
        answer = 0
    if datatype =='str':
        answer =''
    for x in args:
        answer = answer + x
    print(answer)
add('int', 5, 6)
add('str', 'Hi ', 'Geeks')
#11
#Hi Geeks
=======================================
class Human:
 
    def sayHello(self, name=None):
 
        if name is not None:
            print ('Hello ' + name)
        else:
            print ('Hello ')
# Create instance
obj = Human()
# Call the method
obj.sayHello()
# Call the method with a parameter
obj.sayHello('Guido')
#Hello 
#Hello Guido
================================
class Human:
    def sayHello(self, name=None):
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')
obj = Human()
obj.sayHello()
obj.sayHello('Guido')
# Hello
# Hello Guido
==============================
class A:
    def stackoverflow(self):    
        print ('first method')
    def stackoverflow(self, i):
        print ('second method', i)
ob=A()
ob.stackoverflow() #error ==> TypeError: stackoverflow() missing 1 required positional argument: 'i'
==============================
class A:
    def stackoverflow(self):    
        print ('first method')
    def stackoverflow(self, ):
        print ('second method', )
ob=A()
ob.stackoverflow() #second method
=================================
class Robot:
    def action1(self):
        print('action 1')
    def action1(self):
        print('action 2')

class HelloRobot(Robot):
    def action(self):
        print('Hello world')
r = HelloRobot()
r.action()
r.action1()

#Hello world
#action 2
=============================
class Robot:
    def action1(self):
        print('action 1')
    def action1(self):
        print('action 2')
    def action(self):
        print('Hello world55')

class HelloRobot(Robot):
    def action(self):
        print('Hello world')
r = HelloRobot()
r.action()
r.action1()

# Hello world
# action 2
===========================o
class Robot:
    def action1(self):
        print('action 1')
    def action1(self):
        print('action 2')
    def action(self):
        print('Hello world55')

class HelloRobot(Robot):
    pass
r = HelloRobot()
r.action()
r.action1()
# Hello world55
# action 2

======================


