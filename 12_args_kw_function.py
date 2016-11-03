# -*- coding: utf-8 -*-

# Summary:
# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
# 要注意定义可变参数和关键字参数的语法：
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。
# 以及调用函数时如何传入可变参数和关键字参数的语法：
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。

# args
def hello(greeting, *args):
	if (len(args)==0):
		print('%s!' %greeting)
	else:
		print('%s,%s!' %(greeting,','.join(args)))

# 调用
hello('Hi') # => greeting='Hi', args=() 
hello('Hi', 'Sarah') # => greeting='Hi', args=('Sarah') 
hello('Hello', 'Michael', 'Bob', 'Adam') # => greeting='Hello', args=('Michael', 'Bob', 'Adam') 

names = ('Bart', 'Lisa') 
hello('Hello', *names) # => greeting='Hello', args=('Bart', 'Lisa') 

# kw
def print_score(**kw):
	print('name	score')
	print('----------')
	for name, score in kw.items():
		print('%s	%d' %(name,score))
	print()

# 调用
print_score(Adam=100, Lisa=99, Bart=90, Bill=95)

data={
	'Adam':100,
	'Lisa':99,
	'Bart':90,
	'Bill':95
}
print_score(**data)

# 复合参数(命名关键参数)
def print_info(name,*,gender,city='Shanghai',age):
	print('Peronsal Info')
	print('-------------')
	print('Name:%s' %name)
	print('Gender:%s' %gender)
	print('City:%s' %city)
	print('Age: %s' %age)
	print()

# 没有关键字会报错
#print_info()

print_info('Bill',gender='male',age=28)
print_info('Regina',gender='female',city='Beijing',age=27)

# x的n次方
def power(x,n=2):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s

# 1的n次方累加到m的n次方
def total_add(x,m):
	s=0
	n=1
	while n<=x:
		s=s+power(n,m)
		n=n+1
	return s

a=int(input('请输入累加次数：'))
b=int(input('请输入每项的幂：'))
print('从1的%d次方累加到%d的%d次方的和是：%d'  %(b,a,b,total_add(a,b)))
	
	
		
		
	