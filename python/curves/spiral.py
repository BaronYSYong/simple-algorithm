from curves import Curves
from plot import PlotGraph
import math

curve = Curves()
plot = PlotGraph()

x,y = curve.Spiral(a=1, n=10)
plot.Plot2DGraph(x,y,'a=1, n=10')

x,y = curve.Spiral(a=2, n=10)
plot.Plot2DGraph(x,y,'a=2, n=10')
