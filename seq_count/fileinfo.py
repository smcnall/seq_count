file = raw_input("file path of .fa file:")
#now we have to make sure that this is not compressed
import gzip
import re
import json
if file.endswith(".gz"):
        a = gzip.open(file)
else:
        a = open(file)

def CheckFormat(a):
	header = a.readline()
	if header[0] in "@":
		type_file = 'FASTQ'
	elif header[0] in ">gi":
		type_file = 'FASTA'
	else:
		type_file = 'BREAK'
		print "incorrect file type"
#		break
	return type_file

if CheckFormat(a) == 'FASTQ':
	print "yay"
elif CheckFormat(a) == 'FASTA':
	print "not so yay"		
