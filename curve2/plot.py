import matplotlib.pyplot as plt

class PlotGraph(object):
    def Plot2DGraph(self, x, y, vertex, title):
        mp = ((x[0]+x[-1])/2, (y[0]+y[-1])/2) # midpoint
        plt.plot(x,y,'g')
        plt.plot(x[0], y[0], 'ro') # red dot: start point
        plt.plot(x[-1], y[-1], 'bo') # blue dot: end point
        plt.plot([vertex[0], mp[0]], [vertex[1], mp[1]], 'ko')
        plt.plot([vertex[0], mp[0]], [vertex[1], mp[1]], 'b--')
        plt.plot([x[0],x[-1]], [y[0], y[-1]], 'r--')
        plt.grid()        
        plt.axis([80, 220, 80, 220])
        plt.xlabel('x', fontsize=20)
        plt.ylabel('y', fontsize=20)
        plt.title(title, fontsize=15)
        plt.show()      
