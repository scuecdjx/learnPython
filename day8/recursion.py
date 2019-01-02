# -*-coding:utf-8 -*-
#递归函数计算阶乘
def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)
print(fact(5))
print(fact(10))

#尾递归处理防止栈溢出
def fact(n):
	return fact_iter(n,1)

def fact_iter(num,t): #t用来保存调用后的结果
	if num==1:
		return t
	return fact_iter(num-1,num*t)
print(fact(6))

#汉诺塔练习题
def move(n,a,b,c):
	if n!=0:	#当有盘子未完成移动时
		move(n-1,a,c,b)	#将n-1个盘子由a移到b，c为辅助
		print(a,'to',c) #将a最后一个盘子移到c
		move(n-1,b,a,c) #将b上所有盘子的n-1个移到c，a为辅助
move(3,'a','b','c')
