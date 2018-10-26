#-*- coding:utf-8 -*-
#枚举类的运用

from enum import Enum
Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)

from enum import unique

@unique #unique的作用可以检查有没有重复值
class Weekday(Enum):
    Sun = 0 #自定义value的值
    Mon = 1
    Tue = 2
print(Weekday.Mon)
print(Weekday.Sun.value)
print(Weekday(1))

#练习
class Gender(Enum):
    Male = 0
    Female = 1
class Student(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
#测试
djx = Student('djx',Gender.Male)
if djx.gender == Gender.Male:
    print('yes')
else:
    print('no')
