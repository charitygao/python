# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#封装 使用构造方法将内容封装到对象中 然后通过对象直接或self间接获取被封装的内容
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def detail(self):
        print (self.name)
        print (self.age)
    
p1 = Person('test',24)
print (p1.name)
print (p1.age)
#>>>>>>>>>
p1.detail()