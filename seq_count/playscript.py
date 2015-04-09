#a = open('SRR062634.filt.fastq')

f = open('ntest.fa', 'r')
#print a
#b = a.read()
#c = a.readline()
import re
#c = a.read()
while f:
	print "goint"
	header = f.readline()
        seq = f.readline()
        h2 = f.readline()
        phred = f.readline()
       # print "{0}{1}".format(header, seq)
        print header
	print seq

#	stop
#f.close()
#	if header in r'\@\w*':
#        	print "worked"
#	else:
#        	print "didn't work"

#b = re.split(r"\n",c)

#print b.count('@SRR')
#ids = []
#for i in b:
#	#print i
#	if i in ('+'):
#		b.remove(i)
#
#	if i[0] in ('@'):
#		#print "shoud have worked"
#		ids.append('\w')

#print ids 




#seq_ids = re.findall(r'^\@\w+\d+\.\d+',c,re.M)

#d = re.split(r"\n",c)
#e = []
#f = []
#for i in d:
#	if i in ('+'):
#		d.remove(i)
#	elif ('@') in i:
#		e.append(i)
#	else:
#		f.append(i)		
#rint e
#print f
#print b






#print f






































#b = a.readline()
#print b

#	seq = a.readline()
#	h2 = a.readline()
#	phred = a.readline()
#	print "{0}{1}".format(
#def CheckFormat(file):
#	header = file.readline()
	#if header = @ :
#		type = 'FASTQ'
	#elif header = > :
#		type = 'FASTA'
#	return type


