from manim import *
import numpy as np
import math

class GeometricAlgebra2D(Scene):
    def construct(self):
        title = [
            Tex("Vektormultiplikation"),
            Tex("Vektormultiplikation").to_corner(UP + LEFT)
            ]
        
        self.play(Write(title[0]))
        self.wait(1)
        self.play(Transform(title[0], title[1]))
        self.wait(1)
        
        text1 =MathTex("u^2 ",      #0
                       "=",         #1
                       "(",         #2
                       "ae_1",      #3
                       " + ",       #4
                       "be_2",      #5
                       ")(",        #6
                       "ae_1",      #7
                       " + ",       #8
                       "be_2",      #9
                       ")",         #10
                       ).shift(UP)
        text2 =MathTex(" = ",       #0
                       "a^2",       #1
                       "e_1e_1",    #2
                       " + ",       #3
                       "b^2",       #4
                       "e_2e_2",    #5
                       " + ",       #6
                       "abe_1e_2",  #7
                       " + ",       #8
                       "bae_2e_1"   #9
                       )
        
        text3 =MathTex(" = ",       #0
                       "a^2",       #1         
                       " + ",       #2
                       "b^2",       #3         
                       " + ",       #4
                       "abe_1e_2",  #5
                       " + ",       #6
                       "bae_2e_1"   #7
                       ).shift(DOWN)
          
        addText = Tex("Ziel: Quadrat ergibt die Länge des Vektors").shift(2*UP)
        self.play(Write(addText))
        self.wait(0.5)
        self.play(Write(text1[0]))
        self.wait(0.5)
        self.play(Write(text1[1:]))
        self.wait(0.5)
        #Ausrechnen text2_1
        self.play(Write(text2[0]))
        self.wait(0.5)
        
        self.play(ReplacementTransform(text1[3].copy(),text2[1:3]),ReplacementTransform(text1[7].copy(),text2[1:3]))
        self.play(Write(text2[3]))
        self.wait(0.5)
        self.play(ReplacementTransform(text1[5].copy(),text2[4:6]),ReplacementTransform(text1[9].copy(),text2[4:6]))
        self.play(Write(text2[6]))
        self.wait(0.5)
        self.play(ReplacementTransform(text1[3].copy(),text2[7]),ReplacementTransform(text1[9].copy(),text2[7]))
        self.play(Write(text2[8]))                                       
        self.wait(0.5)
        self.play(ReplacementTransform(text1[5].copy(),text2[9]),ReplacementTransform(text1[7].copy(),text2[9]))
        self.wait(2)
        self.play(Write(text3[0]))
        self.play(ReplacementTransform(text2[1:3].copy(),text3[1]))
        self.play(Write(text3[2]))
        self.play(ReplacementTransform(text2[4:6].copy(),text3[3]))
        self.play(Write(text3[4]))
        self.play(ReplacementTransform(text2[7].copy(),text3[5]),Write(text3[6]),ReplacementTransform(text2[9].copy(),text3[7]))
        
        b1 = Brace(text3[1:4])
        b1_text = b1.get_text("Länge Vektor")
        B1 = VGroup(b1,b1_text)
        self.play(Write(B1))
        self.wait(2)
        b2 = Brace(text3[5:8])
        b2_text = b2.get_text("0")
        B2 = VGroup(b2,b2_text)
        self.play(Write(B2))
        self.play(Unwrite(text3[0:5]),Unwrite(text2),Unwrite(text1),Unwrite(B1),Unwrite(addText))
        self.wait(0.5)
  
        equationStage1 = MathTex("abe_1e_2",    #0
                                 " + ",         #1
                                 "ba",          #2
                                 "e_2e_1",      #3
                                 " = ",         #4
                                 "0")           #5
        
        equationStage2 = MathTex("abe_1e_2",    #0
                                 " + ",         #1
                                 "ab",          #2
                                 "e_2e_1",      #3
                                 " = ",         #4
                                 "0")           #5
        
        equationStage3 = MathTex("abe_1e_2",    #0
                                 " = ",         #1
                                 "-",           #2
                                 "ab",          #3
                                 "e_2e_1")      #4
        
        equationStage4 = MathTex("e_1e_2",      #0
                                 " = ",         #1
                                 "-",           #2
                                 "e_2e_1")      #4
        antikommText = Tex("Das Produkt ist somit antikommutativ \\\\",
                           "für orthogonale Vektoren").shift(DOWN)
        
        self.play(ReplacementTransform(text3[5:],equationStage1[0:4]),
                  ReplacementTransform(B2,equationStage1[4:]))
        self.wait(0.5)
        #Wir gehen davon aus, wir erwarten von unserer Algebra,
        # das Skalare umgestellt werden können
        self.play(TransformMatchingTex(equationStage1,equationStage2))
        self.wait(0.5)
        #Der rechte Term auf die rechte Seite nehmen
        self.play(TransformMatchingTex(equationStage2,equationStage3))
        #Und durch ab dividieren
        self.play(TransformMatchingTex(equationStage3,equationStage4))
        self.play(Write(antikommText))
        #Somit zeigt sich das unser Produkt antikommutativ ist
        #Berechnen wir nun das Produkt von zwei beliebigen Vektoren mit den 
        #soeben betrachteten Regeln
        #u_1 = ae_1 + be_2  u_2 = ce_2 + de_2
        #u_1u_2 = (ae_1 + be_2)(ce_1 + de_2) = ace_1e_1
        
        
        

