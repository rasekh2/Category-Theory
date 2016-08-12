

class Location(object):
    
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y
        
    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        #if self.x+deltaX > -60 and self.x+deltaX < 60:
        #    self.x += deltaX
        #if  self.y+deltaY > -60 and self.y+deltaY < 60:
        #    self.y += deltaY
        x=self.x
        y=self.y
        dx=deltaX
        dy=deltaY
        #if x+dx > -60 and self.x+dx < 60:
        #    x += dx
        #elif x+dx > 60:
        #    x = -60 + (x+dx - 60)
        #elif x+dx < -60:
        #    x = 60 - (-60 - (x+dx))
        #
        #if  y+dy > -60 and y+dy < 60:
        #    y += dy
        #elif y+dy > 60:
        #    y = -60 + (y+dy - 60)
        #elif y+dy < -60:
        #    y = 60 - (-60 - (y+dy))
        if x+dx <60 and x+dx > -60 and y+dy < 60 and y+dy > -60:
            x += dx
            y += dy
        else:
            x = 0
            y = 0
        self.x=x
        self.y=y
        return Location(self.x, self.y)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5
    
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'





class Field(object):
    
    def __init__(self):
        self.drunks = {}
        
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
            
    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        #use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)
        
    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]


import random
import pylab

class Drunk(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'This drunk is named ' + self.name
    
class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
	[(-1.0,-1.0),(-1.0,0.0),(-1.0,1.0),(0.0,1.0),(0.0,-1.0),(1.0,-1.0),
	(1.0,0.0),(1.0,1.0)]
        return random.choice(stepChoices)

def walk(f, d, numSteps):
    #start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return f.getLoc(d)
    

def simWalk(numSteps):
    homer = UsualDrunk('Homer')
    origin = Location(0, 0)
    #positions=[]
    f = Field()
    f.addDrunk(homer, origin)
    #positions.append(walk(f, homer, numSteps))
    return walk(f, homer, numSteps)

print simWalk(10).getX()
    
def drunkTestA(number):
    finallist=[]
    for test in range(number):
        finallist.append(simWalk(2000))
    xlist=[]
    ylist=[]
    for test in range(number):
        xlist.append(finallist[test].getX())
        ylist.append(finallist[test].getY())
    pylab.figure(1)
    pylab.plot(xlist,ylist,'o')
    pylab.title('Mean Distance from Origin')
    pylab.xlabel('Steps Taken')
    pylab.ylabel('Steps from Origin')
    pylab.show()

drunkTestA(5000)


##########################################################################
def simWalks(numSteps, numTrials=1):
    homer = UsualDrunk('Homer')
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(homer, origin)
        distances.append(walk(f, homer, numSteps))
    return distances

def drunkTestP(numTrials = 50):
    stepsTaken = [10, 100, 1000, 10000]
    meanDistances = []
    for numSteps in stepsTaken:
        distances = simWalks(numSteps, numTrials)
        meanDistances.append(sum(distances)/len(distances))
    pylab.plot(stepsTaken, meanDistances)
    pylab.title('Mean Distance from Origin')
    pylab.xlabel('Steps Taken')
    pylab.ylabel('Steps from Origin')
    pylab.show()