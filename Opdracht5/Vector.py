from array import array
import math
class Vector:
    def __init__(self,n=0,lijst=[]):
        self.n = n
        if lijst==[]:
            self.lijst = [0] * n
        elif isinstance(lijst, list):
            self.lijst = lijst
        else:
            self.lijst = [lijst] * n

    def __str__(self):
        result=''
        for i in range(self.n):
            result = result + str(self.lijst[i]) +'\n'
        return result
    
    def lincomb(self,other,alpha,beta):
        result=[]
        for i in range(self.n):
            result.append(alpha * self.lijst[i] + beta * other.lijst[i])
        return Vector(self.n,result)

    def scalar(self,alpha):
        result=[]
        for i in range(self.n):
            result.append(alpha * self.lijst[i])
        return Vector(self.n,result)
    
    def inner(self,other):
        result=0
        for i in range(0,self.n):
            result = result + self.lijst[i]* other.lijst[i]
        return result
        
    def norm(self):
        result=0
        for i in range(self.n):
            result = result + self.lijst[i]**2
        return math.sqrt(result)
    
    def project(self, v):
        return self.scalar(v.inner(self)/self.norm()**2)
            
    def orthog(self):
        return self.scalar(1/self.norm())
        
def GrammSchmidt(v):
    u=[v[0]]
    for i in range(1,len(v)):
        result = v[i]
        for j in range(0,i):
            result = result.lincomb(u[j].project(v[i]),1,-1)
        u.append(result)
    for k in range(0,len(v)):
        u[k]=u[k].orthog()
    return u