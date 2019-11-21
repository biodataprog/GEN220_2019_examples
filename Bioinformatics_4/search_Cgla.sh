#!/usr/bin/bash
#SBATCH -p short -N 1 -n 24

module load hmmer
module load db-pfam

QUERY=/bigdata/gen220/shared/data/C_glabrata_ORFs.pep
OUT=Cgla_search
hmmscan --cut_ga --cpu 24 --domtbl $OUT.domtbl $PFAM_DB/Pfam-A.hmm $QUERY > $OUT.hmmscan
