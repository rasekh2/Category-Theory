import pylab

sum=0
l=[1,2,2,3]


def meanandvariance(l):
    sum=0
    for i in l:
        sum+=i
    average = sum/len(l)
    
    suma=0
    for i in l:
        suma+=(average-i)**2
    variance = suma/len(l)     
    return average, variance
    
#print meanandvariance([0,1,2,3,4,5,6,7,8])
#print meanandvariance([5,10,10,10,15])
#print meanandvariance([0,1,2,4,6,8])
#print meanandvariance([6,7,11,12,13,15])
#print meanandvariance([9,0,0,3,3,3,6,6])

def possible_mean(L):
    return sum(L)/len(L)

def possible_variance(L):
    mu = possible_mean(L)
    temp = 0
    for e in L:
        temp += (e-mu)**2
    return temp / len(L)
    
#print possible_mean([0,1,2,3,4,5,6,7,8])

MAXRABBITPOP, CURRENTRABBITPOP, or CURRENTFOXPOP

def rabbitGrowth(CURRENTRABBITPOP, MAXRABBITPOP):
    
    
def foxGrowth(CURRENTFOXPOP):
    
    
def runSimulation:
    