# -*- coding: utf-8 -*-

#请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：

n1=input("Please input an int number: ")
n2=int(float(n1)//1)
n3=hex(n2)
print("%s的16进制为%s" %(n1,n3))


