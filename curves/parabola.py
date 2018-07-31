from curves import Curves
from plot import PlotGraph
import math

curve = Curves()
plot = PlotGraph()

x,y = curve.Parabola(angle=0, shift_x=0, shift_y=0) 
plot.Plot2DGraph(x,y,'angle=0, shift_x=0, shift_y=0')

x,y = curve.Parabola(angle=45, shift_x=0, shift_y=0) 
plot.Plot2DGraph(x,y,'angle=45, shift_x=0, shift_y=0')

x,y = curve.Parabola(angle=90, shift_x=0, shift_y=0) 
plot.Plot2DGraph(x,y,'angle=90, shift_x=0, shift_y=0')


