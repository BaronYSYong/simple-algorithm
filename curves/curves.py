"""
Reference:
    https://elepa.files.wordpress.com/2013/11/fifty-famous-curves.pdf
"""

import math

class Curves(object):
    def deg2rad(self, pos):
        return pos*math.pi/180.0    
            
    def Lissajous(self, a, b, c, n):
        """
        The curves are constructed as a combination of two perpendicular 
        harmonic oscillations. Patterns occur as a result of differences 
        in frequency ratio (n) and phase (c).
        n = 1, c = 0 : straight line 
        n = 1, c = pi/2 : ellipse 
        n = 2, c = pi/2 : parabola
        """
        t = range(-180,180)
        a = float(a)
        b = float(b)
        c = float(c)
        n = float(n)        
        x = []
        y = []
        for i in t:
            i = self.deg2rad(i)
            x.append(a*math.sin(n*i+c))
            y.append(b*math.sin(i))
        return x, y
           
    def Cardioid(self, a):
        """
        1. Trace a point on the circle rolling around another circle of equal radius.
        2. There are exactly three parallel tangents at any given point on the cardioid.
        3. The tangents at the ends of any chord through the cusp point are at right angles.
        """
        t = range(-180,180)
        a = float(a)
        x = []
        y = []
        for i in t:
            i = self.deg2rad(i)
            x.append(a*(2*math.cos(i) - math.cos(2*i)))
            y.append(a*(2*math.sin(i) - math.sin(2*i)))
        return x, y
    
    def Epitrochoid(self, a,b,c):
        """
        The circle of radius b rolls on the outside of the circle of 
        radius a. The point P is at a distance c from the center of the 
        circle of radius b.
        """
        t = range(-180,180)
        a = float(a)
        b = float(b)
        c = float(c)
        x = []
        y = []                  
        for i in t:
            i = self.deg2rad(i)
            x.append((a+b)*math.cos(i) - c*math.cos((a/b+1.0)*i))
            y.append((a+b)*math.sin(i) - c*math.sin((a/b+1.0)*i))
        return x, y
    
    def Spiral(self, a, n):
        """
        radius = a*6
        n = number of circles
        """
        t = range(0,360*n)
        a = float(a)
        x = []
        y = []         
        for i in t:
            i = self.deg2rad(i)
            x.append(a*i*math.cos(i))    
            y.append(a*i*math.sin(i))  
        return x, y

    def Parabola(self, angle, shift_x, shift_y):
        """
        Reference: 
            https://www.youtube.com/watch?v=BPgq2AudoEo
            https://help.geogebra.org/topic/how-do-you-rotate-a-parabola-
        if f(x) = x^2
        x(t) = x cos(a) - f(x)sin(a)
        y(t) = x sin(a) + f(x)cos(a)
        """
        t = range(-10,11)
        angle = self.deg2rad(angle)
        x = []
        y = []         
        for i in t:
            x.append((i*math.cos(angle) - (i**2)*math.sin(angle)) + shift_x)    
            y.append((i*math.sin(angle) + (i**2)*math.cos(angle)) + shift_y)    
        return x, y
