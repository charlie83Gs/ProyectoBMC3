from dissasembler import Dissasembler 
from loader import DNA_DOMAIN , RNA_DOMAIN, ALPHABET, fileLoader

loader = fileLoader("dna.txt")
dna = loader.loadDNA()
print(dna)