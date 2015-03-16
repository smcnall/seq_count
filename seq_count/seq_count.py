#small bit of code that simply loops through a file and counts how many lines 
#start with the symbol ">"
a = open('/home/smcnall/Projects/seq_count/rna.fa')
ar = a.readlines()
#counting variable for keeping track of the number of sequences
c = 0
#keeps track of the length of a sequence, is reset to zero if value is appended into f
d = 0
#a running variable for the total base pairs to be used later for average sequence length
g = 0
#string lengths stored as string variables, may need to be taken out at a later point but for now
#this is the only way to make it go off without an error
e = ('')
#list of sequence lengths
f = []
#used to convert strings in f back to integers
x = []
for i in ar:
	if i[0] in ('A','T','G','C'):
		d += len(i)
		g += len(i)
    	if i[0] in ('>'):
        	c += 1
		e = str(d)
		if d != 0:
			f.append(e)
		d = 0
for n in f:
	x.append(int(n))	
		
print "Number of sequences:",c
print "Range of sequence length:",min(x),"-",max(x)
print "Average sequence length:", g/c

