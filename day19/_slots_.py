#-*- coding:utf-8 -*-
#python可以动态绑定属性，包括变量和方法
#通过_slots_变量可以实现固定变量，无法增加其他变量

class Student(object):
	pass
s=Student()
s.name= 'djx'
print(s.name)
#s2=Student()
#print(s2.name) 另一个实例变量没有name变量

def setAge(self,age):
	self.age = age
s.setAge = setAge #实力变量绑定方法，另一变量没有此方法
Student.setAge = setAge #向类中增加方法
s3= Student()
s3.setAge(25)	#此时s3增加了age变量，并赋值25
print(s3.age)

class Student(object):
	__slots__=('name','age') #用turple定义绑定的属性名称
s4 = Student()
s4.name = 'djx'
s4.age = 16
#s4.score = 98 无法绑定score变量，因为_slots_变量限制了只能绑定两个变量
print(s4.age)
