from trajectory import Trajectory
from plot import PlotGraph
import math

curve = Trajectory()
plot = PlotGraph()

p1 = (150.0, 200.0)
p2 = (200.0, 100.0)
radius = 30.0
x,y,angle,vertex = curve.CurveTrajectory(p1, p2, radius, -1)
title = 'angle = ' + str(angle*180.0/math.pi) + ', direction = clockwise'
plot.Plot2DGraph(x,y,vertex,title)

x,y,angle,vertex = curve.CurveTrajectory(p1, p2, radius, 1)
title = 'angle = ' + str(angle*180.0/math.pi) + ', direction = counterclockwise'
plot.Plot2DGraph(x,y,vertex,title)

x,y,angle,vertex = curve.CurveTrajectory(p2, p1, radius, -1)
title = 'angle = ' + str(angle*180.0/math.pi) + ', direction = clockwise'
plot.Plot2DGraph(x,y,vertex,title)

x,y,angle,vertex = curve.CurveTrajectory(p2, p1, radius, 1)
title = 'angle = ' + str(angle*180.0/math.pi) + ', direction = counterclockwise'
plot.Plot2DGraph(x,y,vertex,title)
