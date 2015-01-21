#!/usr/bin/python

import re
import sys

# This  will detect if before or after 50 characters of the concept contains periods. 
# If there is, just output the strings between/after/before periods.
class Fragment:
    def __init__(self,pos,str,keyword):
        start = pos-50 if pos-50 >= 0 else 0
        end = pos+50+len(keyword)-1 if pos+50+len(keyword)-1<=len(str)-1 else len(str)-1
        temp = str[start:end]
#        print temp
        ts = temp.split('.')
#       print ts
        tp = -50 if pos-50 >= 0 else -pos
        for s in ts:
#            print s
#            print tp
#            print tp+len(s)
#            print len(keyword)
            if(tp<=0 and tp+len(s)>=len(keyword)):
                
                
#               print len(keyword)
                self.pos = pos+tp
                self.str = s
                break
            else: 
                tp = tp+len(s)+1

# file1 is the list of umls identified concepts
# file2: replace \t \n or multiple spaces to one space

# consolidate to one script
# use click if needed http://click.pocoo.org/3/
# add documentation strings 
# outfile as option
# window size as option

file1 = open(sys.argv[1],"r")
file2 = open(sys.argv[2],"r")
outfile = open(r'py_intonegex.txt', 'w')
outfile.write('Report No.'+'\t'+'Concept'+'\t'+'\t'+'Sentence'+'\n')
#ofile=csv.writer(outfile,delimiter='\n')

concepts = file1.readlines()
mynote = file2.readlines()
#for concept in concepts:
for i in range(len(concepts)):
#   print concepts[i].rstrip()
    tmp = concepts[i].rstrip()
#   print tmp
    for mymatch in re.finditer(tmp,mynote[0]):
#   	print mymatch.group()
#       print mymatch.start()
        s = mymatch.start()
        
#       e = mymatch.end()
#		print mynote[0][s-50:e+50]
        frag = Fragment(s,mynote[0],tmp)
#       print frag.pos
#       print frag.str
        outfile.write('1'+'\t'+tmp+'\t'+"\""+frag.str+"\""'\n')
                 





				


