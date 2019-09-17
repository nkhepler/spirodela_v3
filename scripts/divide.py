'''

Identify genes on same region and create separate files for each

'''

inputFile = '/Users/nathanhepler/Desktop/spipo manuscript/spipo_v3/spipo_v3_retrieved_sequences.txt'


def readFile(inputFile):
    seqNames = dict()
    sequence = ''
    header = ''
    with open(inputFile, 'r') as file:
        for line in file.readlines():
            line = line.rstrip()
            if '>' in line:
                header = line
                seqNames[header] = ''
                sequence = ''
            else:
                sequence = sequence + line
                seqNames[header] = sequence
    return seqNames


def scaffoldSep(seqNames):
    names = list()
    for key in seqNames:
        name = key.split('.')
        names.append(name[0])
    names = set(names)
    for val in names:
        filename = f'/Users/nathanhepler/Desktop/spipo manuscript/spipo_v3/scaffolds/{val[1:]}.txt'
        with open(filename, 'w') as doc:
            for key in seqNames:
                if val in key:
                    doc.write(f'{key}\n{seqNames[key]}\n')


s = readFile(inputFile)
scaffoldSep(s)
