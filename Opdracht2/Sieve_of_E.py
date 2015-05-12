import sys
import math
import time

limit = int(sys.argv[1])
bestand = sys.argv[2]


primeChecklist = list(range(0, limit))
primeChecklist[1] = 0
T1 = time.perf_counter()
for i in range(2,math.ceil(math.sqrt(limit))):
    if primeChecklist[i]!=0:
        for n in range(2,math.ceil(limit/i)):
            primeChecklist[i*n]=0
T2 = time.perf_counter()
listOfPrimes = open(bestand, 'w')
numberOfPrimes = 0
numberOfTwinPrimes = 0
for i in range(2,limit):
    if primeChecklist[i]!=0:
        numberOfPrimes = numberOfPrimes+1
        listOfPrimes.write(str(primeChecklist[i]) + "\n")
        if primeChecklist[i-2]==0:
            numberOfTwinPrimes = numberOfTwinPrimes+1
        elif primeChecklist[i-2]==0:
            numberOfTwinPrimes = numberOfTwinPrimes+1
computingTime = T2-T1
    #largestPrime = listOfPrimes.readline()
    #NlogN = largestPrime/math.log(largestPrime)
    #ratio = numberOfPrimes/NlogN
    #c=0.66016181584686957392781211001
    #NTlogN = 2*c*largestPrime / math.log(largestPrime)^2
    #ratioTwin=numberOfTwinPrimes/NTlogN
    


print('Found', numberOfPrimes, 'Prime numbers smaller than', limit, 'in', computingTime, 'sec.')
#print('--------------------------------------------')
# print('Largest Prime = '+ largestPrime)
# print('--------------------------------')
# print('pi(N) = ' + numberOfPrimes)
# print('N/log(N) = '+ NlogN)
# print('ratio = ' + ratio)
# print('--------------------------------')
# print('pi_2(N) = ' + numberOfTwinPrimes)
# print('2CN/log(N)^2 = ' + NTlogN)
# print('ratio = ' + ratioTwin)
    
