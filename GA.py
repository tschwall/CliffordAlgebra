import numpy as np
from manim import *
import numpy as np
import math

class MultiVec():
    """
    Initialization either with np.array or with key word arguments
    
    Parameters
    ----------
    matrix : np.array(), optional
        DESCRIPTION. The default is np.array([[0,0],[0,0]]).
    **kwargs : 
        DESCRIPTION.    scalar: Scalar value --> float,
        vec: Vector value --> [e1,e2,e3]
        bivec: Bivec value --> [e12,e23,e31]
        trivec: Trivac value --> float
    Returns
    -------
    None.
    """
    def __init__(self,matrix=np.array([[0,0],[0,0]]),**kwargs):
        
        j = complex(0,1)
        
        #The four pauli matrices
        self.scalar = np.array([[1,0],
                                [0,1]])
        
        self.e1 = np.array([[0,1],
                            [1,0]])
        self.e2 = np.array([[0,- j],
                            [j,0]])
        self.e3 = np.array([[1,0],
                            [0,-1]])
        #Get value either with the keyword arguments or with matrix value
        try:
            self.value = (np.dot(kwargs["scalar"],self.scalar) 
                          + np.dot(kwargs["vec"][0],self.e1) 
                          + np.dot(kwargs["vec"][1],self.e2) 
                          + np.dot(kwargs["vec"][2],self.e3) 
                          + np.dot(kwargs["bivec"][0],np.dot(self.e1,self.e2))
                          + np.dot(kwargs["bivec"][1],np.dot(self.e2,self.e3))
                          + np.dot(kwargs["bivec"][2],np.dot(self.e3,self.e1))
                          + np.dot(kwargs["trivec"],np.dot(np.dot(self.e1,self.e2),self.e3)))
        except:
            self.value = matrix
        # print(self.scalar)
        
        # print(self.e1)
        # print(self.e2)
        # print(self.e3)
        
        # print(np.dot(self.e1,self.e2))
        # print(np.dot(self.e2,self.e3))
        # print(np.dot(self.e3,self.e1))
        
        # print(np.dot(np.dot(self.e1,self.e2),self.e3))
        
    def scalarMul(self,scalar):
        """
        Multiply the multi vector by a scalar
        
        Parameters
        ----------
        scalar : float
            Scalar to multiply the multi vector by

        Returns
        -------
        MultiVec()
            Returns a reference to the object that called

        """
        scalarMulVec = MultiVec(np.array([[scalar,0],
                                          [0,scalar]]))
        self = self * scalarMulVec
        return self
    
    def getScalar(self):
        """
        Calculate the scalar part out of the matrix

        Returns
        -------
        float
            scalar part of the multi vector

        """
        return (self.value[0][0].real + self.value[1][1].real)/2
    
    
    def getVec(self):
        """
        Calculate the vector parts out of the matrix

        Returns
        -------
        list
            [e1Part,e2Part,e3Part]
        """
        return [(self.value[0][1].real + self.value[1][0].real)/2,
                (self.value[1][0].imag - self.value[0][1].imag)/2,
                (self.value[0][0].real - self.value[1][1].real)/2]
    def getBiVec(self):
        """
        Calculate the bivector parts out of the matrix

        Returns
        -------
        list
            [e12Part,e23Part,e31Part]
        """
        return [(self.value[0][0].imag - self.value[1][1].imag)/2,
                (self.value[0][1].imag + self.value[1][0].imag)/2,
                (self.value[0][1].real - self.value[1][0].real)/2]
    
    def getTriVec(self):
        """
        Calculate the trivector part out of the matrix

        Returns
        -------
        float
            trivector part of the multi vector
        """
        return (self.value[0][0].imag + self.value[1][1].imag)/2
    
    def exp(self):
        """
        Calculate e to the power of this multi vector
        
        Returns
        -------
        MultiVector()
            e^{A}, where A is the 
        """
        matrix = np.array([[0,0],
                           [0,0]])
        for n in range(100):
            matrix = matrix + np.linalg.matrix_power(self.value,n)/math.factorial(n)
        remultiVec = MultiVec(matrix)
        return remultiVec
            
    def __mul__(self,other):
        """
        Multiply a multi vector by another multivector

        Parameters
        ----------
        other : MultiVector()
            Multi vector to multiply by

        Returns
        -------
        remultiVec : MultiVector()
            Resulting multi vector

        """
        remultiVec = MultiVec(np.dot(self.value,other.value))
        return remultiVec
    

    def __str__(self):
        retString = (f"{self.getScalar()} + {self.getVec()[0]}e1 + {self.getVec()[1]}e2 + {self.getVec()[2]}e3"
                     f"+ {self.getBiVec()[0]}e12 + {self.getBiVec()[1]}e23 + {self.getBiVec()[2]}e31 + {self.getTriVec()}e123")
        return retString
    

        

I = MultiVec(scalar=0,vec=[0,0,0],bivec=[math.pi,0,0],trivec=0)

vec = MultiVec(scalar=0,vec=[1,0,0],bivec=[0,0,0],trivec=0)
print(vec * I.exp())

