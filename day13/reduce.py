#-*- coding:utf-8 -*-
#reduce为累计效果
#e.g.
from functools import reduce
def add(x,y):
	return x+y
a=reduce(add,[1,3,5,7,9]) #累加
print(a)
def fn(x,y):
	return x*10+y
print(reduce(fn,[1,3,5,7,9])) #将[1,3,5,7,9]变为13579

#配合map
def charNum(s):
	d={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,
	'6':6,'7':7,'8':8,'9':9}
	return d[s]
num=reduce(fn,map(charNum,'13579'))
print num

#利用lamda函数简化
def strInt(s):
	return reduce(lambda x,y:x*10+y,map(charNum,s))
#test
a='12345'
b=strInt(a)
print b

#练习
#将用户输入的不规范英文名字，变为首字母大写，其他小写的规范名字
#['adam','LISA','barT']输出['Adam','Lisa','Bart']

def normalName(name):
	s=str.upper(name[:1])+str.lower(name[1:])
	return s
#test
L1=['adam','LISA','barT']
L2=list(map(normalName,L1))
print(L2)

#编写一个prod()函数，可以吉首一个list并利用reduce求积
def prod(L):
	return reduce(g,L)
	
def g(x,y):
	return x*y

print('3*5*7*9=',prod([3,5,7,9]))
if prod([3,5,7,9])!=945:
	print 'lose'
else:
	print 'yes'

#利用map和reduce将字符串‘123.456’转换成123.456
def strFloat(s):
	

#test
if abs(strFloat('123.456')-123.456)<0.00001:
	print 'yes'
else:
	print 'lose'
