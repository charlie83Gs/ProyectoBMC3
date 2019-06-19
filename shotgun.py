from dissasembler import Dissasembler 
from loader import DNA_DOMAIN , RNA_DOMAIN, ALPHABET, fileLoader
from utilities import randomDNA,randomRNA
from assembler import Assembler

def loadConfig():
        fo = open("test.conf", "r+")
        parameters = []
        lines = fo.readlines()
        for line in lines:
                parameters += [eval(line)]
        fo.close()
        return parameters

def loadFragments(pFile):
        fo = open(pFile, "r+")
        fragments = []
        lines = fo.readlines()
        for line in lines:
                fragments += [line[:len(line)-1]]
        fo.close()
        return fragments

def generate(pSus, pIns, pDel, pChi, pInv, pMinOver, pMaxOver, pFragQuantity, pFragLength, pFragCover, pFile):
	loader = fileLoader(pFile)
	dna = loader.loadALL()
	domain = loader.getDomain()
	#print(domain)
	#randomize dna
	#dna = randomDNA(20000)
	#print(dna)
	print(randomDNA(100))

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


	#assembler = Assembler()
	#fragments = loadFragments("test.frag")
	#assembler.assemble(fragments)






