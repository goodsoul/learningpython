# -*- coding: utf-8 -*-
import math

#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
#ax2 + bx + c = 0
#求根公式 x=(-b+/-sqrt(b*b-4ac))/2a

def quadratic(a, b, c):
	# if not (isinstance(a,(int,float))|isinstance(b,(int,float))):
		# raise TypeError("Please input number!")
	if a==0:
		x1=x2="a should not be zero!"
		return x1
	if (b*b-4*a*c)<0:
		x1=x2="No root!"
		return x1
	else:
		x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
		x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
		return x1,x2

a=float(input("Please input a:"))
b=float(input("Please input b:")) 
c=float(input("Please input c:"))
print (quadratic(a, b, c))
# print(quadratic(9, 1, 1))
# print(quadratic(1, 3, -4))


