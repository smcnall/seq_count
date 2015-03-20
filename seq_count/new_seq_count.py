file = raw_input("filepath of .fa file:")
#now we have to make sure that this is not compressed
import gzip
import re
import json
if file.endswith(".gz"):
        a = gzip.open(file)
else:
        a = open(file)
b = a.read()
#to count the number of sequences
num_seq = b.count('>')

#for a list of sequence identifiers
seq_ids = re.findall(r'\gi\|\d*',b)

#then to get sequence lengths:
#splits into unique sequences with header attached
seqs = re.split(r'\>',b)
#removes the '' at beggining of list(may be a way to fix this so it is not
#necessary
seqs.remove(seqs[0])
seq_lengths = []
for i in seqs:
	#takes each sequence and splits it back into rows
	seqs2 = re.split(r"\n",i)
	#removes the header row
	seqs2.remove(seqs2[0])
	#combines the remaining sequence into a single string
	seqs3 = ''.join(seqs2)
	#adds the length of that string to a new list
	seq_lengths.append(len(seqs3))
#used to verify that the number of sequences and the number of sequence lengths are the same
print len(seq_ids),len(seq_lengths)

#now to add all the flashy print functions and transfer the code that writes the outputs to a tab
#deliniated file



