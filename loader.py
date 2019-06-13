
DNA_DOMAIN =    {'A' : True,'C' : True,'G' : True,'T' : True}
RNA_DOMAIN =    {'A' : True,'C' : True,'G' : True,'U' : True}
ALPHABET =      {'A' : True,'B' : True,'C' : True,'D' : True,'E' : True,'F' : True,'G' : True,'H' : True,'I' : True,'J' : True,'K' : True,'L' : True,'M' : True,'N' : True,'O' : True,'P' : True,'Q' : True,'R' : True,'S' : True,'T' : True,'U' : True,'V' : True,'W' : True,'X' : True,'Y' : True,'Z' : True,' ' : True}



class fileLoader(object):
	
	def __init__(self, pFileName):
		self.fileNmae = pFileName
		self.domain = set()

	def loadDNA(self):
		#file is loaded and all characters become capitalized
		file=open(self.fileNmae, "r")
		data = file.read().upper()
		file.close()
		data = self.filter(data,DNA_DOMAIN)
		return data;

	def loadRNA(self):
		file=open(self.fileNmae, "r")
		data = file.read().upper()
		file.close()
		data = self.filter(data,RNA_DOMAIN)
		return data;

	def loadALPHABETIC(self):
		file=open(self.fileNmae, "r")
		data = file.read().upper()
		file.close()
		data = self.filter(data,ALPHABET)
		return data;

	def loadALL(self):
		#file is loaded and all characters become capitalized
		file=open(self.fileNmae, "r")
		data = file.read().upper()
		file.close()
		return data;

	def filter(self,original,domain):
		processed = ""
		for c in original:
			if(domain[c] == True):
				self.domain.add(c)
				processed += c

		return processed

	def getDomain(self):
		return list(self.domain)
