"""
Resource:
http://www-lar.deis.unibo.it/people/cmelchiorri/Files_Robotica/FIR_07_Traj_1.pdf
"""

import matplotlib.pyplot as plt
import decimal

def drange(x, y, jump):
    while x < y:
        yield float(x)
        x += decimal.Decimal(jump)

def ThirdOrderInterpolation(time, position, velocity):
    '''
    time[0]: initial time
    time[-1] : final time
    position[0]: initial position
    position[-1]: final position
    velocity[0]: initial velocity
    velocity[-1]: final velocity
    '''    
    a0 = position[0] # initial position
    a1 = velocity[0] # initial velocity
    a2 = (-3*(position[0]-position[-1]) - (2*velocity[0]+velocity[-1])*time[-1]) / pow(time[-1],2)
    a3 = (2*(position[0]-position[-1]) + (velocity[0]+velocity[-1])*time[-1]) / pow(time[-1],3)
    
    instant = []
    disp = []
    vel = []
    acc = []
    
    for t in list(drange(time[0], time[1], '0.1'))+[time[1]]:
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
    #~ instant1, disp1, vel1, acc1 = ThirdOrderInterpolation([0,2], [10,20], [0,-10])
    #~ instant2, disp2, vel2, acc2 = ThirdOrderInterpolation([2,4], [20,0], [-10,20])
    #~ instant3, disp3, vel3, acc3 = ThirdOrderInterpolation([4,8], [0,30], [20,3])
    #~ instant4, disp4, vel4, acc4 = ThirdOrderInterpolation([8,10], [30,40], [3,0])
    #~ instant = instant1+instant2+instant3+instant4
    #~ disp = disp1+disp2+disp3+disp4
    #~ vel = vel1+vel2+vel3+vel4
    #~ acc = acc1 + acc2 + acc3 + acc4
    #~ PlotGraph(instant, disp, vel, acc)
    instant, disp, vel, acc = ThirdOrderInterpolation([0,1], [10,30], [0,0])
    PlotGraph(instant, disp, vel, acc)    
    instant, disp, vel, acc = ThirdOrderInterpolation([0,1], [10,30], [-20,-50])
    PlotGraph(instant, disp, vel, acc)   
