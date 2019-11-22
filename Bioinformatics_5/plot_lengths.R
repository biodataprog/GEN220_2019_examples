transposons = read.csv("transposon.tab",sep="\t",header=TRUE)
summary(transposons)
mRNAs = read.csv("mRNA.tab",sep="\t",header=TRUE)
summary(mRNAs)
hist(transposons$Length,100,main="Histogram of TE lengths")
hist(log(mRNAs$Length),100,main="Histogram of mRNA lengths")
boxplot(mRNAs$Length)
boxplot(transposons$Length)

short = subset(mRNAs,mRNAs$Length < 10000)
summary(short)
boxplot(short$Length)

