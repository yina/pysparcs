#!/usr/bin/python

import click
from subprocess import Popen, PIPE
import os
import re
import shutil


@click.command()
@click.option('--note', help='input medical note,filename without extension, where extension must be .text')
#@click.option('--outdir', help='output directory, there are three output files, we are interested in <input>.res file')

def deid(note):
    # test if input data format is "\d+_\d+"
    fname_format = re.compile("\d+_\d+")
    if fname_format.match(note):
        print ""
    else:
        print "Please edit your input file name format."
    
#    p = subprocess.checkoutput(["echo $PATH"], shell = True)
#    path_var = p.stdout.read()
#    print path_var
#    if "negex.python" not in path_var:
#        print "Please download negex.python and add to $PATH"
#    else:    

    cwd = os.getcwd()
    if os.path.exists(cwd+"/deid-1.1") != True:
        print "Please download deid-1.1 to current directory."
    else:
        pipe = Popen(["perl","deid.pl",note,"deid.config","deid_output"],  stdout = PIPE)
        result = pipe.stdout.read()
                    
        # move .res results to a new directory deid_res_output
        source = os.listdir("deid_output/")
        destination = "deid_res_output"
        for f in source:
            if f.endswith(".res"):
                shutil.copy("deid_output/"+f,destination)
        
if __name__ == '__main__':
    deid()


#optional input as file, directory, or multiple files: ask mail list person, they said cannot take multiple files and it is better to qsub them with shell script or concatenate to one.