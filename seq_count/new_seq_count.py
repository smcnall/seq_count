file = raw_input("file path of .fa file:")
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
#print len(seq_ids),len(seq_lengths)
print "Number of sequences in file:", num_seq
print "Range of sequence lengths:" , min(seq_lengths), "-" , max (seq_lengths)
print "Average sequence length:", sum(seq_lengths)/len(seq_lengths)
#the following prints the sequence ids and lengths to the chosen file in tsv format
outfile = raw_input("what file should this write to?:")

#creates many different dictionaries that can feed into the csv.DictWriter function
#correctly
seq_array = []
counter = 0
for m in seq_ids:
	seq_array.append({'seq_ids':seq_ids[counter], 'seq_lengths':seq_lengths[counter]})
	counter += 1

import csv
#still needs to be checked against a program that only takes tab - delimited files 
fieldnames = ['seq_ids', 'seq_lengths']
csvfile = open(outfile, 'wb')
writer = csv.DictWriter(csvfile, fieldnames = fieldnames, dialect = 'excel-tab')
writer.writerow(dict((fn,fn) for fn in fieldnames))
for row in seq_array:
	writer.writerow(row)

csvfile.close()	
    

