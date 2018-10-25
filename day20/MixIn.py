#-*- coding:utf-8 -*-
'''
多重继承的用法
'''
class Animal(object): #动物
	pass

class Mammal(Animal): #哺乳动物
	pass

class Bird(Animal): #鸟类动物
	pass

class Runnable(object):
	def run(self):
		print('Running....')
class Flyable(object):
	def fly(self):
		print('flying...')

#定义一个狗类，它既是哺乳动物，也是跑步类
class Dog(Mammal,Runnable):
	pass

