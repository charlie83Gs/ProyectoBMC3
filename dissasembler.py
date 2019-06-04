

#will take completion over overlapping
class Dissasembler(object):
    
    def __init__(self,pSustitution,pInsertion,pDeletion,pChimeras,pInversion,pMinOverlap,pMaxOverlap):
        self.sustitution = pSustitution
        self.insertion = pInsertion
        self.deletion = pDeletion
        self.chimeras = pChimeras
        self.inversion = pInversion
        self.minOverlap = pMinOverlap
        self.maxOverlap = pMaxOverlap
        self.domain = []
        self.data = ""
        self.visited = []

    def generateFragment():
        size = len(self.data)



    def setData(newSequence):
        self.data = newSequence
        self.visited = [false] * len(newSequence)
