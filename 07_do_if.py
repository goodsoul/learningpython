# -*- coding: utf-8 -*-

def square(n):
	return n*n
	
height=input('Please input your height: ')
weight=input('Please input your weight: ')

# height = 1.75
# weight = 80.5

height=float(height)
weight=float(weight)

BMI=weight/square(height)
# print(BMI)

if BMI > 32:
	result='严重肥胖'
elif BMI > 28:
	result='肥胖'
elif BMI > 25:
	result='过重'
elif BMI > 18.5:
	result='正常'
else:
	result='过轻'

print('Your BMI is %.2f. \n %s' %(BMI, result))