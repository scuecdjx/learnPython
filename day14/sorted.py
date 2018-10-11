#-*- coding:utf-8 -*-
#排序函数
L=sorted([36,5,-12,9,-21])
print L

#sorted也是高阶函数，可以传入函数参数
L1=sorted(L,key=abs)
print L1

s=sorted(['bob','about','Zoo','Crime'])
print s

#不区分大小写排序
s1=sorted(s,key=str.lower)
print s1
#逆序排序
s2=sorted(s,key=str.lower,reverse=True)
print s2

#对列表按名字排序
L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
def byName(t):
	return t[0]
L2=sorted(L,key=byName)
print(L2)

#对分数进行排序
def byScore(t):
	return t[1] #返回第二个数
L3=sorted(L,key=byScore)
print(L3)
