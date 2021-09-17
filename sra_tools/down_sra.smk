##reference https://stackoverflow.com/questions/44561183/multiple-inputs-and-outputs-in-a-single-rule-snakemake-file
import os

SRA_ID = dict()

with open("all.sra.txt")as fin:
    for line in fin:
        #SRA_ID.append(line.strip())
        SRA_ID[line.strip()] = line.strip()


def chainfile2link(wildcards):
    return SRA_ID[wildcards.sra_id]


rule all:
    input:
        expand("sra/{sra_id}_1.fastq.gz",sra_id=SRA_ID.keys())

rule down_sra:
    output:
        os.path.join("sra","{sra_id}_1.fastq.gz")
    envmodules:
        "bbc/sratoolkit/sratoolkit-2.11.0",
    params:
        link=chainfile2link
    threads: 4
    resources:
        nodes=1,
        mem_gb=8,
    shell:
        """
        fastq-dump --split-3 --gzip {params.link}  --outdir "sra"
        """
