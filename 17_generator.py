# -*- coding: utf-8 -*-

#定义斐波拉契数列
def fib(max):
	n,a,b=0,0,1
	while n<max:
		print(b)
		a,b=b,a+b
		n=n+1
	return 'done'
	
print(fib(3))

#定义generator斐波拉契数列
#generator和函数的执行流程不一样。
#函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
#而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

def fib_g(max):
	n,a,b=0,0,1
	while n<max:
		yield b
		a,b=b,a+b
		n=n+1
	return 'done'
	
for n in fib_g(6):
	print(n)

#generator下生成斐波那契数列	
g = fib_g(6)
print('\n')
#构成循环
while True:
	#异常抓取
	try:
		x=next(g)
		print('g:', x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break

#练习：杨辉三角
def triangeles():
	L=[1]
	while True:
		yield L
		L1=[0]+L
		L2=L+[0]
		#L=[L[i]+L1[i] for i in range(len(L)))]+[1]
		L=L1+L2

for t in triangeles():
	print(t)
	n=n+1
	if n==10:
		break