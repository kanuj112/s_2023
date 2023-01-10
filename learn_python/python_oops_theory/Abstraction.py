==============================
Abstraction:==================
==============================
1. Abstract classes are classes that contain one or more abstract methods.
2. An abstract method is a method that is declared, but contains no implementation.
3. Abstract classes may not be instantiated, and require subclasses to provide implementations for the abstract methods. 
4. Subclasses of an abstract class in Python are not required to implement abstract methods of the parent class.
==============================
==> Abstraction refers to providing only essential information about the data to the outside world, hiding the background
details or implementation.
==============================
Abstraction: Suppose you are going to an ATM to withdraw money. You simply insert your card and click some buttons and get
the money. You don’t know what is happening internally on press of these buttons. Basically you are hiding unnecessary 
information from user. So, abstraction is a method to hide internal functionalities from user.
===============================
==>Data encapsulation -->is one of the fundamentals of OOP (object-oriented programming). It refers to the bundling of 
data with the methods that operate on that data.Encapsulation is used to hide the values or state of a 
structured data object inside a class, preventing unauthorized parties' direct access to them.
==============================
Encapsulation: Suppose there is a tree. Now a tree can have its components like root, stem, branches, leaves, flowers 
and fruits. It has some functionalities like Photosynthesis. But in a single unit we call it a tree. In same way encapsulation 
is a characteristic to bind data members and functions in single unit.
======================================
class AbstractClass:
	def do_something(self):
        pass
class B(AbstractClass):
    pass
a = AbstractClass()
b = B()
================================
class AbstractClass:
    def do_something(self):
        print("abc")
class B(AbstractClass):
    print("zzz")
a = AbstractClass()
a.do_something()
#zzz
#abc
=================================
class AbstractClass:
    def do_something(self):
        print("abc")
class B(AbstractClass):
    def do_something(self):
        print("abc01")
    print("zzz")
a = AbstractClass()
a.do_something()
# zzz
# abc
=================================
class AbstractClass:
    def do_something(self):
        print("abc")
class B(AbstractClass):
    def do_something(self):
        print("abc01")
    print("zzz")
a = B()
a.do_something()
# zzz
# abc01
===============================
class AbstractClass:
    def do_something(self):
        print("abc")
class B(AbstractClass):
    print("zzz")
a = AbstractClass()
#a.do_something()
#zzz
=================================
class AbstractClass:
    def do_something(self):
        print("abc")
class B(AbstractClass):
    print("zzz")
a = B()
#a.do_something()
#zzz
=================================
class AbstractClass:
    def do_something(self):
        print("abc")
class B(AbstractClass):
    print("zzz")
a = B()
a.do_something()
# zzz
# abc
=================================
class AbstractClass:
    def do_something(self):
        print("abc")
class B(AbstractClass):
    def do_something(self):
        print("abc01")
    print("zzz")
a = B()
a.do_something()
# zzz
# abc01
=================================
class abc:
    def aaa(self):
        pass
class abc02(abc):
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    a1 = abc() #NOT NECESSDARE as it wont do anything
    main()
#class abc02
#class abc03
================================
class abc:
    print("class abc")
    def aaa(self):
        pass
class abc02(abc):
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    a1 = abc() #NOT NECESSDARE as it wont do anything
    main()
# class abc
# class abc02
# class abc03
================================
class abc:
    def aaa(self):
        print("zzz")
class abc02(abc):
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    a1 = abc() #NOT NECESSDARE as it wont do anything
    main()
# class abc02
# class abc03
================================
class abc:
    def aaa(self):
        print("zzz")
class abc02(abc03):
    def aaa(self):
        print("class abc02")
class abc03(abc02):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    a1 = abc() #NOT NECESSDARE as it wont do anything
    main()
#NameError: name 'abc03' is not defined
================================
class abc:
    def aaa(self):
        print("zzz")
class abc02():
    def aaa(self):
        print("class abc02")
class abc03():
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    a1 = abc() #NOT NECESSDARE as it wont do anything
    main()
# class abc02
# class abc03
============================
class abc:
    def aaa(self):
        print("bbb")
class abc02(abc):
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    a1 = abc() #only creating objects wont do anything
    main()
#class abc02
#class abc03
================================
class abc:
    def aaa(self):
        print("bbb")
class abc02(abc):
    def aa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    a1 = abc() #only creating objects wont do anything
    main()
# bbb
# class abc03
================================
class abc:
    def aaa(self):
        print("aabbcc")
class abc02(abc):
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    a1 = abc() 
    a1.aaa()
    main()
#aabbcc
#class abc02
#class abc03
===============================
from abc import ABC, abstractmethod

class abc(ABC):
    @abstractmethod
    def aaa(self):
        pass
class abc02(abc):
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    a1 = abc()
    main()
#TypeError: Can't instantiate abstract class abc with abstract methods aaa
=================================
from abc import ABC, abstractmethod
class abc(ABC):
    print("hhh")
    @abstractmethod
    def aaa(self):
        pass
class abc02(abc):
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    a1 = abc()
    main()
#TypeError: Can't instantiate abstract class abc with abstract methods aaa
#hhh
=========================================
from abc import ABC, abstractmethod

class abc(ABC):
    @abstractmethod
    def aaa(self):
        pass
class abc02(abc):
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    a1 = abc()
    a1.aaa()
    main()
#TypeError: Can't instantiate abstract class abc with abstract methods aaa
=================================
from abc import ABC, abstractmethod

class abc(ABC):
    #@abstractmethod
    def aaa(self):
        pass
class abc02():
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    a1 = abc()
    main()
#class abc02
#class abc03
==============================
from abc import ABC, abstractmethod

class abc(ABC):
    #@abstractmethod
    def aaa(self):
        print("ss")
class abc02():
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    a1 = abc()
    a1.aaa() #it will call class abc aaa method
    main()
# class abc02
# class abc03
==============================
from abc import ABC, abstractmethod

class abc(ABC):
    @abstractmethod
    def aaa(self):
        pass
class abc02(abc):
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    #a1 = abc()
    main()
#class abc02
#class abc03
==============================
from abc import ABC, abstractmethod

class abc(ABC):
    @abstractmethod
    def aaa(self):
        pass
class abc02(abc):
    def aaa0(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    #a1 = abc()
    main()
#TypeError: Can't instantiate abstract class abc02 with abstract methods aaa
==============================
from abc import ABC, abstractmethod
class abc(ABC):
    @abstractmethod
    def aaa(self):
        pass
class abc02():
    def aaa(self):
        print("class abc02")
class abc03(ABC):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    a1 = abc()
    main()
#TypeError: Can't instantiate abstract class abc with abstract methods aaa
===============================
from abc import ABC, abstractmethod

class abc(ABC):
    print("kjfd")
    @abstractmethod
    def aaa(self):
        pass
class abc02(abc):
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    a1 = abc()
    main()
#kjfd
#TypeError: Can't instantiate abstract class abc with abstract methods aaa
===============================
from abc import ABC, abstractmethod

class abc(ABC):
    @abstractmethod
    def aaa(self):
        print("scfjnsdjk")
class abc02():
    def aaa(self):
        print("class abc02")
class abc03(ABC):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    a1 = abc()
    a1.aaa()
    main()
# a1 = abc()
#TypeError: Can't instantiate abstract class abc with abstract methods aaa
===============================
from abc import ABC, abstractmethod

class abc(ABC):
    @abstractmethod
    def aaa(self):
        print("scfjnsdjk")
class abc02():
    def aaa(self):
        print("class abc02")
class abc03(ABC):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    # a1 = abc()
    # a1.aaa()
    main()
# class abc02
# class abc03
===============================
from abc import ABC, abstractmethod

class abc(ABC):
    @abstractmethod
    def aaa(self):
        print("scfjnsdjk")
class abc02(abc):
    def aaa1(self):
        print("class abc02")
class abc03(ABC):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    # a1 = abc()
    # a1.aaa()
    main()
# TypeError: Can't instantiate abstract class abc02 with abstract methods aaa
===============================
from abc import ABC, abstractmethod

class abc(ABC):
    @abstractmethod
    def aaa(self):
        print("scfjnsdjk")
class abc02(abc):
    def aaa(self):
        print("class abc02")
class abc03(ABC):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    # a1 = abc()
    # a1.aaa()
    main()
# class abc02
# class abc03
===============================
from abc import ABC, abstractmethod

class abc():
    @abstractmethod
    def aaa(self):
        pass
class abc02(ABC):
    @abstractmethod
    def aaa(self):
        print("class abc02")
class abc03(ABC):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    a1 = abc()
    main()
#TypeError: Can't instantiate abstract class abc with abstract methods aaa
=================================
from abc import ABC, abstractmethod

class abc():
    @abstractmethod
    def aaa(self):
        print("aaa")
class abc02(ABC):
    @abstractmethod
    def aaa(self):
        print("class abc02")
class abc03(ABC):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    a1 = abc()
    a1.aaa()
    main()
#aaa
#TypeError: Can't instantiate abstract class abc02 with abstract methods aaa
=================================
from abc import ABC, abstractmethod
class abc():
    print("aaa")
    @abstractmethod
    def aaa(self):
        print("fkfd")
class abc02(ABC):
    @abstractmethod
    def aaa(self):
        print("class abc02")
class abc03(ABC):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    a1 = abc()
    main()
#aaa
#TypeError: Can't instantiate abstract class abc02 with abstract methods aaa
=================================
from abc import ABC, abstractmethod
class abc():
    print("aaa")
    @abstractmethod
    def aaa(self):
        print("fkfd")
class abc02(ABC):
    @abstractmethod
    def aaa(self):
        print("class abc02")
class abc03(ABC):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    a1 = abc()
    a1.aaa()
    main()
# TypeError: Can't instantiate abstract class abc02 with abstract methods aaa
# aaa
# fkfd
=================================
from abc import ABC, abstractmethod
class abc():
    @abstractmethod
    def aaa(self):
        print("dbfsd")
class abc02(ABC):
    @abstractmethod
    def aaa(self):
        print("class abc02")
class abc03(ABC):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    a1 = abc()
    a1.aaa()
    main()
#dbfsd
#obj1 = abc02()
#TypeError: Can't instantiate abstract class abc02 with abstract methods aaa
=================================
from abc import ABC, abstractmethod
class abc():
    @abstractmethod
    def aaa(self):
        print("dbfsd")
class abc02(ABC):
    @abstractmethod
    def aaa(self):
        print("class abc02")
class abc03(ABC):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    a1 = abc()
    a1.aaa()
    main()
#dbfsd
#TypeError: Can't instantiate abstract class abc02 with abstract methods aaa
=====================================
from abc import ABC, abstractmethod

class abc(ABC):
    @abstractmethod
    def aaa(self):
        pass
class abc02(abc):
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    #a1 = abc()
    main()
#class abc02
#class abc03
=================================
from abc import ABC, abstractmethod

class abc(ABC):
    print("ddddd")
    @abstractmethod
    def aaa(self):
        pass
class abc02(abc):
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    #a1 = abc()
    main()
# ddddd
# class abc02
# class abc03
=================================
from abc import ABC, abstractmethod

class abc(ABC):
    print("ddddd")
    @abstractmethod
    def aaa(self):
        pass
class abc02(abc):
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    #obj1 = abc02()
    #obj1.aaa()

    #obj2 = abc03()
    #obj2.aaa()
    pass
if __name__ == "__main__":  # it will call the abc class 
    pass
    #a1 = abc()
    #main()
#ddddd
=================================
from abc import ABC, abstractmethod

class abc(ABC):
    #@abstractmethod
    def aaa(self):
        print("aabbcc")
class abc02(abc):
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    a1 = abc()
    main()
#class abc02
#class abc03
=================================
from abc import ABC, abstractmethod

class abc(ABC): #ABC in argument
    #@abstractmethod
    def aaa(self):
        print("aabbcc")
class abc02(abc):
    @abstractmethod
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()

    #obj2 = abc02() it will give error
    #obj2.aaa()

if __name__ == "__main__":
    a1 = abc()
    main()
#aabbcc
#class abc03
=================================
from abc import ABC, abstractmethod

class abc(ABC): #ABC in argument
    #@abstractmethod
    def aaa(self):
        print("aabbcc")
class abc02():
    @abstractmethod
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()

    #obj2 = abc02() it will give error
    #obj2.aaa()

if __name__ == "__main__":
    a1 = abc()
    main()
# aabbcc
# class abc03
=================================
from abc import ABC, abstractmethod

class abc():
    #@abstractmethod
    def aaa(self):
        print("aabbcc")
class abc02(abc):
    @abstractmethod
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()

    obj2 = abc02() 
    obj2.aaa()

if __name__ == "__main__":
    a1 = abc()
    main()
#aabbcc
#class abc03
#class abc02
=================================
from abc import ABC, abstractmethod

class abc(ABC):
    #@abstractmethod
    def aaa(self):
        print("aabbcc")
class abc02():
    @abstractmethod
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()

    obj2 = abc02()
    obj2.aaa()

if __name__ == "__main__":
    a1 = abc()
    main()
# aabbcc
# class abc03
# class abc02
=================================
from abc import ABC, abstractmethod

class abc():
    #@abstractmethod
    def aaa(self):
        print("aabbcc")
class abc02(abc):
    @abstractmethod
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc()
    obj1.aaa()
    obj2 = abc03()
    obj2.aaa()
    obj2 = abc02()
    obj2.aaa()
if __name__ == "__main__":
    a1 = abc()
    a1.aaa()
    main()
# aabbcc
# aabbcc
# class abc03
# class abc02
=================================GOOD EXAMPLE
=================================
from abc import ABC, abstractmethod

class abc(ABC):
    #@abstractmethod
    def aaa(self):
        print("aabbcc")
class abc02(abc):
    @abstractmethod
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()

    obj2 = abc02() #it will give error
    obj2.aaa()

if __name__ == "__main__":
    a1 = abc()
    main()
#aabbcc
#class abc03
#TypeError: Can't instantiate abstract class abc02 with abstract methods aaa
=================================
from abc import ABC, abstractmethod

class abc(ABC):
    print("das")
    #@abstractmethod
    def aaa(self):
        print("aabbcc")
class abc02(abc):
    @abstractmethod
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc()
    obj1.aaa()
    obj2 = abc03()
    obj2.aaa()
    obj2 = abc02() #it will give error
    obj2.aaa()
if __name__ == "__main__":
    main()
# das
# aabbcc
# class abc03
# TypeError: Can't instantiate abstract class abc02 with abstract methods aaa
======================================
from abc import ABC, abstractmethod

class abc(ABC):  #ERROR IS COMING BECAUSE ABS IS THERE IN ARGUMENT
    #@abstractmethod
    def aaa(self):
        print("aabbcc")
class abc02(abc):
    @abstractmethod  #ERROR IS COMING BECAUSE ABS IS THERE IN ARGUMENT
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()

    obj2 = abc02() #it will give error
    obj2.aaa()

if __name__ == "__main__":
    a1 = abc()
    main()
#aabbcc
#class abc03
#TypeError: Can't instantiate abstract class abc02 with abstract methods aaa
=================================
from abc import ABC, abstractmethod

class abc(ABC):  #ERROR IS COMING BECAUSE ABC IS THERE IN ARGUMENT
    #@abstractmethod
    def aaa(self):
        print("aabbcc")
class abc02(abc):
    @abstractmethod
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():

    a1.aaa() #we have created obj
    obj2 = abc03()
    obj2.aaa()
    obj2 = abc02() #it will give error
    obj2.aaa()
if __name__ == "__main__":
    a1 = abc()
    main()
# TypeError: Can't instantiate abstract class abc02 with abstract methods aaa
# aabbcc
# class abc03
=================================
class abc:
    def aaa(self):
        pass
class abc02(abc):
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc()
    obj1.aaa()
if __name__ == "__main__":
    a1 = abc() #NOT NECESSARY as it wont do anything
    main()
#NO OUTPUT
================================
class abc:
    def aaa(self):
        pass
class abc02(abc):
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    a1 = abc() #NOT NECESSARY as it wont do anything
    main()
#class abc03
===============================
class abc:
    def aaa(self):
        pass
class abc02(abc):
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaab(self):
        print("class abc03")
def main():
    obj1 = abc03()
    obj1.aaa()
if __name__ == "__main__":
    a1 = abc() #NOT NECESSARY as it wont do anything
    main()
#No output
=================================
class abc:
    def aaa(self):
        print("djfjd")
class abc02(abc):
    def aab(self):
        print("class abc02")
class abc03(abc):
    def aaab(self):
        print("class abc03")
def main():
    obj1 = abc03()
    obj1.aab()
if __name__ == "__main__":
    a1 = abc() #NOT NECESSARY as it wont do anything
    main()
#AttributeError: 'abc03' object has no attribute 'aab'
================================
class abc:
    def aaa(self):
        print("djfjd")
class abc02(abc):
    def aab(self):
        print("class abc02")
class abc03(abc):
    def aaab(self):
        print("class abc03")
def main():
    obj1 = abc03()
    obj1.aaa()
if __name__ == "__main__":
    a1 = abc() #NOT NECESSARY as it wont do anything
    main()
#djfjd
=================================
class abc:
    def aaa(self):
        print("method aaa")
class abc02(abc):
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaab(self):
        print("class abc03")
def main():
    obj1 = abc03()
    obj1.aaa()
if __name__ == "__main__":
    a1 = abc() #NOT NECESSARY as it wont do anything
    main()
#method aaa
=================================
class abc:
    print("fkf")
    def aaa(self):
        print("method aaa")
class abc02(abc):
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaab(self):
        print("class abc03")
def main():
    obj1 = abc03()
    obj1.aaa()
if __name__ == "__main__":
    a1 = abc() #NOT NECESSARY as it wont do anything
    main()
# fkf
# method aaa
=================================
class abc:
    print("fkf")
    def aaa(self):
        print("method aaa")
class abc02(abc):
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaab(self):
        print("class abc03")
def main():
    obj1 = abc03()
    obj1.aaa()
if __name__ == "__main__":
    pass
    #a1 = abc() #NOT NECESSARY as it wont do anything
    #main()
#fkf
=================================
class abc:
    print("fkf")
    def aaa(self):
        print("method aaa")
class abc02(abc):
    def aaa(self):
        print("class abc02")
class abc03(abc02):
    def aaab(self):
        print("class abc03")
def main():
    obj1 = abc03()
    obj1.aaa()
if __name__ == "__main__":
    a1 = abc() #NOT NECESSARY as it wont do anything
    main()
# fkf
# class abc02
=================================
class abc:
    def aaa(self):
        pass
class abc02(abc):
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc03()
    obj1.aaa()
if __name__ == "__main__":
    a1 = abc() #NOT NECESSARY as it wont do anything
    main()
#class abc03
================================
 class abc:
    def aaa(self):
        print("aabbc")
class abc02(abc):
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aab(self):
        print("class abc03")
def main():
    obj1 = abc()
    obj1.aaa()
    obj1.aab() #error

if __name__ == "__main__":
    a1 = abc() #NOT NECESSDARE as it wont do anything
    main()
#aabbc
#AttributeError: 'abc' object has no attribute 'aab'
=================================
class abc:
    def aaa(self):
        print("aabbc")
class abc02(abc):
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aab(self):
        print("class abc03")
def main():
    obj1 = abc03()
    obj1.aaa()
    obj1.aab()

if __name__ == "__main__":
    a1 = abc() #NOT NECESSDARE as it wont do anything
    main()
#aabbc
#class abc03
=================================
from abc import ABC, abstractmethod
class abc(ABC):
    @abstractmethod
    def aaa(self):
        pass
class abc02(abc):
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    #a1 = abc()
    main()
#class abc02
#class abc03
=====================================
from abc import ABC, abstractmethod

class abc(ABC):
    print("aaa")
    @abstractmethod
    def aaa(self):
        pass
class abc02(abc):
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    #a1 = abc()
    main()
# aaa
# class abc02
# class abc03
=====================================
from abc import ABC, abstractmethod

class abc(ABC):
    @abstractmethod
    def aaa(self):
        pass
class abc02(abc):
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    #a1 = abc() #iT WILL GIVE ERROR
    main()
#class abc02
#class abc03
=====================================
from abc import ABC, abstractmethod

class abcd(ABC):
    @abstractmethod
    def __init__(self):
        print("aaa")
    def aaa(self):
        pass
class abc02(abcd):
    def __init__(self):
        print("zzz")
    def __init__(self):
        print("xxx")
    def aaa(self):
        print("class abc02")
class abc03(abcd):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()
if __name__ == "__main__":
    main()
#xxx
#class abc02
===================================
from abc import ABC, abstractmethod

class abcd(ABC):
    @abstractmethod
    def __init__(self):
        print("aaa")
    def aaa(self):
        pass
class abc02(abcd):
    def __init__(self):
        print("zzz")
    def __init__(self):
        print("xxx")
    def aaa(self):
        print("class abc02")
class abc03(abcd):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()
if __name__ == "__main__":
    obj2 = abcd()
    main()
#TypeError: Can't instantiate abstract class abcd with abstract methods __init__
===================================
from abc import ABC, abstractmethod

class abcd(ABC):
    @abstractmethod
    def __init__(self):
        print("aaa")
    def aaa(self):
        pass
class abc02(abcd):
    def __init__(self):
        print("zzz")
    def __init__(self):
        print("xxx")
    def aaa(self):
        print("class abc02")
class abc03(abcd):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()
if __name__ == "__main__":
    obj2 = abcd()
    obj2.aaa()
    main()
#TypeError: Can't instantiate abstract class abcd with abstract methods __init__
===================================
from abc import ABC, abstractmethod

class abcd(ABC):
    @abstractmethod
    def __init__(self):
        print("aaa")
    def aaa(self):
        pass
class abc02(abcd):
    def __init__(self):
        print("zzz")
    def __init__(self):
        print("xxx")
    def aaa(self):
        print("class abc02")
class abc03(abcd):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    #obj2 = abcd() #TypeError: Can't instantiate abstract class abcd with abstract methods __init__
    #obj2.aaa() #erroe
if __name__ == "__main__":
    main()
#xxx
#class abc02
===================================
from abc import ABC, abstractmethod

class abc(ABC):
    @abstractmethod
    def aaa(self):
        pass
class abc02():
    @abstractmethod
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    #a1 = abc()
    main()
#class abc02
#class abc03
======================
from abc import ABC, abstractmethod

class abc(ABC):
    @abstractmethod
    def aaa(self):
        print("vfudgyu")
class abc02():
    @abstractmethod
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    #a1 = abc()
    main()
# class abc02
# class abc03
======================
from abc import ABC, abstractmethod

class abc(ABC):
    @abstractmethod
    def aaa(self):
        pass
class abc02(abc):
    @abstractmethod
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    #a1 = abc()
    main()
#good example
# obj1 = abc02()
#TypeError: Can't instantiate abstract class abc02 with abstract methods aaa
=======================
from abc import ABC, abstractmethod

class abc():
    @abstractmethod
    def aaa(self):
        print("dghd")
class abc02(abc):
    @abstractmethod
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    #a1 = abc()
    main()
# class abc02
# class abc03
=======================
from abc import ABC, abstractmethod

class abc():
    @abstractmethod
    def aaa(self):
        pass
class abc02(abc):
    @abstractmethod
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    #a1 = abc()
    main()
#class abc02
#class abc03
===============================
from abc import ABC, abstractmethod

class abc(ABC):
    #@abstractmethod
    def aaa(self):
        pass
class abc02(abc):
    @abstractmethod
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    #a1 = abc()
    main()
#TypeError: Can't instantiate abstract class abc02 with abstract methods aaa
==================================
from abc import ABC, abstractmethod

class abc():
    #@abstractmethod
    def aaa(self):
        pass
class abc02(abc):
    @abstractmethod
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    #a1 = abc()
    main()
# class abc02
# class abc03
==================================
from abc import ABC, abstractmethod

class abc():
    #@abstractmethod
    def aaa(self):
        print("jdvjd")
class abc02(abc):
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    #a1 = abc() #iT WILL GIVE ERROR
    main()
#class abc02
#class abc03
=========================
from abc import ABC, abstractmethod

class abc():
    #@abstractmethod
    def aaa(self):
        print("jdvjd")
class abc02(abc):
    def aaas(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    #a1 = abc() #iT WILL GIVE ERROR
    main()
#jdvjd
#class abc03
===========================
from abc import ABC, abstractmethod

class abc():
    #@abstractmethod
    def aaa(self):
        print("jdvjd")
class abc02(abc):
    def aaa(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()
    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    #a1 = abc() #iT WILL GIVE ERROR
    main()
# class abc02
# class abc03
===========================
from abc import ABC, abstractmethod

class abc(ABC):
    #@abstractmethod
    def aaa(self):
        print("jdvjd")
class abc02(abc):
    def aaas(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    #a1 = abc() #iT WILL GIVE ERROR
    main()
#jdvjd
#class abc03
==============================
from abc import ABC, abstractmethod

class abc(ABC):
    @abstractmethod
    def aaa(self):
        print("jdvjd")
class abc02(abc):
    def aaas(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    #a1 = abc() #iT WILL GIVE ERROR
    main()
#TypeError: Can't instantiate abstract class abc02 with abstract methods aaa
==============================
from abc import ABC, abstractmethod

class abc(ABC):
    @abstractmethod
    def aaa(self):
        print("jdvjd")
class abc02(abc):
    def aaas(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    #a1 = abc() #iT WILL GIVE ERROR
    main()
#TypeError: Can't instantiate abstract class abc02 with abstract methods aaa
=================================
from abc import ABC, abstractmethod
class abc():
    @abstractmethod
    def aaa(self):
        print("jdvjd")
class abc02(abc):
    def aaas(self):
        print("class abc02")
class abc03(abc):
    def aaa(self):
        print("class abc03")
def main():
    obj1 = abc02()
    obj1.aaa()

    obj2 = abc03()
    obj2.aaa()
if __name__ == "__main__":
    #a1 = abc() #iT WILL GIVE ERROR
    main()
# jdvjd
# class abc03
