#-*- coding:utf-8 -*-
def now():
	print('2018/10/13')

print(now.__name__)
#在代码运行期间动态增加功能的方式，叫装饰器
def log(func):
	def wrapper(*args,**kw):
		print('call %s():'%func.__name__)
		return func(*args,**kw)
	return wrapper

@log 	#相当于now=log(now)
def now():
	print('2018-10-13')

print(now())

