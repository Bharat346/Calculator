import random as rd 

class person:
    def __init__(self,name,age):
        self.name = name
        self.Age = age 
    def info(self):
        print(f"my name is {self.name} and {self.Age} years old")

a = person("Bharat",17)
print(a.info())

