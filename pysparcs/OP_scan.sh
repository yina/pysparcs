#!/bin/bash
#$ -cwd
#$ -S /bin/bash


# list1 is target string 
# list1="179,18000,1808,1809,181,18200,18201,1828,18300,18302,18303,1834,1835,1838,1839,18400,1849,23301,23302,23331,7213,62210,62211,62212,62300,15800,1588,1589,23600,23601,23602,23603"

#list2 is the columns to be filtered
list2="312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337"

list1=$1
file=$2
awk -v "list1=$list1" -v "list2=$list2" -F "," 'BEGIN { split (list1,tmp,",");split(list2,tmp2,",");for (i in tmp) targets[tmp[i]] } { for (j = 1; j <=26 ; j++) if ($tmp2[j] in targets) {print $0} }' $file.csv > $file'_tmp'.csv
chmod 700 *
cut -d "" -f1 $file'_tmp'.csv |  uniq > $file'_filter'.csv
chmod 700 *

## add header to final output
head -1 $file.csv > $file'_header'.csv
sed -i 1i$(cat $file'_header'.csv) $file'_filter'.csv

#sort -t ',' -u -k2 $file'_filter'.csv > $file'_filter_uniq'.csv




