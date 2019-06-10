from dissasembler import Dissasembler 
from loader import DNA_DOMAIN , RNA_DOMAIN, ALPHABET, fileLoader
from utilities import randomDNA,randomRNA





loader = fileLoader("dna.txt")

dna = loader.loadDNA()
domain = loader.getDomain()
print(domain)
#randomize dna
dna = randomDNA(6000)
#print(dna)


dissasembler = Dissasembler(0,0,0,0,0,2, 5, 400)
dissasembler.setData(dna)
dissasembler.setFragmentCoverage(0.8)
dissasembler.setDomain(domain)

#print(dissasembler.generateFragments())
print(len(dissasembler.generateFragments()))











