# -*- coding: utf-8 -*-

L = ['Bart', 'Lisa', 'Adam']

#请利用循环依次对list中的每个名字打印出Hello, xxx!
#用For循环	
for x in L:
	print('Hello, %s!' %x)
print('End')	
#用While循环		
x=n=len(L)
while n>0:
	a=x-n
	n=n-1
	print('Hello, %s!' %L[a])
print('End')

#Break & Continue		
x=n=len(L)
while n>0:
	a=x-n
	n=n-1
	if a==0:
		continue
		#break
	print('Hello, %s!' %L[a])
print('End')	
	
