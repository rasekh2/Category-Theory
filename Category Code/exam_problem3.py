import random
import pylab
import numpy
import math

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    global MAXRABBITPOP
    
    population = CURRENTRABBITPOP
    for rabbit in range(population):
        if CURRENTRABBITPOP==1000:
            break
        if random.random() < 1.0 - float(CURRENTRABBITPOP)/float(MAXRABBITPOP):
            CURRENTRABBITPOP+=1
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global MAXRABBITPOP
    global CURRENTFOXPOP
    
    population = CURRENTFOXPOP
    for fox in range(population):
        if CURRENTRABBITPOP <=10:
            break
        if random.random() < float(CURRENTRABBITPOP)/float(MAXRABBITPOP):
            CURRENTRABBITPOP-=1
            if random.random()<1.0/3.0:
                CURRENTFOXPOP+=1
        else:
            if random.random() < 9.0 / 10.0 and CURRENTFOXPOP>10:
                CURRENTFOXPOP-=1        
        
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    
    global MAXRABBITPOP 
    global CURRENTRABBITPOP 
    global CURRENTFOXPOP 
    rabbitpopulation = []
    foxpopulation = []
    for step in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbitpopulation.append(CURRENTRABBITPOP)
        foxpopulation.append(CURRENTFOXPOP)
        
    return (rabbitpopulation,foxpopulation)
 
tuple = runSimulation(200)

pylab.figure(1) #create figure 1
pylab.title('Rabbit Population')
pylab.xlabel('Time')
pylab.ylabel('Numbers of Rabbits')
pylab.plot(tuple[0]) #draw on figure 1
#pylab.show()
pylab.savefig('Rabbit Population')
pylab.figure(2) #create figure 2
pylab.plot(tuple[1]) #draw on figure 2
pylab.title('Fox Population')
pylab.xlabel('Time')
pylab.ylabel('Numbers of Foxes')
#pylab.show()
pylab.savefig('Fox Population') #save figure 1  

coeff = numpy.polyfit(range(200),tuple[1],2)
a=math.floor(coeff[0]*100000)/100000

b=math.floor(coeff[1]*100000)/100000

c=math.floor(coeff[2]*100000)/100000

list=[]
for step in range(200):
    list.append(a*step**2 + b*step + c)

pylab.figure(3)
pylab.plot(list)
pylab.show()