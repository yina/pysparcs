#!/usr/bin/python

import click
from subprocess import Popen, PIPE
import subprocess
import os
import re
import shutil
import sys

@click.command()
@click.option('--inputdir', help='input directory containing medical note with extension must be .text')
@click.option('--yourdeidpath', help='This is the path of your download deid')

def deid(inputdir,yourdeidpath):
    cwd = os.getcwd()
    # test if input data format is "\d+_\d+"
    for notes in os.listdir(inputdir):
        fname_format = re.compile("\d+_\d+")
        if notes.endswith(".text"):
            if fname_format.match(notes):
                print ""
            else:
                print "Please edit your input file name in format \d+_\d+ , for example 1_123.text"

    if os.system("ls -d "yourdeidpath)!=0:
        print "Please download deid-1.1"

    
    else:
        sys.path.append(yourdeidpath)
        deid_path = yourdeidpath
    
        #change working directory to deid package
        os.chdir(yourdeidpath)   

        for notes in os.listdir(inputdir):
            if notes.endswith(".text"):
                notes_new = notes.replace(".text","")
            
       
                pipe = Popen(["perl","deid.pl",inputdir+"/"+notes_new,"deid.config"], stdout = PIPE)
                result = pipe.stdout.read()
    
                # move .res results to a new directory deid_res_output
                source = os.listdir(inputdir)
                destination = cwd+"/deid_res_output/"
    
                for f in source:
                
                    if f.endswith(".res"):
                        shutil.copy(inputdir+"/"+f,destination)
                    #rm files .info .phi .res
                    if f.endswith(".text")!=True:
                        os.remove(inputdir+"/"+f)
                                                
        os.chdir(cwd)     
if __name__ == '__main__':
    deid()


