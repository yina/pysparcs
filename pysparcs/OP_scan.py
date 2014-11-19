#!/bin/python

import sys
import subprocess
# list1 is the filter value,in this case list1="E"
#list2 is the columns to be filtered,in this case, filter claimtype=="E",claimtype is the 39th column in prime1 data.so list2="39"
#file is the filename,in this case, file=LIMITEDOP_#.DAT_prime1

#list1=sys.argv[1]
#file=sys.argv[2]

command1= "head -1 "+sys.argv[2]+'.csv'+" > "+sys.argv[2]+'_header.csv'
#print command1
subprocess.call(command1,shell=True)

command2= ''' awk -v list1='''+sys.argv[1]+''' -v list2="2" -F "," 'BEGIN { split (list1,tmp,",");split(list2,tmp2,",");for (i in tmp) targets[tmp[i]] } { for (j = 1; j <=1 ; j++) if ($tmp2[j] in targets) {print $0} }' ''' +sys.argv[2]+'.csv'+ ''' | cut -d "" -f1 | uniq >'''+sys.argv[2]+'_filter.csv'
#print command2

subprocess.call(command2,shell=True)
## add header to final output
command3="sed -i 1i$(cat "+sys.argv[2]+'_header.csv'+") "+sys.argv[2]+'_filter.csv'
#print command3
subprocess.call(command3,shell=True)



