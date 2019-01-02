#-*- coding:utf-8 -*-
class Student(object):
	def __init__(self,name=None,score=0):
		self.name=name
		self.score=score
	def printScore(self): #必须包含参数self
		print('%s: %s'% (self.name,self.score))
djx=Student()
#djx.name='dengjiaxin'	#python实例变量允许绑定任意属性变量
print(djx.name)
lxx=Student('laoxixin',100)
print(lxx.score)

lxx.printScore()
