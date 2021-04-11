# -*- coding: utf-8 -*-
"""
Motivation von Geometrischer Algebra
"""

from manim import *
import numpy as np
import math

class GeometricAlgebra2D(Scene):
    def construct(self):
        self.uEqu()
        
        
    def uEqu(self):
        u_vec = (["a"],["b"])
        e1_vec = ([1],[0])
        e2_vec = ([0],[1])
        e1_vec_mul = (["a"],[0])
        e2_vec_mul = ([0],["b"])
        u_equation = MathTex("u = a \cdot",
                       "e_1",
                       "+ b \cdot",
                       "e_2",
                       ).scale(1.5)
        u_equation_with_vec = MathTex("u = a \cdot", matrix_to_tex_string(e1_vec),"+ b \cdot", matrix_to_tex_string(e2_vec)).scale(1.5)

        self.play(Write(u_equation))
        self.wait(2)
        self.play(TransformMatchingTex(u_equation, u_equation_with_vec))
        self.wait(2)
        self.play(TransformMatchingTex( u_equation_with_vec,u_equation))
        
        numberplane = NumberPlane()
        vec_u_end = [3,2,0]
        vec_u = Arrow(ORIGIN,vec_u_end,buff=0)
        vec_u_text = MathTex('(a,b)').next_to(vec_u.get_end(),RIGHT)   
        Vec_u = VGroup(vec_u,vec_u_text)
        
        self.play(Transform(u_equation,Vec_u),Create(numberplane))
        self.wait(2)
        
        add_text = MathTex("u+v=(a+c)e_1 + (b+d)e_2").scale(1.5)
        add_text.to_corner(DOWN+LEFT)
        
        self.play(Write(add_text))
        
        vec_v = Arrow(ORIGIN,[-2,1,0],buff=0,COLOR=BLUE)
        vec_v_text = MathTex('(c,d)').next_to(vec_v.get_end(),UP)
        vec_v_trans= Arrow(vec_u_end,[vec_u_end[0] - 2, vec_u_end[1] + 1,0],buff=0,COLOR=BLUE)
        Vec_v = VGroup(vec_v,vec_v_text)
        
        self.play(Create(Vec_v))
        self.wait(0.5)
        self.play(Transform(Vec_v,vec_v_trans))
        
        vec_add = Arrow(ORIGIN,[vec_u_end[0] - 2, vec_u_end[1] + 1,0],buff=0)
        
        self.play(Create(vec_add))
        
        #Vektor Subtraktion in der Mitte
        
        mul_text = MathTex("uv=?").scale(1.5)
        mul_text.to_corner(DOWN+RIGHT)
        
        self.play(Write(mul_text))

        
        
        
        
        