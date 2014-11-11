
#!usr/bin/python
# use pandas package to merge data: prime1 and secndr_a/secndr

import pandas as  pd
import sys

df1=pd.read_csv('./'+sys.argv[1]+'.DAT_prime1.csv',dtype=str)
df2=pd.read_csv('./'+sys.argv[1]+'.DAT_secndr_a.csv',dtype=str)


#check if the same variable name means the same things respectively

#same_var=set(list(df1.columns)).intersection(list(df2.columns))
#print same_var
print "readya"

OP_merge =pd.merge(df1,df2,on='DISCHNO',how='outer',suffixes=['_prime','_secndr'])

# have the 'DISCHINO' to be the first column

index=OP_merge.columns.get_loc('DISCHNO')
print index

mylist=OP_merge.columns.tolist()
new_col=mylist[index:index+1]+mylist[0:index]+mylist[index+1:]
OP=OP_merge[new_col]

OP.to_csv('OP'+sys.argv[2]+'.csv')
print "bingo"
