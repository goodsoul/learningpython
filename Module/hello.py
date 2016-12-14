#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#以内建的sys模块为例，编写一个hello的模块：

'a test module'

__author='bill ye'

import sys

def test():
	#sys模块有一个argv变量，用list存储了命令行的所有参数。
	#运行python3 hello.py获得的sys.argv就是['hello.py']；
	#运行python3 hello.py Michael获得的sys.argv就是['hello.py', 'Michael]。
	
	args=sys.argv
	if len(args)==1:
		print('Hello, world!')
	elif len(args)==2:
		print('Hello, %s!' %args[1])
	else:
		print('Too many arguments!')
		
if __name__=='__main__':
	test()

#python hello.py
#python hello.py Bill
#python hello.py Bill Test
	
#正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等
#类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途
#类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用