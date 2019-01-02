#-*- coding:utf-8 -*-
class Student(object):
	name = 'Student' #Student本身的属性
	def __init__(self,name):
		self.name = name
s= Student('djx')
s.score = 90	#实例对象可以任意绑定变量
print(s.name,s.score)
del s.name 	#删除s的name属性
print(s.name,s.score)

#练习
'''
为了统计人数，可以给Student变量增加一个类属性，每
创建一次实例，该属性+1
'''
class Student(object):
	count = 0
	def __init__(self,name=None):
		Student.count +=1
		self.name = name
# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
