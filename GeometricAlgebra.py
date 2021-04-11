from manim import *
import numpy as np
import math

sizeofGrid = 10

def mulVec(vec1,vec2):
    if(len(vec1) == len(vec2)):
        retVec = []
        for n,vec in enumerate(vec1):
            retVec.append(vec1[n]*vec2[n]) 
    else:
        raise Exception(f'The Vectors have wrong size Vec1: {len(vec1)} und Vec2: {len(vec2)}')
    return retVec

def addVec(vec1,vec2):
    if(len(vec1) == len(vec2)):
        retVec = []
        for n,vec in enumerate(vec1):
            retVec.append(vec1[n]+vec2[n]) 
    else:
        raise Exception(f'The Vectors have wrong size Vec1: {len(vec1)} und Vec2: {len(vec2)}')
    return retVec

def subVec(vec1,vec2):
    if(len(vec1) == len(vec2)):
        retVec = []
        for n,vec in enumerate(vec1):
            retVec.append(vec1[n]-vec2[n]) 
    else:
        raise Exception(f'The Vectors have wrong size Vec1: {len(vec1)} und Vec2: {len(vec2)}')
    return retVec

def scalarMulVec(vec,n):
    retVec = []
    for elements in vec:
        retVec.append(float(elements)*n)
    return retVec
    
def absVec(vec1):
    ret = 0
    for n,vec in enumerate(vec1):
            ret += vec1[n]**2
    return math.sqrt(ret)

class GeometricAlgebra2D(Scene):
    def construct(self):
        self.sizeConst = 7/sizeofGrid
        self.play_NumberPlane()
        self.create_bivector_parallel([1,0,0],[2,1,0],[2,0,0],[-2,0,0],"GREEN")
        self.create_bivector_parallel([1,2,0],[2,3,0],[2,1,0],[-2,3,0],"GREEN")
    
    def play_NumberPlane(self):
        numberplane = NumberPlane(x_line_frequency=self.sizeConst,y_line_frequency=self.sizeConst)
        self.play(Create(numberplane))
    
    def create_bivector_parallel(self,vector1_start, vector1_end, vector2_start, vector2_end, color="GREEN"):
        """VEC1^VEC2"""
        vector1_start = scalarMulVec(vector1_start, self.sizeConst)
        vector2_start = scalarMulVec(vector2_start, self.sizeConst)
        vector1_end = scalarMulVec(vector1_end, self.sizeConst)
        vector2_end = scalarMulVec(vector2_end, self.sizeConst)
        vec1 = subVec(vector1_end,vector1_start)
        vec2 = subVec(vector2_end,vector2_start)
        parallel = Polygon(vector1_start,vector1_end,addVec(vector1_end,vec2),subVec(addVec(vector1_end,vec2),vec1),fill_color=BLUE,fill_opacity=0.5)
        print(absVec(subVec(vector2_start,vector2_end)))
        print(absVec(subVec(vector1_start,vector1_end)))
        arrow1 = Arrow(vector1_start,vector1_end,buff=0,color=BLUE)
        arrow2 = Arrow(vector2_start,vector2_end,buff=0,color=BLUE)
        arrow2_trans = Arrow(vector1_end,addVec(vector1_end,vec2),buff=0,color = BLUE)
        
        self.play(Create(arrow1))
        self.play(Create(arrow2))
        self.play(Transform(arrow2,arrow2_trans))
        self.play(Create(parallel))
        self.wait(2) 
    def plot_bivector_parallel(self,vector1_start, vector1_end, vector2_start, vector2_end, color="GREEN"):
        """VEC1^VEC2"""
        vector1_start = scalarMulVec(vector1_start, self.sizeConst)
        vector2_start = scalarMulVec(vector2_start, self.sizeConst)
        vector1_end = scalarMulVec(vector1_end, self.sizeConst)
        vector2_end = scalarMulVec(vector2_end, self.sizeConst)
        vec1 = subVec(vector1_end,vector1_start)
        vec2 = subVec(vector2_end,vector2_start)
        parallel = Polygon(vector1_start,vector1_end,addVec(vector1_end,vec2),subVec(addVec(vector1_end,vec2),vec1),fill_color=BLUE,fill_opacity=0.5)
        print(absVec(subVec(vector2_start,vector2_end)))
        print(absVec(subVec(vector1_start,vector1_end)))
        arrow1 = Arrow(vector1_start,vector1_end,buff=0,color=BLUE)
        arrow2 = Arrow(vector1_end,addVec(vector1_end,vec2),buff=0,color = BLUE)
        
        self.add(arrow1,arrow2,parallel)
        self.wait(2)
        
        