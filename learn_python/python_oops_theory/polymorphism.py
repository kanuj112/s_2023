===================
Polymorphism :=====
===================
1. Polymorphism means that different types respond to the same function.
2. Polymorphism is based on the greek words Poly (many) and morphism (forms)
3. Polymorphism is the ability to leverage the same interface for different underlying forms such as data
types or classes. This permits functions to use entities of different types at different times.
4. Polymorphism is an important feature of class definition in Python that is utilized when you 
have commonly named methods across classes or subclasses. This allows functions to use objects of
any of these polymorphic classes without needing to be aware of distinctions across the classes.
5. Sometimes an object comes in many types or forms. If we have a button, there are many different draw outputs
(round button, check button, square button, button with image) but they do share the same logic: onClick().  
 We access them using the same method . This idea is called Polymorphism.

Polymorphism with a function:
================================

class dog():
    def sound(self):
        print("bark")
class cat():
    def sound(self):
        print("meow")
def animal(animaltype):
    animaltype.sound()
obj1 = dog()
obj2 = cat()
animal(obj1)
animal(obj2)

#bark
#meow
===============================
class dog():
    def sound():
        print("bark")
class cat():
    def sound(self):
        print("meow")
def animal(animaltype):
    animaltype.sound()
obj1 = dog()
obj2 = cat()
animal(obj1)
animal(obj2)
#TypeError: sound() takes 0 positional arguments but 1 was given

Polymorphism with abstract class:
=================================
1. If you create an editor you may not know in advance what type of documents a user will 
open (pdf format or word format?).  
2. To do so, we create an abstract class called document.
This class does not have any implementation but defines the structure (in form of functions) that all 
forms must have.   If we define the function show()  then both the PdfDocument and 
WordDocument must have the show() function

class Document:
    def __init__(self, name):    
        self.name = name
 
    def show(self):             
        raise NotImplementedError("Subclass must implement abstract method")
class Pdf(Document):
    def show(self):
        return 'Show pdf contents!'
class Word(Document):
    def show(self):
        return 'Show word contents!'
documents = [Pdf('Document1'),
             Pdf('Document2'),
             Word('Document3')]
for document in documents:
    print document.name + ': ' + document.show()

output ==>
Document1: Show pdf contents!
Document2: Show pdf contents!
Document3: Show word contents!

=================================
class Shark():
    def swim(self):
        print("The shark is swimming.")

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")

    def skeleton(self):
        print("The shark's skeleton is made of cartilage.")


class Clownfish():
    def swim(self):
        print("The clownfish is swimming.")

    def swim_backwards(self):
        print("The clownfish can swim backwards.")

    def skeleton(self):
        print("The clownfish's skeleton is made of bone.")

sammy = Shark()
sammy.skeleton()
casey = Clownfish()
casey.skeleton()

#The shark's skeleton is made of cartilage.
#The clownfish's skeleton is made of bone.
==================================
class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi the primary language of India.")

    def type(self):
        print("India is a developing country.")


class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")
obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()

#New Delhi is the capital of India.
#Hindi the primary language of India.
#India is a developing country.
#Washington, D.C. is the capital of USA.
#English is the primary language of USA.
#USA is a developed country.
=======================================
class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")
class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")
class ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()
obj_bird.intro()
obj_bird.flight()
obj_spr.intro()
obj_spr.flight()
obj_ost.intro()
obj_ost.flight()

#There are many types of birds.
#Most of the birds can fly but some cannot.
#There are many types of birds.
#Sparrows can fly.
#There are many types of birds.
#Ostriches cannot fly
======================================
class India():
    def capital(self):
        print("New Delhi is the capital of India.")
    def language(self):
        print("Hindi the primary language of India.")
    def type(self):
        print("India is a developing country.")
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
    def language(self):
        print("English is the primary language of USA.")
    def type(self):
        print("USA is a developed country.")
def func(obj):
    obj.capital()
    obj.language()
    obj.type()
obj_ind = India()
obj_usa = USA()
func(obj_ind)
func(obj_usa)

#New Delhi is the capital of India.
#Hindi the primary language of India.
#India is a developing country.
#Washington, D.C. is the capital of USA.
#English is the primary language of USA.
#USA is a developed country.

================================


