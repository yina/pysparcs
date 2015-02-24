from negex import *
import negex_input
import csv
import sys
print(sys.argv[1]) # input dir
print(sys.argv[2]) # output dir
print(sys.argv[3]) # negex_input file


def main():
    rfile = open(r'negex_triggers.txt')
    irules = sortRules(rfile.readlines())
    reports = csv.reader(open(('./'+sys.argv[1]+'/'+sys.argv[3]),'rb'), delimiter = '\t')
    reports.next()
    reportNum = 0
    ofile = open(r'./'+sys.argv[2]+'/negated_'+sys.argv[3], 'w')
    output = []
    outputfile = csv.writer(ofile, delimiter = '\t')
    for report in reports:

        tagger = negTagger(sentence = report[2], phrases = [report[1]], rules = irules, negP=False)
        # list.append : add another column to a list
        report.append(tagger.getNegTaggedSentence())
        #see how many items in the list after tagger.getNegTaggeredSetence
        report.append(tagger.getNegationFlag())
        size=len(report)

#       if 1==1:
        output.append(report)

    for row in output:
        if row:
            outputfile.writerow(row)
    ofile.close()

if __name__ == '__main__': main()
