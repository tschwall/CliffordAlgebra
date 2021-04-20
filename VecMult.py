# -*- coding: utf-8 -*-
"""
Manim video of VectorMultiplication
"""

from manim import *
import numpy as np
import math

class VecMult(Scene):
    def construct(self):
        title = [
            Tex("Vektormultiplikation: ","u","v"),
            Tex("Vektormultiplikation: ","u","v").to_corner(UP + LEFT)
            ]
        uEq = MathTex(*"u = a e_1 + b e_2".split()).shift(UP).shift(UP)
        vEq = MathTex(*"v = c e_1 + d e_2".split()).shift(UP)
        uvEq = [
            MathTex(*"u v = ( a e_1 + b e_2 )( c e_1 + d e_2 )".split()),
            MathTex(*"u v = a c e_1 e_1 + b d e_2 e_2 + a d e_1 e_2 + b c e_2 e_1".split()).shift(DOWN),
            MathTex(*"u v = a c \cdot 1 + b d \cdot 1 + a d e_1 e_2 - b c e_1 e_2".split()).shift(DOWN),
            MathTex(*"u v = ( a c + b d ) + ( a d - c d ) e_1 e_2".split()).shift(DOWN),
            MathTex(*"u v = ( a c + b d ) + ( a d - c d ) e_1 e_2".split()).to_corner(UP + LEFT).shift(0.5*DOWN + LEFT*0.5).scale(0.75),
            MathTex(*r"u v = ( |u| |v| cos( \varphi )) + ( |u| |v| sin( \varphi ) ) e_1 e_2".split()).to_corner(UP + LEFT).shift(2*DOWN + LEFT).scale(0.75)
            ]
        self.play(Write(title[0]))
        self.wait(1)
        self.play(Transform(title[0], title[1]))
        self.wait(1)
        self.play(Write(uEq), Write(vEq))
        self.wait(1)
        self.play(ReplacementTransform(uEq[0].copy(), uvEq[0][0]), ReplacementTransform(vEq[0].copy(), uvEq[0][1]))
        self.play(
            Write(uvEq[0][2:4]),
            ReplacementTransform(uEq[2:].copy(), uvEq[0][4:9]),
            Write(uvEq[0][9]),
            ReplacementTransform(vEq[2:].copy(), uvEq[0][10:15]),
            Write(uvEq[0][15])
            )
        self.wait(2)
        self.play(Write(uvEq[1][:3]), Write(uvEq[1][7::5]))
        
        
        
        
        self.remove(uvEq[1])
        self.play(
            ReplacementTransform(uvEq[0][4:6].copy(), uvEq[1][3:7]),
            ReplacementTransform(uvEq[0][10:12].copy(), uvEq[1][3:7])
            )
        self.play(
            ReplacementTransform(uvEq[0][7:9].copy(), uvEq[1][8:12]),
            ReplacementTransform(uvEq[0][13:15].copy(), uvEq[1][8:12])
            )
        self.play(
            ReplacementTransform(uvEq[0][4:6].copy(), uvEq[1][13:17]),
            ReplacementTransform(uvEq[0][13:15].copy(), uvEq[1][13:17])
            )
        self.play(
            ReplacementTransform(uvEq[0][7:9].copy(), uvEq[1][18:]),
            ReplacementTransform(uvEq[0][10:12].copy(), uvEq[1][18:])
            )
        self.wait(2)
        self.play(
            TransformMatchingTex(uvEq[1], uvEq[2])
            )
        self.wait(2)
        self.play(
            TransformMatchingTex(uvEq[2], uvEq[3])
            )
        self.wait(2)
        brace1 = Brace(uvEq[3][3:10])
        brace2 = Brace(uvEq[3][11:18])
        print("GG")
        brace1_text = brace1.get_text("Dot-Product").shift(LEFT*0.5)
        brace2_text = brace2.get_text("Parallelogramm").shift(RIGHT*0.5)
        braces = VGroup(brace1,brace2,brace1_text,brace2_text)
        self.play(Write(braces))
          
        #Transfer to numberplane
        self.play(
            FadeOut(braces),
            FadeOut(uEq),
            FadeOut(vEq),
            FadeOut(uvEq[0])
            )
        self.play(
            Transform(uvEq[3], uvEq[4])
            )
        
        vGroup = VGroup(uvEq[4],title[1])
        self.add_foreground_mobjects(vGroup)
        frame = SurroundingRectangle(vGroup,fill_color=BLACK,fill_opacity=1,color=WHITE,buff = .1)
        numberplane = NumberPlane()
        self.play(Write(frame))
        self.add_foreground_mobjects(frame)
        self.add_foreground_mobjects(vGroup)
        self.play(Write(numberplane))
        
        u_vec_val = np.array([4/3,2,0])
        v_vec_val = np.array([2.25,0.75,0])
        u_vec = Arrow(ORIGIN,u_vec_val,buff=0)
        u_vec_text = Tex('({{a}}, {{b}})').next_to(u_vec.get_end(), LEFT*0.9).scale(0.75)
        v_vec = Arrow(ORIGIN,v_vec_val,buff=0)
        v_vec_text = Tex('({{c}}, {{d}})').next_to(v_vec.get_end(), DOWN).scale(0.75)
        self.play(Create(v_vec),Create(u_vec_text),Create(u_vec),Create(v_vec_text))
        self.wait(1)
        #DOTPRODUCT
        
        ortho = np.dot(u_vec_val,v_vec_val)/np.dot(v_vec_val,v_vec_val)
       
        line = DashedLine(v_vec_val * ortho
                          ,u_vec_val)
        orto_vec = Arrow(ORIGIN,
                         v_vec_val* ortho,buff=0)
        dotProd =  Arrow(ORIGIN,
                         v_vec_val*math.sqrt(np.dot(u_vec_val,v_vec_val)),
                         buff=0)
        b1 = Brace(dotProd,direction=(dotProd.copy().rotate(-math.pi/2).get_unit_vector()),buff=0)
        b1_text = b1.get_tex("|...| = ac + bd").shift(0.5*DOWN)
        b2_text = b1.get_tex(r"ac + bd = |u||v|cos( \varphi )").shift(0.5*DOWN)
        angleBetween = Angle(v_vec, u_vec, radius=0.8, other_angle=False)
        angleTex = MathTex(r"\varphi").move_to(angleBetween).shift(0.2*UP+0.2*RIGHT)
        dotProd_G = VGroup(line,dotProd,b1,b1_text,angleBetween,angleTex,b2_text)
        frame2 = SurroundingRectangle(uvEq[5],fill_color=BLACK,fill_opacity=1,color=WHITE,buff = .1)
        self.play(Create(line))
        self.play(Create(orto_vec))
        self.play(ReplacementTransform(orto_vec,dotProd))
        self.play(Create(b1),
                  Create(b1_text))
        self.play(Create(angleBetween),
                  Create(angleTex))
        self.play(Unwrite(b1_text))
        self.play(Write(b2_text))
        self.play(Write(frame2),
                  Write(uvEq[5][0:3]))
        self.play(ReplacementTransform(b2_text.copy(),uvEq[5][3:9]))
        self.play(Unwrite(dotProd_G))
        
        #PARALLELOGRAM
        parallel = Polygon(ORIGIN,u_vec_val,u_vec_val + v_vec_val,v_vec_val,color=WHITE,fill_color=WHITE,fill_opacity=0.5)
        flaecheText = Tex(r" Fläche = ad-cb").next_to(v_vec).shift(DOWN+4*LEFT)
        flaecheText2 = Tex(r" {{Fläche}} = |u||v| sin($\varphi$)").next_to(v_vec).shift(DOWN+4*LEFT)
        self.play(Write(parallel))
        self.play(Write(flaecheText))
        self.play(TransformMatchingTex(flaecheText,flaecheText2))
        self.play(ReplacementTransform(flaecheText2.copy(),uvEq[5][9:17]))
        self.play(ReplacementTransform(uvEq[4][19:].copy(),uvEq[5][17:]))
        self.wait(2)
        
