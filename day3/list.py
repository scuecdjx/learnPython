#-*- coding=utf-8 -*-
classmates=['Michael','Bob','Tracy']
print(classmates[0])
a=len(classmates)#获取长度
print(a)
print(classmates[-1])#-1为索引直接获取最后一个元素
print(classmates[-2])
classmates.append('Adam')#末尾插入
classmates.insert(2,'Jack')
print(classmates)
classmates.pop()#删除末尾
classmates.pop(2)
print(classmates)

L=['abc','123','True']
s=['a','b',['g','h'],'d']
print(len(s))

