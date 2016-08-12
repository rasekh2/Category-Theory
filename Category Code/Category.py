
class Category(object):
    
    def __init__(self):
        self.objects=[]
        self.morphisms=[]
        
        
    def getObjects(self):
        return self.objects
        
    def getMorphisms(self):
        return self.morphisms
        
    def addObject(self, object):
        self.objects.append(object)
        
    def addMorphism(self,morphism, source, target):
        if source in self.objects and target in self.objects:
            self.morphisms.append((morphism,source,target))
        else:
            return 'Target or source does not exists'
        
cat=Category()
