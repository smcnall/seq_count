#small bit of code that simply loops through a file and counts how many lines 
#start with the symbol ">"
#standard method of file input:
#a = open('/home/smcnall/Projects/seq_count/rna.fa')

#new attempt at file input:
file = raw_input("filepath of .fa file:")
#now we have to make sure that this is not compressed
import gzip
if file.endswith(".gz"):
	a = gzip.open(file)
else:
	a = open(file)
ar = a.readlines()
#counting variable for keeping track of the number of sequences
c = 0
#keeps track of the length of a sequence, is reset to zero if value is appended into f
d = 0
#a running variable for the total base pairs to be used later for average sequence length
g = 0
#list of sequence lengths
f = []
#used to convert strings in f back to integers
x = []
for i in ar:
	if i[0] not in ('>'):
		d += len(i)
		g += len(i)
    	if i[0] in ('>'):
        	c += 1
		if d != 0:
			f.append(d)
		d = 0	
		
print "Number of sequences:",c
print "Range of sequence length:",min(f),"-",max(f)
print "Average sequence length:", g/c

