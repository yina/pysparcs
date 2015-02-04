#!/usr/bin/python

import re
import sys
import click
#import subprocess
import os

@click.command()
@click.option('--f1', help='extracted concepts file from cTakes without extension')
@click.option('--f2', help='medical note file without extension')
@click.option('--outdir', help='output directory')


    file1 = open(f1+".txt","r")
    file2 = open(f2+".txt","r")
    outfile = open(outdir+"/"+f2+'_negexinput.txt', 'w')
    logfile = open(outdir+"/"+f2+'_log.txt','w')
    outfile.write('Report No.'+'\t'+'Concept'+'\t'+'\t'+'Sentence'+'\n')


    concepts = file1.readlines()
    mynote = file2.readlines()
    mynote_new = filter(lambda x: x not in '\n',mynote)
    for i in range(len(concepts)):
        tmp = concepts[i].rstrip()
#        print tmp
        for lines in mynote_new: 
            str_split = re.split(r"\t| {2,9}|\.|\;",lines) # splitting on periods, semicolons, 2 to 9 multiple spaces
            for s in str_split:
                mymatch = re.findall(tmp,s)
                if len(mymatch)>0:
                    outfile.write('1'+'\t'+tmp+'\t'+"\""+s+"\""+'\n')
                    if len(re.findall(tmp,s)) > 1:
                        logfile.write(tmp+":Mutiple occurence in:"+s+"\n")
                        
if __name__ == '__main__':
    negex_input()
    
        
# add test case
# nosetests
# replace tab in sentence before writing
# intermediate file should be tmp
# use system call to start negex
# add pretest to see if negex exists.
# add documentation about where breaks are.

            







				


