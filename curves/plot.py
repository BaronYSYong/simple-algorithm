import matplotlib.pyplot as plt

class PlotGraph(object):
    def Plot2DGraph(self, x, y, title):
        plt.plot(x,y,'g')
        plt.grid()
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(title)
        plt.show()      
