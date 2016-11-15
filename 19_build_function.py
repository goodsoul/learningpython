# -*- coding: utf-8 -*-

def minus(x,y,f):
	return f(x)+f(y)
	
x=float(input('Please input number1: '))
y=float(input('Please input number2: '))
#变量f现在已经指向了abs函数本身。
#直接调用abs()函数和调用变量f()完全相同。
f=abs
print('f(%.2f)+f(%.2f)=%.2f' %(x,y,minus(x,y,f)))