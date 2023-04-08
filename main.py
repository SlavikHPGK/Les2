class Cat:
    def __init__(self,name):
        self.name = name

    def play(self,person):
        print("Ovdje je maczka", person.name)
        person.isHappy = True

class Person:
    isHappy = False

    def __init__(self,name,age):
        self.name = name
        self.age = age

me = Person("Hrvat", 22)
my_cat = Cat("Ovo")
friend = Person("Srbin", 31)
my_cat.play(me)
my_cat.play(friend)
print(me.isHappy)
