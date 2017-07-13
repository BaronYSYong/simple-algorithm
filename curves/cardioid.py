from curves import Curves
from plot import PlotGraph
import math

curve = Curves()
plot = PlotGraph()
x,y = curve.Cardioid(a=-0.7)
plot.Plot2DGraph(x,y,'a=-0.7')
