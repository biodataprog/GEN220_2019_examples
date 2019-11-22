#!/usr/bin/bash
curl -L ftp://ftp.wormbase.org/pub/wormbase/species/c_elegans/sequence/transcripts/c_elegans.PRJNA13758.WS260.transposon_transcripts.fa.gz > transposon.fa.gz
curl -L ftp://ftp.wormbase.org/pub/wormbase/species/c_elegans/sequence/transcripts/c_elegans.PRJNA13758.WS260.mRNA_transcripts.fa.gz > mRNA.fa.gz 

gunzip *.gz
