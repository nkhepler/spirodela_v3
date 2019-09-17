import fileinput

def addSeq(file):
	seqNames = dict()
	sequence = ''
	header = ''
	for line in file:
		line = line.rstrip()
		if '+' in line:
			pass
		elif '?' in line:
			pass
		elif '@' in line:
			header = line
			seqNames[header] = ''
			sequence = ''
		elif '@' not in line:
			sequence = sequence + line
			seqNames[header] = sequence

	return seqNames

def readOut(final):
	for key in seqNames:
		print(f"{key.replace('@', '>')}\n{seqNames[key]}")


file = fileinput.input()
seqNames = addSeq(file)
final = readOut(seqNames)