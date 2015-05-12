import sys
import random
import math

try:
    L= int(sys.argv[1]) 
    N = int(sys.argv[2])
except:
    print('Use: estimate_pi.py N L')

if L>1:
    print('AssertionError: L should be smaller than 1')
elif L==0 or L<0:
    print('AssertionError: L should be smaller than 1')

def drop_needle(L):
        # uniform in [0,1]
        x0 = random.random()
        # uniform in [0,2pi]
        a = random.vonmisesvariate(0,0)
        x1 = x0 + L*math.cos(a)
        if x1>0:
            if x1<1:
                return False
        return True

numberOfHits = 0        
for i in range(1,N):
    if drop_needle(L)==True:
        numberOfHits = numberOfHits+1
    
approxPi = 2*L*N/numberOfHits 
print(numberOfHits, 'hits in', N, 'tries')
print('Pi =', approxPi)