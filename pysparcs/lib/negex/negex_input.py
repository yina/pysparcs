#!/usr/bin/python

import re
import sys
import click
import subprocess
import os

@click.command()
@click.option('--f1', help='extracted concepts file from cTakes without extension')
@click.option('--f2', help='medical note file without extension')
@click.option('--outdir', help='output directory')
@click.option('--inputdir', help='input directory')



def negex_input(inputdir,f1,f2,outdir):
    
#    p = subprocess.checkoutput(["echo $PATH"], shell = True)
#    path_var = p.stdout.read()
#    print path_var
#    if "negex.python" not in path_var:
#        print "Please download negex.python and add to PATH"
#    else:
        
    cwd = os.getcwd()
    if os.path.exists(cwd+"/negex.python") != True:
        print "Please download negex to current directory."
    else:

        negex_path = os.path.dirname(os.path.realpath("negex.python"))
        file1 = open(inputdir+"/"+f1+".txt","r")
        file2 = open(inputdir+"/"+f2+".txt","r")
        
        logfile = open(outdir+"/"+f2+'_log.txt','w')
        outfile = open(outdir+'/'+f2+'_negexinput.txt', 'w')
        outfile.write('Report No.'+'\t'+'Concepts'+'\t'+'Sentence'+'\n')


        concepts = file1.readlines()
        mynote = file2.readlines()
        mynote_new = filter(lambda x: x not in '\n',mynote)
        for i in range(len(concepts)):
            cpt = concepts[i].rstrip()
            for lines in mynote_new: 
                str_split = re.split(r"\t| {2,9}|\.|\;",lines) # splitting on periods, semicolons, 2 to 9 multiple spaces
                for s in str_split:
                    mymatch = re.findall(cpt,s)
                    if len(mymatch)>0:
                        s = s.replace("\t"," ")
                        outfile.write('1'+'\t'+cpt+'\t'+"\""+s+"\""+'\n')
                        if len(re.findall(cpt,s)) > 1:
                            logfile.write(cpt+":Mutiple occurence in:"+s+"\n")
                        
        pipe = os.popen("python "+cwd+"/negex.python/wrapper.py "+outdir+" negex_out "+f2+'_negexinput.txt','w',1) 
if __name__ == '__main__':
    
    negex_input()
    
                
        


                
            







				


