#-*- coding:utf-8 -*-
print(type(123))	#type判断对象类型

print(type('abc')==type(123)) #判断对象是否相同
import types
def fn():	#测试函数
	pass
a = type(fn)==types.FunctionType
b = type(abs)==types.BuiltinFunctionType
c = type(lambda x:x)==types.LambdaType
d = type((x for x in range(10)))==types.GeneratorType
#优先使用isinstance

print(a,b,c,d)

#dir()函数
#print(dir('abv'))

class myClass(object):
	def __len__(self): #__***__方法在函数内部时，会自动调用该对象的方法
		return 100
dog = myClass()
print(len(dog)) #等价于len(dog) = dog.__len__()

print(len('123'))

#getattr() setattr() hasattr()的用法
class myObject(object):
	def __init__(self):
		self.x=9
	def power(self):
		return self.x * self.x

obj = myObject()
a = hasattr(obj,'x')	#有变量x吗？,相当于obj.x
b = setattr(obj,'y',19)	#设置变量y
c = getattr(obj,'y')
d = getattr(obj,'z', 404) #获取不存在变量时，抛出AttributeError异常可以修改默认值，抛出404'''
print(a,b,c,d)

fn = getattr(obj,'power') #获取power
print(fn())
