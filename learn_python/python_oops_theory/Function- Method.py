===================================
==========methods==================
===================================
1. It's a function which is a member of a class:
class C:
    def my_method(self):
        print("I am a C")
c = C()
c.my_method()  # Prints "I am a C"
2. Method is called by its name, but it is associated to an object (dependent).
3. A method is implicitly passed the object on which it is invoked.
4. It may or may not return any data.
5. A method can operate on the data (instance variables) that is contained by the corresponding class

# Basic Python method  
class class_name 
    def method_name () : 
        ...... 
        # method body 
        ......    
class ABC : 
    def method_abc (self): 
        print("I am in method_abc of ABC class. ") 
  class_ref = ABC() # object of ABC class 
class_ref.method_abc() 
============================
===========Functions========
============================
1. Function is block of code that is also called by its name. (independent)
2. The function can have different parameters or may not have any at all. If any data (parameters) 
are passed, they are passed explicitly.
3. It may or may not return any data.
4. Function does not deal with Class and its instance concept.
5. Basic Function Structure in Python :

def function_name ( arg1, arg2, ...) : 
    ...... 
    # function body 

def Subtract (a, b): 
    return (a-b) 
print( Subtract(10, 12) ) # prints -2 
print( Subtract(15, 6) ) # prints 9 
============================================
Difference between method and function:=====
============================================
1. Simply, function and method both look similar as they perform in almost similar way, 
but the key difference is the concept of ‘Class and its Object‘.
2. Functions can be called only by its name, as it is defined independently. 
But methods can’t be called by its name only, we need to invoke the class by a 
reference of that class in which it is defined, i.e. method is defined within a class and 
hence they are dependent on that class.
