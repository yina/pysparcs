#!/usr/bin/python

import click
from subprocess import Popen, PIPE
import os


@click.command()
@click.option('--note', help='input medical note,filename without extension, where extension must be .text')
@click.option('--outdir', help='output directory, there are three output files, we are interested in <input>.res file')

def deid(note,outdir):
    # deid package path can be modified
    if os.path.exists("/Users/yu/Documents/deid-1.1") != True:
        print "Please download deid-1.1."
    else:

        pipe = Popen(["perl","deid.pl",note,"deid.config",outdir],  stdout = PIPE)

        result = pipe.stdout.read()

        print result
if __name__ == '__main__':
    deid()
    