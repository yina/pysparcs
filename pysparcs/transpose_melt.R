
#!/bin/Rscript
setwd("/ifs/home/liangy03/IPfilter")

#install.packages("reshape",repos='http://cran.mirrors.hoobly.com')
library(reshape)

args <- commandArgs(TRUE)
print(args[1])
print(args[2])

mydata=read.table(paste(args[1],"_tp.csv",sep=""),header=TRUE,sep=',',colClasses="character")


#dx_str=sprintf("DX%02d",1:25 )
#poa_str=sprintf("DXEM%d",1:25 )
#colnames(mydata)=c("DISCHNO","DXA",dx_str,poa_str)

mymelt=melt(mydata,id=c("DISCHNO"))
mymelt$year=args[2]
output=mymelt[,c(4,1,2,3)]

colnames(output)=c("Year","DISCHNO","Variable","ICD-9")
output=output[order(output$DISCHNO,decreasing=FALSE),]
write.table(output,file=paste("melt_",args[1],".csv",sep=""),quote=FALSE,sep=",",col.names=TRUE,row.names=FALSE)
proc.time()


