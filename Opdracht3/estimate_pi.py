#!/usr/bin/python3
import sys
import random
import math

try:
    N = int(sys.argv[1])    
    L = float(sys.argv[2]) 
except:
    print('Use: estimate_pi.py N L seed')
    sys.exit()

SeedActivated=False
try:
    seed = int(sys.argv[3])
    SeedActivated=True
except: {}

if L>1:
    print('AssertionError: L should be smaller than 1')
    sys.exit()
elif L==0 or L<0:
    print('AssertionError: L should be smaller than 1')
    sys.exit()
    
def drop_needle(L):
        x0 = random.random()
        a = random.vonmisesvariate(0,0)
        x1 = x0 + L*math.cos(a)
        if x1>0:
            if x1<1:
                return False
        return True
    
numberOfHits = 0     
if SeedActivated==True:
        random.seed(seed)
for i in range(1,N):
    if drop_needle(L):
        numberOfHits = numberOfHits+1
            
    
approxPi = 2*L*N/numberOfHits 
print(numberOfHits, 'hits in', N, 'tries')
print('Pi =', approxPi)