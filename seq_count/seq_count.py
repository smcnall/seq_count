#small bit of code that simply loops through a file and counts how many lines 
#start with the symbol ">"
a = open('/home/smcnall/Mueggle_table/datasets/rna.fa')
ar = a.readlines()
c = 0
for i in ar:
    if i[0] in ('>'):
        c = c+1

print c
