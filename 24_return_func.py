# -*- coding: utf-8 -*-

#高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回

def lazy_sum(*args):
	def sum():
		ax=0
		for n in args:
			ax=ax+n
		return ax
	return sum

f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())

def count():
	def f(j):
		def g():
			return j*j
		return g
	fs=[]
	for i in range(1,4):
		fs.append(f(i))
	return fs
	
f1, f2, f3 = count()
print(f1, f2, f3)
print(f1())
print(f2())
print(f3())

#总结:
#一个函数可以返回一个计算结果，也可以返回一个函数。
#返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量

