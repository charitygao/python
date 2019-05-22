# -*- coding: utf-8 -*-
"""
Created on Wed May 22 22:02:55 2019

@author: 19056
"""

#继承 子继承父的某些特性
class Animal:
    def eat(self):
        print ("%s 吃 " %self.name)
    def drink(self):
        print ("%s 喝 " %self.name)
    def shit(self):
        print ("%s 拉 " %self.name)
    def pee(self):
        print ("%s 撒 " %self.name)

class Cat(Animal):
    def __init__(self,name):
        self.name = name
    def cry(self):
        print ("喵喵叫！！！")
    
class Dog(Animal):
    def __init__(self,name):
        self.name = name
    def cry(self):
        print ("汪汪叫！！！")
        
c = Cat("猫儿")
c.eat()
c.cry()

d = Dog("狗儿")
d.eat()
d.cry()




