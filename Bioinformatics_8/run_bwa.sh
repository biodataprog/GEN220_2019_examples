#!/usr/bin/bash
#SBATCH -p short -N 1 -n 8 --mem 8gb

module load bwa
module load samtools
CPU=16
mkdir -p fastq
ln -s /bigdata/gen220/shared/data/S_enterica/*.fastq.gz fastq
ln -s /bigdata/gen220/shared/data/S_enterica/S_enterica_CT18.fasta
ln -s /bigdata/gen220/shared/data/S_enterica/acc.txt
GENOME=S_enterica_CT18.fasta
if [ ! -f $GENOME.sa ]; then
   bwa index $GENOME
fi
for acc in $(cat acc.txt)
do
	FWDREAD=fastq/${acc}_1.fastq.gz
	REVREAD=fastq/${acc}_2.fastq.gz

	bwa mem -t $CPU $GENOME $FWDREAD $REVREAD > ${acc}.sam
	samtools fixmate -O bam ${acc}.sam ${acc}_fixmate.bam
	samtools sort --threads $CPU -O BAM -o ${acc}.bam ${acc}_fixmate.bam
	samtools index ${acc}.bam
done
