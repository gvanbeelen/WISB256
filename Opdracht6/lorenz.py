from scipy.integrate import odeint
import numpy
class Lorenz:
    def __init__(self,lijst=[],sigma=10,rho=28,beta=8/3):
        self.lijst=lijst
        self.sigma=sigma
        self.rho=rho
        self.beta=beta
    
    def func(self,Y,t):
        [x,y,z]=Y
        return [self.sigma*(y-x),x*(self.rho-z)-y,x*y-self.beta*z]
        
    def solve(self,T,dt):
        time=numpy.arange(0,T+dt,dt)
        result=odeint(self.func,self.lijst,time)
        return result
        
    