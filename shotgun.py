from dissasembler import Dissasembler 
from loader import DNA_DOMAIN , RNA_DOMAIN, ALPHABET, fileLoader
from utilities import randomDNA,randomRNA
from assembler import Assembler




loader = fileLoader("dna.txt")

dna = loader.loadDNA()
domain = loader.getDomain()
print(domain)
#randomize dna
dna = randomDNA(200000)
#print(dna)


dissasembler = Dissasembler(0,0,0,0,0,28, 70, 600)
dissasembler.setData(dna)
dissasembler.setFragmentLenght(400)
dissasembler.setFragmentCoverage(0.98)
dissasembler.setDomain(domain)

fragments = dissasembler.generateFragments()
#for f in fragments:
#	print(len(f))


#print(final_s);
#print(fragments)
#print(dissasembler.generateFragments())
print(len(fragments))


assembler = Assembler()

assembler.assemble(fragments)






