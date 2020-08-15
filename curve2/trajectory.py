import math
import decimal

class Trajectory(object):
    def drange(x, y, jump):
        while x < y:
            yield float(x)
            x += decimal.Decimal(jump)

    def deg2rad(self, pos):
        return pos*math.pi/180.0   
        
    def PerpendicularPoint(self, (x1,y1), (x2,y2), r):
        dx = x1-x2 
        dy = y1-y2
        midpoint_x = (x1+x2)/2.0
        midpoint_y = (y1+y2)/2.0
        distance = math.sqrt(dy**2+dx**2)     
        x3 = midpoint_x + r/distance*dy
        y3 = midpoint_y - r/distance*dx
        x4 = midpoint_x - r/distance*dy
        y4 = midpoint_y + r/distance*dx
        return (x3,y3), (x4,y4), distance

    def PerpendicularDistance(self, (x1,y1), (x2,y2), (x3,y3)):
        m = float(y2-y1)/float(x2-x1)
        c = float(y1 - m*x1)
        d = abs(m*x3 - y3 + c)/math.sqrt(m**2+1)
        return d
        
    def Parabola(self, r, d, t_range, angle, shift_x, shift_y):
        """
        Reference: 
            https://www.youtube.com/watch?v=BPgq2AudoEo
            https://help.geogebra.org/topic/how-do-you-rotate-a-parabola-
        if f(x) = ax**2
        x(t) = x cos(a) - f(x)sin(a)
        y(t) = x sin(a) + f(x)cos(a)
        """
        t = range(t_range[0], t_range[1]+1)
        x = []
        y = []   
        print "radius = ", r    
        print "distance ", d
        print "t_range ", t_range 
        print "angle ", angle*180.0/math.pi 
        print "vertex ", (shift_x, shift_y)
        for i in t:
            fx = (r/(d/2.0)**2)*i**2
            x.append((i*math.cos(angle) - fx*math.sin(angle)) + shift_x)    
            y.append((i*math.sin(angle) + fx*math.cos(angle)) + shift_y)    
        return x, y

    def CurveTrajectory(self, p1, p2, radius, direction):
        """
        p1 = (x1, y1)
        p2 = (x2, y2)
        radius in mm
        direction: 
            -1: clockwise 
            1: for counter-clockwise
        """
        p3, p4, distance = self.PerpendicularPoint(p1, p2, radius)
        angle = math.atan2(p2[1]-p1[1], p2[0]-p1[0])
        td = round(direction*math.cos(angle), 8) # turning direction, the value will be round to 8 decimal points
        if td == 0.0:
            if (direction*math.sin(angle)) > 0.0:
                if p3[0] > p4[0]:
                    vertex = (p3[0], p3[1])
                else:
                    vertex = (p4[0], p4[1])
            else:
                if p3[0] > p4[0]:
                    vertex = (p4[0], p4[1])
                else:
                    vertex = (p3[0], p3[1])                 
        elif td < 0.0: # if td is negative           
            if p3[1] > p4[1]:
                vertex = (p3[0], p3[1])
            else:
                vertex = (p4[0], p4[1])
        else: # if td is positive
            if p3[1] > p4[1]:
                vertex = (p4[0], p4[1])
            else:
                vertex = (p3[0], p3[1])            
        t_range = [int(round(0.0-(distance/2.0))), int(round(0.0+(distance/2.0)))]                
        x,y = self.Parabola(direction*radius, distance, t_range, angle, vertex[0], vertex[1])
        return x, y, angle, vertex
         
