#!/usr/bin/bash
#SBATCH -p short -N 1 -n 4

module load hmmer
module load db-pfam

QUERY=query_SOD1.fa
OUT=SOD1_search.hmmscan
hmmscan --cut_ga --cpu 4 --domtbl SOD1_search.domtbl $PFAM_DB/Pfam-A.hmm $QUERY > SOD1_search.hmmscan
