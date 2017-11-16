import math
from decimal import Decimal,getcontext

getcontext().prec = 30

class Vector(object):

    """Constant message"""
    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'
    ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG = 'Only defined in two three dimensions vectors'
    
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            #self.coordinates = tuple(coordinates)
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(self.coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    """Iterable Feature"""
    def __iter__(self):
        self.current = -1
        return self

    def next(self):
        self.current += 1
        if self.current >= self.dimension:
            raise StopIteration
        else:
            return self.coordinates[self.current]

    def __getitem__(self, key):
        if key >= self.dimension:
            raise IndexError
        else:
            return self.coordinates[key]

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)
  
    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        """Perform plus action for two vectors"""
        new_coordinates = [x+y for x,y in zip(self.coordinates,v.coordinates)]
        return Vector(new_coordinates)

    def minus(self, v):
        """Perform minus action for two vectors"""
        new_coordinates = [x-y for x,y in zip(self.coordinates,v.coordinates)]
        return Vector(new_coordinates)

    def time_scalar(self, c):
        """Perform time scalar action for vector"""
        new_coordinates = [Decimal(c)*x for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        """
            Calculate length of unit vector:
            Keyword arguments:
                self -- vector
        """
        s=0
        for x in self.coordinates:
            s+=x*x
        return Decimal(math.sqrt(s))

    def normalized(self):
        """ Transfer vector to normal vector:
            Keyword arguments:
                self -- vector
        """
        try:
            magnitude=self.magnitude()
            return self.time_scalar(Decimal('1.0')/magnitude)

        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    def dot_product(self,v):
        """ Perform dot product for two vectors:
            Keyword arguments:
                self -- vector
                v -- 2nd vector
            Math Formula:
                v*m=v1*w1 + v2*w2 + ... + vn*wn
        """
        new_coordinates = [x*y for x,y in zip(self.coordinates,v.coordinates)]
        return sum(new_coordinates)

    def angle(self, v,output_type):
        """ Calculate the angle :
            Keyword arguments:
                self -- vector
                v -- 2nd vector
                output_type -- 'd'-degree / 'r'-rad
        """
        try:
            angle = math.acos(self.normalized().dot_product(v.normalized()))
        
            if output_type=='d':
                degrees_per_radians = 180./math.pi
                return angle*degrees_per_radians
            if output_type=='r':
                return angle
            #else:
            #    return 'Please input correct output type;'

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with the zero vector')
            else:
                raise e
 
    def is_zero(self,tolerance=1e-10):
        return self.magnitude()<tolerance        

    def check_para_orth(self,v,tolerance=1e-10):
        """ Check for Parallelism & Orthogonality:
            Keyword arguments:
                self -- vector
                v -- 2nd vector
            Output:
                Result for Parallel & Orthogonality
            
        """ 
        isorth = False 
        ispara = False

        if (self.is_zero() or v.is_zero()):
            ispara = True
            isorth = True 

        else:
            if 1-abs(self.normalized().dot_product(v.normalized()))<tolerance:
                ispara = True

            if abs(self.normalized().dot_product(v.normalized()))<tolerance:
                isorth = True

        return 'Paralell:'+str(ispara)+' ; Orthogonal:'+str(isorth)

    def is_parallel_to(self,v,tolerance=1e-10):
        ispara = False
        if (self.is_zero() or v.is_zero()):
            ispara = True
        else:
            if 1-abs(self.normalized().dot_product(v.normalized()))<tolerance:
                ispara = True
        return ispara


    def is_orth_to(self,v,tolerance=1e-10):
        isorth = False
        if (self.is_zero() or v.is_zero()):
            isorth = True
        else:
            if abs(self.normalized().dot_product(v.normalized()))<tolerance:
                isorth = True
        return isorth    

    def component_parallel_to(self,b):
        """Calculate the project vector:
            Key arguments:
                self -- vector
                b -- baseline vector
            Output:
                Project vector on baseline vector
            Formula:
                project vector = (v*ub)*ub
            
        """
        if b.is_zero()==False:
            b_n=b.normalized()
            c=self.dot_product(b_n)
            return b_n.time_scalar(c)
        return b

    def component_orthogonal_to(self,b):
        """Calculate the project vector:
            Key arguments:
                self -- vector
                b -- baseline vector
            Output:
                Orthogonal vector For baseline project
            Formula:
                vector v = v's project vector + b's orthogonal vector
                b's orthogonal vector = vector v - v's project vector
        """        
        return self.minus(self.component_parallel_to(b))

    def component_cross_product(self,v):
        """Calculate the cross product for two vectors:
            Key arguments:
                self -- vector1
                v -- vector2
            Output:
                Orthogonal vector For baseline project
        """ 
        try:
            x_1,y_1,z_1=self.coordinates
            x_2,y_2,z_2=v.coordinates
            new_coordinates=[y_1*z_2 - y_2*z_1,
                             -(x_1*z_2 - x_2*z_1),
                             x_1*y_2 - x_2*y_1]
            return Vector(new_coordinates)
        except ValueError as e:
            msg = str(e)
            if msg == 'need more than 2 values to unpack':
                self_embedded_in_R3 = Vector(self.coordinates + ('0',))
                v_embedded_in_R3 = Vector(v.coordinates + ('0',))
                return self_embedded_in_R3.cross(v_embedded_in_R3)
            elif (msg == 'too many values to unpack' or
                    msg == 'need more than 1 value to unpack'):
                raise Exception(self.ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG)
            else:
                raise e

    def component_area_of_para(self,v):
        """Calculate the area of parallelogram:
            Key arguments:
                self -- vector1
                v -- vector2
            Output:
                area of parallelogram
            Formula:
                ||v x w|| = ||v||*||w||*sin(a)
                => area of parallelogram = ||v x w||
        """ 
        return self.component_cross_product(v).magnitude()

    def component_area_of_triangle(self,v):
        """Calculate the area of triangle:
            Key arguments:
                self -- vector1
                v -- vector2
            Output:
                area of triangle
            Formula:
                area of triangle = 0.5 * ||v x w||
        """ 
        return self.component_area_of_para(v)/2
