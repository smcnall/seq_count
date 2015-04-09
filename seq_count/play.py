#!/bin/
#f = open('SRR062634.filt.fastq')
a = 0
f = open('test.fa', 'r')
import re
#c = a.read()
#while f:
#        header = f.readline()
#        seq = f.readline()
#        h2 = f.readline()
#        phred = f.readline()
#       	print "{0}{1}".format(header, seq)
#	a += 1
#	if a > 5:
#		break
	
headers = []
seqs = []
while f:
        header = f.readline()
        j = re.findall(r'\@\w+\d+\.\d+',header)
	headers.append(j)
	seq = f.readline()
	k = len(seq)
        seqs.append(k)
	h2 = f.readline()
        phred = f.readline()
        #print "{0}{1}".format(header, seq)
        
	if header in ("\n"):
                break

seq_ids = headers
seq_lengths = seqs


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




#b = a.readline()
#print b

#       seq = a.readline()
#       h2 = a.readline()
#       phred = a.readline()
#       print "{0}{1}".format(
#def CheckFormat(file):
#       header = file.readline()
        #if header = @ :
#               type = 'FASTQ'
        #elif header = > :
#               type = 'FASTA'
#       return type




