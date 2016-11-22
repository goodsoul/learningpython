# -*- coding: utf-8 -*-

#算素数的一个方法是埃氏筛法

#可以先构造一个从3开始的奇数序列
def _odd_iter():
	n=1
	while True:
		n=n+2
		yield n

#然后定义一个筛选函数		
def _not_divisble(n):
	#lambda的一般形式是关键字lambda后面跟一个或多个参数，紧跟一个冒号，以后是一个表达式。
	#f = lambda x,y,z : x+y+z  
	#print f(1,2,3)  
	return lambda x:x%n>0

#最后，定义一个生成器，不断返回下一个素数
def primes():
	yield 2
	it = _odd_iter() # 初始序列
	while True:
		n= next(it)  # 返回序列的第一个数
		yield n
		it = filter(_not_divisble(n),it) # 构造新序列

#调用时需要设置一个退出循环的条件
for n in primes():
	if n<1000:
		print(n)
	else:
		break
	
	