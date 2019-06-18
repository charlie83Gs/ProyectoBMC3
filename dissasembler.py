
import random
from math import sqrt
from math import floor


'''
TODO
-add multi string support for chimeras, and configuration variable
-add distance confifuration for all other errors
'''
#agregar distribucion uniforme da puntos extra1!

#will take completion over overlapping
class Dissasembler(object):
    
    def __init__(self,pSustitution,pInsertion,pDeletion,pChimeras,pInversion,pMinOverlap,pMaxOverlap,pFragments):
        self.sustitution = pSustitution
        self.insertion = pInsertion
        self.deletion = pDeletion
        self.chimeras = pChimeras
        self.inversion = pInversion
        self.minOverlap = pMinOverlap
        self.maxOverlap = pMaxOverlap
        self.data = ""
        self.visited = []
        self.fragments = pFragments
        self.framentLength = 20
        self.fragmentStandartDeviation = 2
        self.fragmentCoverage = 0
        self.domain = ["A","C","T","G"]
        #random.seed (28)

    #generates and saver fragments with name
    def saveConfiguration(self, pSus, pIns, pDel, pChi, pInv, pMinOver, pMaxOver, pFragQuantity, pFragLength, pFragCover, pFile):
        confFile= open(pFile + ".conf","w+")
        
        confFile.write(str(pSus) + "\n")
        confFile.write(str(pIns) + "\n")
        confFile.write(str(pDel) + "\n")
        confFile.write(str(pChi) + "\n")
        confFile.write(str(pInv) + "\n")
        confFile.write(str(pMinOver) + "\n")
        confFile.write(str(pMaxOver) + "\n")
        confFile.write(str(pFragQuantity) + "\n")
        confFile.write(str(pFragLength) + "\n")
        confFile.write(str(pFragCover))
        
        #write all config parameters of generated fragments
        confFile
        confFile.close()
        
    def saveFragments(self,name):
        fragments = self.generateFragments()
        fragmentFile= open(name+".frag","w+")        

        #store on file
        for fragment in fragments:
            fragmentFile.write(fragment + "\n")
            
        fragmentFile.close()


    def generateFragments(self):
        size = len(self.data)
        newFragments = []
        #fragments assuring coverage and overlap prameters
        if(self.fragmentCoverage > 0):
            newFragments = self.generatePorcentualFragment(self.fragmentCoverage)

        print("generated cover fragments " + str(len(newFragments)))
        #framgents to complete fragment amount my break rules
        # this is because theres is only a limited number of fragments that can
        # be created following the rules
        if(len(newFragments) < self.fragments):
            remainingFragments = self.fragments - len(newFragments)
            newFragments += self.generetaFreeFragment(remainingFragments)

        
        #generate chimera fragments
        chimeras = floor(self.chimeras*len(newFragments))
        while(chimeras > 0):
            firstFragment = random.randint(0, len(newFragments)-1)
            secondFragment = random.randint(0, len(newFragments)-1)
            firstData = newFragments[firstFragment]
            secondData = newFragments[secondFragment]
            mixPoint = random.randint(0, min(len(firstData)-1, len(secondData) -1))
            newFragments[firstFragment] = firstData[:mixPoint] + secondData[mixPoint:] 
            chimeras -=1

        return newFragments

    #all filters
    #a very constrainend fragment generation
    #coverage is a porcentual value betwen 0 and 1
    def generatePorcentualFragment(self,coverage):
        size = len(self.data)
        newFragments = []
        dataPos = 0
        while(dataPos < size):
            newSize = self.getUniformRandomLength()
            overlap = random.randint(self.minOverlap,self.maxOverlap)
            dataPos = max(dataPos-overlap, 0)
            newFragment = self.data[dataPos : dataPos + newSize]
            #add errors to fragment
            newFragment = self.createErrors(newFragment);
            newFragments.append(newFragment)
            dataPos += newSize

        #remove extra fragments
        coverage = min(1,max(0,coverage))
        #calculate the amount of removed fragments
        removed = floor((1-coverage) * len(newFragments))
        while(removed > 0 and len(newFragments) > 0):
            toRemove = random.randint(0, len(newFragments)-1)
            del newFragments[toRemove]
            removed -= 1

        '''
        prev = newFragments[0]
        for f in newFragments:
            print(overlapMax(prev,f))
            prev = f
        '''
        return newFragments
        

    #generates an amount of random fragments
    def generetaFreeFragment(self,totalFragments):
        newFragments = []
        while(totalFragments > 0):
            newSize = self.getUniformRandomLength()
            overlap = random.randint(self.minOverlap,self.maxOverlap)
            #get a random position for the fragment
            dataPos = random.randint(0, len(self.data)-newSize+overlap)
            dataPos = max(dataPos-overlap, 0)
            newFragment = self.data[dataPos : dataPos + newSize]
            #add errors to fragment
            newFragment = self.createErrors(newFragment);
            newFragments.append(newFragment)

            totalFragments -=1

        return newFragments


    def setData(self,newSequence):
        self.data = newSequence
        self.visited = [False] * len(newSequence)

    def setStandartDeviation(self,newDeviation):
        self.fragmentStandartDeviation = newDeviation

    def setFragmentLenght(self, newLength):
         self.framentLength = newLength

    def setFragmentCoverage(self,newCoverage):
        self.fragmentCoverage = newCoverage
    
    def setDomain(self, newDomain):
        self.domain = newDomain
    def getFragmentStart(self):
        return random.randint(0, lend(data)-1)

    def getUniformRandomLength(self):   
        variance = pow(self.fragmentStandartDeviation,2)
        variationRange = sqrt(variance *12)
        rangeHalf = floor(variationRange/2)
        newFragmentLength = self.framentLength + random.randint(-rangeHalf,rangeHalf)
        return newFragmentLength




    def createErrors(self, fragment):
        modifiedFragment = fragment
        #creates sustitutionError
        if(random.random() < self.sustitution):
            newChar = self.domain[random.randint(0,len(self.domain)-1)]
            changeIndex = random.randint(0,len(fragment)-1)
            change_char(modifiedFragment, changeIndex, newChar)
        #create insertion error
        if(random.random() < self.insertion):
            newChar = self.domain[random.randint(0,len(self.domain)-1)]
            changeIndex = random.randint(0,len(fragment)-1)
            modifiedFragment =add_char(modifiedFragment, changeIndex, newChar)
        #create deletion error
        if(random.random() < self.deletion):
            changeIndex = random.randint(0,len(fragment)-1)
            modifiedFragment = remove_char(modifiedFragment,changeIndex)
        #create inversion error
        if(random.random() < self.inversion):
            modifiedFragment = reverse_string(modifiedFragment);

        return modifiedFragment
    

    def setRandomSeed(self,value):
        random.seed (value)



def change_char(s, p, r):
    return s[:p]+r+s[p+1:]

def add_char(s,p,r):
    return s[:p]+r+s[p:]

def remove_char(s,p):
    return s[:p]+s[p+1:]


def reverse_string(s):
    return s[::-1]


def overlapMax(a, b):
    values = (i for i in range(len(b)) if b[i-1] == a[-1] and a.endswith(b[:i]))
    return max(values,default = 0)
