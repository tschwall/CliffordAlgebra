import numpy as np
from manim import *
import numpy as np
import math

class Render(ThreeDScene):
    
    def giveVec(self,multiVec,col=GOLD_D):
        arrow1 = Arrow3D(ORIGIN,multiVec.getVec(),angle=0*DEGREES,color=col)
        return arrow1
    
    def giveBiVec(self,multiVec):
        a,b,c = multiVec.getBiVec()
        poly = Polygon(ORIGIN,[a,0,-b],[a,1,-b-c/a],[0,1,- c/a],fill_color=BLUE,fill_opacity=0.8)
        return poly
        
    
    def plotMultiVec(self,multiVec):
        plotVec(multiVec)
        plotBiVec(multiVec)
        
    def transformVec(self,rotVec,rotBiVec,steps,degree):
        vec = MultiVec(rotVec.value)
        vGroup = VGroup()
        for step in range(steps-1):
            R = (rotBiVec.scalarMul(degree/steps)).exp()
            R_inv = (rotBiVec.scalarMul(-1*degree/steps)).exp()
            vec = R*vec*R_inv
            plot_vec = self.giveVec(vec)
            vGroup.add(plot_vec)
        return vGroup
    
    def drawRotation(self,rotVec,rotBiVec,steps,degree):
        vec = MultiVec(rotVec.value)
        points = [rotVec.getVec()]
        for step in range(steps):
            R = (rotBiVec.scalarMul(degree/steps)).exp()
            R_inv = (rotBiVec.scalarMul(-1*degree/steps)).exp()
            vec = R*vec*R_inv
            points.append(vec.getVec())
        return points
    

        
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        self.play(Create(axes))
        
        vec1 = MultiVec(scalar=0,vec=[2,0,0],bivec=[0,0,0],trivec=0)
        bivec2 = MultiVec(scalar=0,vec=[0,0,0],bivec=[1/math.sqrt(2),1/math.sqrt(2),0],trivec=0)
        
        points = self.drawRotation(vec1,bivec2,15,math.pi/2)
        print(len(points))
        rotateVec = self.giveVec(vec1)
        self.add(self.giveBiVec(bivec2))
        self.add(rotateVec)
        
        #self.play(Rotate(rotateVec,axis=np.array(np.cross([1/math.sqrt(2),0,-1/math.sqrt(2)],[0,1,0]))))
        
        for n,point in enumerate(points):
            if n>= len(points)-1: break
            line = Line3D(point, points[n+1])
            self.add(line)
            self.wait(0.2)
            
        
        # self.add(self.giveBiVec(bivec2))
        # self.add(self.giveVec(vec1))
        
        # self.begin_ambient_camera_rotation(rate=0.2)
        
        # group = self.transformVec(vec1,bivec2,4,math.pi/2)
        # for element in group:
        #     self.wait(1)
        #     self.add(element)
            
        # self.wait(5)
        # self.stop_ambient_camera_rotation()
        
        self.wait(2)