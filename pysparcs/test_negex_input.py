#!/usr/bin/python

import nose
    import negex_input

@click.command()
@click.option('--f1', help='extracted concepts file from cTakes without extension')
@click.option('--f2', help='medical note file without extension')
@click.option('--outdir', help='output directory')
@click.option('--inputdir', help='input directory')


def test_negex_input():
    assert negex_input(inputdir,f1,f2,outdir)
if __name__ == '__main__':
        nose.runmodule()


            







				


