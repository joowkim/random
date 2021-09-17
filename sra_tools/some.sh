## example
GSE893-PRJNA3517
GSE848-PRJNA3353
GSE868-PRJNA3423


cat GSE_2_PRJNA.txt | cut -d "-" -f2 | xargs -n1 bash get_srr_from_prjna.sh

## get_srr_from_prjna.sh
esearch -db sra -query $1  | efetch -format runinfo | cut -d ',' -f 1 | grep SRR > $1.srr.txt

## get_runinfo_from_prjna.sh
esearch -db sra -query $1 | efetch -format runinfo > $1.runinfo.txt