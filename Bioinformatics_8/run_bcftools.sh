#!/usr/bin/bash
#SBATCH -p batch -N 1 -n 4 --mem 16gb
module unload perl
module load samtools
module load bcftools
GENOME=S_enterica_CT18.fasta

# need to make a string which is all the bam files you want to process
# but if we do *.bam it will catch the intermediate bam files that are in the folder
for a in $(cat acc.txt)
do
m="$a.bam $m"
done

VCF=Salmonella.vcf.gz
FILTERED=Salmonella.filtered.vcf.gz
LOWQUAL="FAIL"
bcftools mpileup -Ou -f $GENOME $m | bcftools call --ploidy 1 -vmO z -o $VCF
tabix -p vcf $VCF
bcftools stats -v -F $GENOME -s - $VCF > $VCF.stats
mkdir -p plots
plot-vcfstats -p plots/ $VCF.stats
bcftools filter -O z -o $FILTERED -s $LOWQUAL -i'%QUAL>10' $VCF
