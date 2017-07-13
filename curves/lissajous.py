from curves import Curves
import math

curve = Curves()

x,y = curve.Lissajous(a=3,b=3,c=0,n=1) # n=1, c=0: straight line
curve.Plot2DGraph(x,y,'a=3,b=3,c=0,n=1')

x,y = curve.Lissajous(a=3,b=3,c=math.pi/2,n=1) # n=1, c=pi/2: ellipse
curve.Plot2DGraph(x,y,'a=3,b=3,c=math.pi/2,n=1')

x,y = curve.Lissajous(a=3,b=3,c=math.pi/2,n=2) # n=2, c=pi/2: parabola
curve.Plot2DGraph(x,y,'a=3,b=3,c=math.pi/2,n=2')

x,y = curve.Lissajous(a=3,b=2,c=3,n=3) # b affect the boundary of y, e.g. b = 2, y = range(-2,2)
curve.Plot2DGraph(x,y,'a=3,b=2,c=3,n=3')

x,y = curve.Lissajous(a=3,b=3,c=5,n=3) # c affect number of ellipse
curve.Plot2DGraph(x,y,'a=3,b=3,c=5,n=3')


