#-*- coding:utf-8 -*-
#切片练习

L=['a','b','c','d']

#循环方式提取前三元素
r=[]
n=3
for i in range(n):
	r.append(L[i])
print(r)

#切片方式提取前三元素
print(L[0:3]) #取0，1，2元素
print(L[-3:-1]) #倒数切片，为0可以省略

#创建一个0-99的数列
nums=list(range(100))
print(nums[:10]) 	#前十个数
print(nums[-10:]) 	#后十个数
print(nums[10:20])	#10-19个数
print(nums[:10:2])	#前十个数，每2取一个
print(nums[::5])	#所有数每5个取一个数
n2=nums[:]		#复制
print((0,1,2,3,4,5)[:3]) #tuple也可以切片

'''利用切片，去除字符串首位的空格'''
def trim(s):
	n=len(s)
	str=s
	i=0
	j=-1
	count=0
	'''如果s的第i个为空格，
	且i+1个不为空格则取第i+1项以后'''
	while s[0]==' ' or s[-1]==' ':
	# 如果全部为空格，则输出‘ ’	
		if s[i]==' ':
			count+=1
		if count==len(s):
			s=' '
			break
	# 去前面的空格
		if s[i]==' ' and s[i+1]!=' ':
			s=s[i+1:len(s)] 
		i+=1
	# 去后面的空格
		if s[j]==' ' and s[j-1]!=' ':
			s=s[0:len(s)+j]
		j-=1
	return s
if trim('hello ')!='hello':
	print(False,1)
elif trim('  hello')!='hello':
	print(False,2)
elif trim('  hello  ')!='hello':
	print(False,3)
elif trim(' ')!=' ':
	print(False,4)
elif trim('    ')!=' ':
	print(False,5)
else:
	print(True)

