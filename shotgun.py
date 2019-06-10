from dissasembler import Dissasembler 
from loader import DNA_DOMAIN , RNA_DOMAIN, ALPHABET, fileLoader
from utilities import randomDNA,randomRNA
from assembler import Assembler




loader = fileLoader("dna.txt")

dna = loader.loadDNA()
domain = loader.getDomain()
print(domain)
#randomize dna
dna = randomDNA(20000)
#print(dna)


dissasembler = Dissasembler(0,0,0,0,0,5, 12, 600)
dissasembler.setData(dna)
dissasembler.setFragmentLenght(40)
dissasembler.setFragmentCoverage(0.8)
dissasembler.setDomain(domain)

fragments = dissasembler.generateFragments()




#print(final_s);
#print(fragments)
#print(dissasembler.generateFragments())
print(len(fragments))


assembler = Assembler()

assembler.assemble(fragments)






