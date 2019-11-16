#!/usr/bin/bash
#SBATCH -p short -N 1 -n 8
module load kallisto
mkdir -p output
if [ ! -f Scer.idx ]; then
 kallisto index -i Scer.idx S_cerevisiae.fasta
fi

cat samples.tsv | while read ACC COND REP
do
 OUT=output/$COND.$REP
 kallisto quant -t 8 --single -l 300 -s 20 -i Scer.idx -o $OUT data/${ACC}_1.fastq.gz
# if paired end
# kallisto quant -t 8 -i Scer.idx -o $OUT data/${ACC}_1.fastq.gz data/${ACC}_2.fastq.gz
done 
