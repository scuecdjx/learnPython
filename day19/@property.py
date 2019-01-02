#-*- coding:utf-8 -*-
'''
用@property来防止属性暴露，并增加参数检验的功能
'''
class Student(object):
	pass
s= Student()
s.score = 9999 #代码没问题，但是不符合逻辑
class Student(object):
	def getScore(self):
		return self.score
	def setScore(self,score):
		if not isinstance(score,int): #如果分数不是
			raise ValueError('score must be an integer')
		if score<0 or score>100:
			raise ValueError('score must between 0~100')
		self.score = score
s2 = Student()
#s2.setScore('900') 错误
s2.setScore(90)
print(s2.getScore())
#使用@property实现直接绑定变量并检查参数
class Student(object):

	@property
	def score(self): #注意方法名称和变量名称不能一样
		return self._score
	@score.setter
	def score(self,value):
		if not isinstance(value,int): #如果分数不是
			raise ValueError('score must be an integer')
		if value<0 or value>100:
			raise ValueError('score must between 0~100')
		self._score = value
s3 = Student()
s3.score = 60 #没问题,实际调用（s3.setScore(60)）
print(s3.score) #虽然实例变量没有属性score，但是实际是调用（s3.getScore）

class Student(object):
	@property
	def birth(self):
		return self._birth
	@birth.setter
	def birth(self,value):
		self._birth = value
	@property #只设置get
	def age(self):
		return 2018-self._birth
s4 = Student()
s4.birth = 1997
#s4.age = 18 #会报错，因为没有设置setAge方法
print(s4.age)

#练习
#利用@property给Screen对象加上width和height，并设置只读变量resolution
class Screen(object):
#@property必须在前面，不然无法设置下面的函数
	@property
	def width(self):
		return self._width
	@width.setter
	def width(self,value):
		self._width = value
	@property
	def height(self):
		return self._height
	@height.setter
	def height(self,value):
		self._height = value
	@property
	def resolution(self):
		return self._width * self._height

#测试
s= Screen()
s.width = 1024
s.height = 768
print('resolution = %d'%s.resolution)
if s.resolution == 786432:
	print('yes')
else:
	print('no')
