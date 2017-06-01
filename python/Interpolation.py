"""
Resource:
http://www-lar.deis.unibo.it/people/cmelchiorri/Files_Robotica/FIR_07_Traj_1.pdf
"""

import decimal

def drange(x, y, jump):
    while x < y:
        yield float(x)
        x += decimal.Decimal(jump)

def ThirdOrderPolynomial(time, position, velocity):
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
    a2 = (-3.0*(position[0]-position[-1]) - (2.0*velocity[0]+velocity[-1])*time[-1]) / pow(time[-1],2)
    a3 = (2.0*(position[0]-position[-1]) + (velocity[0]+velocity[-1])*time[-1]) / pow(time[-1],3)
    
    instant = []
    disp = []
    vel = []
    acc = []
    
    for t in list(drange(time[0], time[-1], '0.1'))+[time[-1]]:
        instant.append(t)
        disp.append(a0 + a1*t + a2*pow(t,2) + a3*pow(t,3))
        vel.append(a1 + 2.0*a2*t + 3.0*a3*pow(t,2))
        acc.append(2.0*a2 + 6.0*a3*t)
    return instant, disp, vel, acc

def ThirdOrderPolynomialMultiPoints(time, position, velocity):
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
    a2 = (-3.0*(position[0]-position[-1]) - (2*velocity[0]+velocity[-1])*(time[-1]-time[0])) / pow(time[-1]-time[0],2)
    a3 = (2.0*(position[0]-position[-1]) + (velocity[0]+velocity[-1])*(time[-1]-time[0])) / pow(time[-1]-time[0],3)
    
    instant = []
    disp = []
    vel = []
    acc = []
    
    for p in range(len(time)-1):
        print time[p], time[p+1]
        for t in list(drange(time[p], time[p+1], '0.1')):
            instant.append(t)
            disp.append(a0 + a1*(t-time[0]) + a2*pow(t-time[0],2) + a3*pow(t-time[0],3))
            vel.append(a1 + 2.0*a2*(t-time[0]) + 3.0*a3*pow(t-time[0],2))
            acc.append(2.0*a2 + 6.0*a3*(t-time[0]))
    return instant, disp, vel, acc

def FifthOrderPolynomial(time, position, velocity, acceleration):
    T = time[-1] - time[0]
    a0 = position[0] # initial position
    a1 = velocity[0] # initial velocity
    a2 = 0.5*acceleration[0]
    a3 = (1.0/(2.0*pow(T,3)))*(20.0*(position[-1]-position[0]) - (8.0*velocity[-1]+12.0*velocity[0])*T - (3.0*acceleration[-1]-acceleration[0])*pow(T,2))
    a4 = (1.0/(2.0*pow(T,4)))*(30.0*(position[0]-position[-1]) + (14.0*velocity[-1]+16.0*velocity[0])*T + (3.0*acceleration[-1]-2.0*acceleration[0])*pow(T,2))
    a5 = (1.0/(2.0*pow(T,5)))*(12.0*(position[-1]-position[0]) - 6.0*(velocity[-1]+velocity[0])*T - (acceleration[-1]-acceleration[0])*pow(T,2))
       
    instant = []
    disp = []
    vel = []
    acc = []
    
    for t in list(drange(time[0], time[-1], '0.1'))+[time[-1]]:
        instant.append(t)
        disp.append(a0 + a1*t + a2*pow(t,2) + a3*pow(t,3) + a4*pow(t,4) + a5*pow(t,5))
        vel.append(a1 + 2.0*a2*t + 3.0*a3*pow(t,2) + 4.0*a4*pow(t,3) + 5*a5*pow(t,4))
        acc.append(2.0*a2 + 6.0*a3*t + 12.0*a4*pow(t,2) + 20.0*a5*pow(t,3))
    return instant, disp, vel, acc        
