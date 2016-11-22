# -*- coding: utf-8 -*-

#算回数

#构造一个无限序列
def _list_iter():
	n=1
	while True:
		n=n+1
		yield n

#然后定义一个筛选函数		
def _is_palindrome(n):
	return lambda n:str(n)==str(n)[::-1] #正序=倒序

#最后，定义一个生成器，不断返回下一个素数
def primes():
	it = _list_iter() # 初始序列
	while True:
		n= next(it)  # 返回序列的第一个数
		yield n
		it = filter(_is_palindrome(n),it) # 构造新序列

#调用时需要设置一个退出循环的条件
for n in primes():
	if n<1000:
		print(n)
	else:
		break
	
	