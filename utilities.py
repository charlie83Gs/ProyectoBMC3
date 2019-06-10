import random



def randomDNA(size):
	newDNA = ""
	validchar =  ["A","C","T","G"]
	while(size > 0 ):
		newdnapiece = random.randint(0,len(validchar) -1)
		newDNA += validchar[newdnapiece]
		size -=1
	return newDNA


def randomRNA(size):
	newDNA = ""
	validchar =  ["A","C","U","G"]
	while(size > 0 ):
		newdnapiece = random.randint(0,len(validchar) -1)
		newDNA += validchar[newdnapiece]
		size -=1
	return newDNA