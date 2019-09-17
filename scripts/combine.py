import os
import glob

'''
Combines blast results into single file. Final output is scaffold (or chromosome), start and end of subject.
In tab separated format.
'''

out_file = 'combined_blast_spipo_v3.txt'

path = '/Users/nathanhepler/Desktop/spipo manuscript/spipo_v3/blast results/short/'


combined = dict()
scaffold_n = list()
locations = list()


def createFile():
    with open(out_file, 'w'):
        pass


def scanner():
    for tt in glob.glob(os.path.join(path, '*.txt')):
        with open(tt, 'r') as file:
            for line in file.readlines():
                if '#' not in line:
                    line = line.strip()
                    line = line.split('\t')

                    scaffold = line[1]
                    start = line[8]
                    end = line[9]

                    scaffold_n.append(scaffold)
                    locations.append((start,end))

                else:
                    pass
            i=0
            for name in scaffold_n:
                combined[locations[i]] = name
                i+=1


def combined_out(in_dict):
    with open(out_file, 'w') as file:
        for val in in_dict:
            file.write(f'{combined[val]}\t{val[0]}\t{val[1]}\n')


createFile()
scanner()
combined_out(combined)