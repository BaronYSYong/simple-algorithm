import matplotlib.pyplot as plt

class PlotGraph(object):
    def Plot2DGraph(self, x, y, title):
        plt.plot(x,y,'g')
        plt.plot(x[0], y[0], 'ro') # red dot: start point
        plt.plot(x[-1], y[-1], 'bo') # blue dot: end point
        plt.grid()
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(title)
        plt.show()      
