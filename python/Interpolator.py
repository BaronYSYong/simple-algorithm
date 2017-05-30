import matplotlib.pyplot as plt

def ThirdOrderInterpolation(time, position, velocity):
    '''
    time[0]: initial time
    time[1] : final time
    position[0]: initial position
    position[1]: final position
    velocity[0]: initial velocity
    velocity[1]: final velocity
    '''    
    a0 = position[0] # initial position
    a1 = velocity[0] # initial velocity
    a2 = (-3*(position[0]-position[1]) - (2*velocity[0]+velocity[1])*time[1]) / pow(time[1],2)
    a3 = (2*(position[0]-position[1]) + (velocity[0]+velocity[1])*time[1]) / pow(time[1],3)
    
    instant = []
    disp = []
    vel = []
    acc = []
    
    for t in range(time[1]*10+1):
        t = t*0.1
        instant.append(t)
        disp.append(a0 + a1*t + a2*pow(t,2) + a3*pow(t,3))
        vel.append(a1 + 2*a2*t + 3*a3*pow(t,2))
        acc.append(2*a2 + 6*a3*t)
    return instant, disp, vel, acc

def PlotGraph(instant, disp, vel, acc):        
    plt.subplot(311)
    plt.plot(instant,disp)
    plt.title('displacement')
    plt.grid()    
    plt.subplot(312)
    plt.plot(instant,vel)
    plt.title('velocity')  
    plt.grid()      
    plt.subplot(313)
    plt.plot(instant,acc)
    plt.title('acceleration')
    plt.grid()
    plt.show()
        
if __name__ == '__main__':
    instant, disp, vel, acc = ThirdOrderInterpolation([0,1], [10,30], [0,0])
    PlotGraph(instant, disp, vel, acc)
    instant, disp, vel, acc = ThirdOrderInterpolation([0,1], [10,30], [-20,-50])
    PlotGraph(instant, disp, vel, acc)
