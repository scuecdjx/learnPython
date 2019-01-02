#-*- coding:utf-8 -*-
class Student(object):
	def __init__(self,name,score):
		self.__name = name #内部属性前加__表示私有变量private
		self.__score = score
	 #通过内部方法来获取变量
	def getName(self): 
		return self.__name
	def getScore(self):
		return self.__name
	#通过内部方法外部设置变量
	def setName(self,name):
		self.__name=name
	def setScore(self,score):
		if 0<= score <=100: #可以检查参数
			self.__score=score
		else:	#抛出异常
			raise ValueError('bad score')

	def printSelf(self):
		print(self.getName(),self.__score)
djx = Student('dengjiaxin',80)
#djx.setScore(101)
djx.printSelf()

#练习
class Stu(object):
	def __init__(self,name,gender):
		self.name=name 
		self.__gender=gender #设置为私有变量
	def getGender(self):
		return self.__gender
	def setGender(self,gender):
		if gender == 'male' or 'female':
			self.__gender=gender
		else:
			raise ValueError('wrong gender')
#测试
lxx=Stu('lxx','female')
if lxx.getGender()!='female':
	print('lose')
else:
	lxx.setGender('male')
	if lxx.getGender()=='male':
		print('yes')
	else:
		print('lose')
