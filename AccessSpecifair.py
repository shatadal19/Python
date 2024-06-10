# class Employ:
#    def __init__(self):
#       self.__name = "Shatadal"

# a = Employ()
# print(a._Employ__name) #Can be access indirectly

class Student:
    def __init__(self):
        self.name =  "Shatadal"


    def _funName(self):
     return "CoderBeen"
    
class Subject(Student):
   pass

obj = Student()
print(obj.name)
print(obj._funName())
obj1 = Subject()
print(obj1.name)
print(obj1._funName())
    