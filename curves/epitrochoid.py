from curves import Curves
from plot import PlotGraph
import math

curve = Curves()
plot = PlotGraph()

x,y = curve.Epitrochoid(a=10,b=2,c=5) 
plot.Plot2DGraph(x,y,'a=10,b=2,c=5')

