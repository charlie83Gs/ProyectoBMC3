from dissasembler import Dissasembler 
from loader import DNA_DOMAIN , RNA_DOMAIN, ALPHABET, fileLoader
from utilities import randomDNA,randomRNA
from assembler import Assembler



def generate(pSus, pIns, pDel, pChi, pInv, pMinOver, pMaxOver, pFragQuantity, pFragLength, pFragCover, pFile):
	loader = fileLoader(pFile)
	dna = loader.loadDNA()
	domain = loader.getDomain()
	#print(domain)
	#randomize dna
	dna = randomDNA(20000)
	#print(dna)

	dissasembler = Dissasembler(pSus, pIns, pDel, pChi, pInv, pMinOver, pMaxOver, pFragQuantity)
	dissasembler.setData(dna)
	dissasembler.setFragmentLenght(pFragLength)
	dissasembler.setFragmentCoverage(pFragCover)
	dissasembler.setDomain(domain)

	#fragments = dissasembler.generateFragments()
	dissasembler.saveFragments("test")
	dissasembler.saveConfiguration(pSus, pIns, pDel, pChi, pInv, pMinOver, pMaxOver, pFragQuantity, pFragLength, pFragCover, "test")
	#for f in fragments:
	#	print(len(f))


	#print(final_s);
	#print(fragments)
	#print(dissasembler.generateFragments())
	#print(len(fragments))


	assembler = Assembler()

	#assembler.assemble(fragments)






