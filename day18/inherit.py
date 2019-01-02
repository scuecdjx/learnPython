#-*- coding:utf -*-
class Animal(object):
	def run(self):
		print('Animals is running...')
class Dog(Animal): #继承份父类，Animal
	def run(self):	#覆盖父类方法，称为多态
		print('Dog is running...')
	def eat(self): #可以增加新方法
		print('Eating meat...')
dog =Dog() #实例化对象
dog.run()
dog.eat()
	
#可以用isinstance判断类型
print(isinstance(Animal,object)) #True

print(isinstance(Dog,Animal)) #False
print(isinstance(dog,Dog)) #True
print(isinstance(dog,Animal))  #True

