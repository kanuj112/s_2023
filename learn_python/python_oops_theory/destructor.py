==========================
===========================
=========destructor========
===========================
==>Destructors are called when an object gets destroyed. In Python, destructors are not needed as 
much needed in C++ because Python has a garbage collector that handles memory management automatically.
The __del__() method is a known as a destructor method in Python. It is called when all references to the
object have been deleted i.e when an object is garbage collected.
==>Destructors are called when an object gets destroyed. It’s the polar opposite of the constructor, which gets called on creation.
==>These methods are only called on creation and destruction of the object. They are not called manually but completely automatic. 

1. The destructor is defined using __del__(self).
2. The obj is created and manually deleted, therefore, both messages will be displayed.
3. However, if you comment out the last line ‘del obj’, the destructor will not be called immediately.
4. Instead, the Garbage Collector (GC) will take care of the deletion automatically.
5. If you raise an exception in the destructor, it will be ignored.
6. In Python, destructors are needed much less, because Python has a garbage collector that 
handles memory management
====================================
class TestClass:
    def __init__(self):
        print("constructor")
    def __del__(self):
        print("destructor")
obj = TestClass()
del obj
#constructor
#destructor
==================================
class TestClass:
    def __init__(self):
        print("constructor")
    def __del__(self):
        print("destructor")
obj = TestClass()
#del obj

#constructor
#destructor
==================================
class TestClass:
    def __init__(self):
        print("constructor")
    def __del__(self):
        print("destructor")
obj1 = TestClass()
del obj1
obj1 = TestClass()
#constructor
#destructor
#constructor
#destructor
===============================
class TestClass:
    def __init__(self):
        print("constructor")
    def __del__(self):
        print("destructor")
obj1 = TestClass()
del obj1
obj1 = TestClass()

#constructor
#destructor
#constructor
#destructor
===============================
class TestClass:
    def __init__(self):
        print("constructor")
    def __del__(self):
        print("destructor")
        raise Exception("raise")
obj = TestClass()
del obj
#constructor
#destructor
#Exception ignored in: <function TestClass.__del__ at 0x00DCA4B0>
