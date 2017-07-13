"""
Reference:
    https://elepa.files.wordpress.com/2013/11/fifty-famous-curves.pdf
"""

import math

class Curves(object):
    def deg2rad(self, pos):
        return pos*math.pi/180.0    
            
    def Lissajous(self, a, b, c, n):
        t = range(-180,180)
        x = []
        y = []
        for i in t:
            i = self.deg2rad(i)
            x.append(a*math.sin(n*i+c))
            y.append(b*math.sin(i))
        return x, y
           
    def Cardioid(self, a):
        t = range(-180,180)
        x = []
        y = []
        for i in t:
            i = self.deg2rad(i)
            x.append(a*(2*math.cos(i) - math.cos(2*i)))
            y.append(a*(2*math.sin(i) - math.sin(2*i)))
        return x, y
        
                  

    
    
