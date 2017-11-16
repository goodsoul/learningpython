#import test.vector as vector
import vector
import math

v1 = vector.Vector(['7.887','4.138'])
w1 = vector.Vector(['-8.802','6.776'])

v2 = vector.Vector(['-5.955','-4.904','-1.874'])
w2 = vector.Vector(['-4.496','-8.755','7.103'])

v3 = vector.Vector(['3.183','-7.627'])
w3 = vector.Vector(['-2.668','5.319'])

v4 = vector.Vector(['7.35','0.221','5.188'])
w4 = vector.Vector(['2.751','8.259','3.985'])

#--------------------------------------

v5 = vector.Vector([-7.579,-7.88])
w5 = vector.Vector([22.737,23.64])

v6 = vector.Vector([-2.029,9.97,4.172])
w6 = vector.Vector([-9.231,-6.639,-7.245])

v7 = vector.Vector([-2.328,-7.284,-1.214])
w7 = vector.Vector([-1.821,1.072,-2.94])

v8 = vector.Vector([2.118,4.827])
w8 = vector.Vector([0,0])

#--------------------------------------
v9 = vector.Vector([3.039,1.879])
b9 = vector.Vector([0.825,2.036])

v10 = vector.Vector([-9.88,-3.264,-8.159])
b10 = vector.Vector([-2.155,-9.353,-9.473])

v11 = vector.Vector([3.009,-6.172,3.692,-2.51])
b11 = vector.Vector([6.404,-9.144,2.759,8.718])

#--------------------------------------

v12 = vector.Vector([8.462,7.893,-8.187])
w12 = vector.Vector([6.984,-5.975,4.778])

v13 = vector.Vector([-8.987,-9.838,5.031])
w13 = vector.Vector([-4.268,-1.861,-8.866])

v14 = vector.Vector([1.5,9.547,3.691])
w14 = vector.Vector([-6.007,0.124,5.772])

#print v1.magnitude()
#print v2.magnitude()
print v3.normalized()
#print v4.normalized()

'''
print v1.dot_product(w1)
print v2.dot_product(w2)
print v3.angle(w3,'r')
print v4.angle(w4,'d')
'''

'''
#Check Paralell or Orthonogal
print v5.check_para_orth(w5)
print v6.check_para_orth(w6)
print v7.check_para_orth(w7)
print v8.check_para_orth(w8)

print v9.component_parallel_to(b9)
print v10.component_orthogonal_to(b10)

print v11.component_parallel_to(b11)
print v11.component_orthogonal_to(b11)
'''

print v12.component_cross_product(w12)
print v13.component_area_of_para(w13)
print v14.component_area_of_triangle(w14)

#print v2==v3
#print v1==v3
#print v4
#print v5
#print v6
