# -*- coding: utf-8 -*-

# 利用递归函数移动汉诺塔: 
def move(n,a,b,c):
	# 如果是最底下一块，则a->c
	if n==1:
		print('move',a,'->',c)
		return
	
	# 第一部分, 将n-1(除了最后一块的盘)从a列通过c列都移到b列上
	move(n-1,a,c,b)
	print('move',a,'->',c)
	
	# 第二部分，将n-1(除了最后一块的盘)从b列通过a列都移到c列上
	move(n-1,b,a,c)
	
move(4,'A','B','C')


# 利用递归函数计算阶乘 
# N! = 1 * 2 * 3 * ... * N 
def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)

m=int(input('请输入计算的乘阶：'))
print('fact(%d)=%d' %(m,fact(m)))


# 利用递归函数计算阶乘 
# N! = 1 * 2 * 3 * ... * N 
# 尾递归优化
# def fact_2(n):
	# return fact_inner(n,1)

# def fact_inner(num, product):
	# if num==1:
		# return product
	# return fact_inner(num-1, num*product)
	
# m=int(input('请输入计算的乘阶：'))
# print('fact(%d)=%d' %(m,fact_2(m)))
	
	

