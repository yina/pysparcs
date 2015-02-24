#!/usr/bin/python

import click
from subprocess import Popen, PIPE
import subprocess
import os
import re
import shutil
import sys
import timeit

@click.command()
@click.option('--inputdir', help='input directory containing medical note with extension must be .text')
@click.option('--yourdeidpath', help='This is the path of your download deid')

def deid(inputdir):
    cwd = os.getcwd()
    # test if input data format is "\d+_\d+"
    for notes in os.listdir(inputdir):
        fname_format = re.compile("\d+_\d+")
        if notes.endswith(".text"):
            if fname_format.match(notes):
                print ""
            else:
                print "Please edit your input file name in format \d+_\d+ , for example 1_123.text"
                return -1

#    if os.system("ls -d "+yourdeidpath)!=0:
#        print "Please download deid-1.1"
	
    else:
#        sys.path.append(yourdeidpath)
#        deid_path = yourdeidpath
    
        #change working directory to deid package
        os.chdir(cwd+'/deid-1.1')   
        #output directory is deid_res_output
        if not os.path.exists(cwd+"/deid_res_output/"):
            os.makedirs(cwd+"/deid_res_output/")
            
       
        for notes in os.listdir(inputdir):
            
            if notes.endswith(".text"):
                
                notes_new = notes.replace(".text","")
                tmplst = re.split("_",notes_new)
                
                # extract the note number from the first line, o.w it will be deided.
                # sos.system('''awk -v var1='''+tmplst[0]+''' -v var2='''+tmplst[1]+''' 'BEGIN{print "START_OF_RECORD="var1"||||"var2"||||"\n}{print}END{print "||||END_OF_RECORD"}' '''+inputdir+'''/'''+notes_new+'''.text > '''+inputdir+'''/'''+notes_new+'''.tmp.text ''')
                tmpfile = open(inputdir+'/'+notes,"r")
                tmpfileout = open(inputdir+'/'+notes_new+'.tmp.text', 'w')
                tmpdata = tmpfile.readlines()
                
                tmpdata[0] = "START_OF_RECORD="+tmplst[0]+"||||"+tmplst[1]+"||||"+"\n"
                tmpdata.append("||||END_OF_RECORD")
                tmpfileout.writelines(tmpdata)
                tmpfileout.close()

                pipe = Popen(["perl","deid.pl",inputdir+"/"+notes_new+'.tmp',"deid.config"], stdout = PIPE)
                result = pipe.stdout.read()
    
                # move .res results to a new directory deid_res_output
                source = os.listdir(inputdir)
                destination = cwd+"/deid_res_output/"
    
                for f in source:
                
                    if f.endswith(".res"):
                        shutil.copy(inputdir+"/"+f,destination)
                    #rm files .info .phi .res
                    if f.endswith(".text")!=True or f.endswith(".tmp.text"):
                        os.remove(inputdir+"/"+f)
            
        os.chdir(cwd)
        return 0    
if __name__ == '__main__':
    deid()


