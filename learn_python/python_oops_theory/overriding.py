=========================================
===========Override Method===============
=========================================
1. A subclass may change the functionality of a Python method in the superclass. 
It does so by redefining it
2. Overriding is the ability of a class to change the implementation of a method provided by one of its ancestors.
3. Overriding is a very important part of OOP since it is the feature that makes inheritance exploit its full power.
4. Through method overriding a class may "copy" another class, avoiding duplicated code, and at the same time enhance or customize part of it. 
5. Override means having two methods with the same name but doing different tasks. It means that one of the methods overrides the other.
If there is any method in the superclass and a method with the same name in a subclass, then by executing the method,
the method of the corresponding class will be executed.
6. Overriding is the ability of a class to change the implementation of a method provided by one of its ancestors.
Overriding is a very important part of OOP since it is the feature that makes inheritance exploit its full power. 
Through method overriding a class may "copy" another class, avoiding duplicated code, and at the same time enhance 
or customize part of it. Method overriding is thus a strict part of the inheritance mechanism.
==========================
class A:
  def sayhi(self):
    print("I'm in A")                          
class B(A):
  def sayhi(self):
    print("I'm in B")                             
bobj=B()
bobj.sayhi()
A.sayhi("xxx")
#I'm in B
#I'm in A
========================
class A:
  def sayhi(self):
    print("I'm in A")
class B(A):
  def sayhi(self):
    print("I'm in B")
bobj=B()
bobj.sayhi()
A.sayhi("xxx")
B.sayhi("aaa")
# I'm in B
# I'm in A
# I'm in B
========================
class A:
  def sayhi():
    print("I'm in A")                          
class B(A):
  def sayhi1():
    print("I'm in B")                             
bobj=B()
bobj.sayhi1()
#TypeError: sayhi1() takes 0 positional arguments but 1 was given
=========================
class A:
  def sayhi(self):
    print("I'm in A")
class B(A):
  def sayhi1(self):
    print("I'm in B")
bobj=B()
bobj.sayhi1()
#I'm in B
===============================

class A:
  def sayhi():
    print("I'm in A")                          
class B(A):
  def sayhi1(self):
    print("I'm in B")                             
bobj=B()
bobj.sayhi1()
#I'm in B
=========================
class A:
  def sayhi(self):
    print("I'm in A")                          
class B(A):
  def sayhi1():
    print("I'm in B")                             
bobj=B()
bobj.sayhi1()
#TypeError: sayhi1() takes 0 positional arguments but 1 was given
===========================
class Rectangle():
	def __init__(self,length,breadth):
		self.length = length
		self.breadth = breadth
	def getArea(self):
		print(self.length*self.breadth," is area of rectangle")
class Square(Rectangle):
	def __init__(self,side):
		self.side = side
		Rectangle.__init__(self,side,side)
	def getArea(self):
		print(self.side*self.side," is area of square")
s = Square(4)
r = Rectangle(2,4)
s.getArea()
r.getArea()
#16  is area of square
#8  is area of rectangle
===================================
class Rectangle():
	def __init__(self,length,breadth):
		self.length = length
		self.breadth = breadth
	def getArea(self):
		print(self.length*self.breadth," is area of rectangle")
class Square(Rectangle):
	def __init__(self,side):
		self.side = side
		#Rectangle.__init__(self,side,side)
	def getArea(self):
		print(self.side*self.side," is area of square")
s = Square(4)
r = Rectangle(2,4)
s.getArea()
r.getArea()
#16  is area of square
#8  is area of rectangle
================================
class Rectangle():
	def __init__(self,length,breadth):
		self.length = length
		self.breadth = breadth
	def getArea(self):
		print(self.length*self.breadth," is area of rectangle")
class Square(Rectangle):
	def __init__(self,side):
		self.side = side
		#Rectangle.__init__(self,side,side)
	def getArea(self):
		print(self.side*self.side," is area of square")
s = Square(4)
r = Rectangle(2,4)
s.getArea()
r.getArea()

#16  is area of square
#8  is area of rectangle



