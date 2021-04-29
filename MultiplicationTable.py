from manim import *
import numpy as np
import math

class GeometricAlgebra2D(Scene):
    
    def mat(self,matrix,element):
        matrix = np.array(matrix).astype("str")

        n_rows, n_cols = matrix.shape
        prefix = "\\begin{array}{%s}" % ("c" * n_cols  )
        suffix = "\\end{array}"
        string = ""
        for row in range(n_rows):
            
            for column in range(n_cols):
                text = matrix[row][column]
                searchFor = [row,column]
                if not searchFor in element:
                    text = "\phantom{" + "text" + "}"
                    
                if not column == n_cols-1:
                    string += text + " & " 
                else:
                    string += text
            string += "  \\\\ "
       
        
        return prefix + string + suffix
    
    def construct(self):
        
      
         matrix = Matrix([[r"-"     ,r"1"   ,r"e_1" ,r"e_2" ,r"e_1e_2"],
                   [r"1"     ,r"1"   ,r"e_1" ,r"e_2" ,r"e_1e_2"],
                   [r"e_1"   ,r"e_1" ,r"1"   ,r"e_1e_2" ,r"e_2"],
                   [r"e_2"   ,r"e_2" ,r"-e_1e_2" ,r"1" ,r"-e_1"],
                   [r"e_1e_2",r"e_1e_2",r"-e_2" ,r"e_1" ,r"???"]]).scale(1.5)
         matrix_2 = Matrix([[r"-"     ,r"1"   ,r"e_1" ,r"e_2" ,r"e_1e_2"],
                   [r"1"     ,r"1"   ,r"e_1" ,r"e_2" ,r"e_1e_2"],
                   [r"e_1"   ,r"e_1" ,r"e_1^2"   ,r"e_1e_2" ,r"e_2"],
                   [r"e_2"   ,r"e_2" ,r"e_2e_1 " ,r"e_2^2" ,r"-e_1"],
                   [r"e_1e_2",r"e_1e_2",r"{{e_1}}{{e_2}}{{e_1}}" ,r"e_1" ,r"???"]]).scale(1.5)
         
      

         
         
         elements = matrix.get_entries()
         elements2 = matrix_2.get_entries()
         self.play(Write(elements[1:5]),
                   Write(elements[5]),
                   Write(elements[10]),
                   Write(elements[15]),
                   Write(elements[20]),)
         self.wait(2)
         #Mal 1
         self.play(Write(elements[6:10]),
                   Write(elements[11]),
                   Write(elements[16]),
                   Write(elements[21]))
         self.wait(2)
         #Diagonale
         self.play(Indicate(elements[2]),
                   Indicate(elements[10]))
         self.play(ReplacementTransform(elements[2].copy(),elements2[12]),
                   ReplacementTransform(elements[10].copy(),elements2[12]))
         self.play(Transform(elements2[12],elements[12]))
         
         self.play(Indicate(elements[3]),
                   Indicate(elements[15]))
         self.play(ReplacementTransform(elements[3].copy(),elements2[18]),
                   ReplacementTransform(elements[15].copy(),elements2[18]))
         self.play(Transform(elements2[18],elements[18]))
         
         self.wait(0.5)
         self.play(Indicate(elements[2]),
                   Indicate(elements[15]))
         self.play(ReplacementTransform(elements[2].copy(),elements2[17].shift(RIGHT*0.2)),
                   ReplacementTransform(elements[15].copy(),elements2[17].shift(RIGHT*0.2)))
         self.wait(0.5)
         self.play(TransformMatchingTex(elements2[17].shift(RIGHT*0.2),elements[17].shift(RIGHT*0.4)))
         
         self.play(Indicate(elements[3]),
                   Indicate(elements[10]))
         self.play(ReplacementTransform(elements[3].copy(),elements[13]),
                   ReplacementTransform(elements[10].copy(),elements[13]))

         
         
         

         self.wait(2)

    