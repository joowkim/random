def get_sample_name():
    import glob
    sample_list = glob.glob("analysis/star/*.bam")
    sample_name = [i.replace("analysis/star/","").split(".Aligned")[0] for i in
                   sample_list]
    return sample_name


rule all:
    input:
        expand("analysis/preseq_complexity/{sample}.c_curve.txt",sample=get_sample_name()),
        expand("analysis/preseq_complexity/{sample}.lc_extrap.txt",sample=get_sample_name())


rule preseq_complexity:
    input:
        "analysis/star/{sample}.Aligned.sortedByCoord.out.bam",
    output:
        filtbam=temp("analysis/preseq_complexity/{sample}.filt.bam"),
        ccurve="analysis/preseq_complexity/{sample}.c_curve.txt",
        lcextrap="analysis/preseq_complexity/{sample}.lc_extrap.txt",
    envmodules:
        "bbc/preseq/preseq-3.1.2",
        "bbc/samtools/samtools-1.12",
    params:
        seg_len_max=10000000,
        preseq_min_reads=10000,
    resources:
        mem_gb=88,
    threads: 4
    shell:
        """
        # Filter for primary alignments only
        samtools view -@ {threads} -F 256 -o {output.filtbam} {input}
        # Run preseq only if there are more reads than the cutoff
        if [ `samtools view -f 64 -F 256 -c {output.filtbam}` -lt {params.preseq_min_reads} ]
        then
            touch {output.ccurve} {output.lcextrap}
        else
            preseq c_curve \
            -l {params.seg_len_max} \
            -v \
            -P \
            -bam \
            -o {output.ccurve} \
            {output.filtbam}
            echo "Finished c_curve." >&1
            echo "Finished c_curve." >&2
            preseq lc_extrap \
            -l {params.seg_len_max} \
            -v \
            -P \
            -bam \
            -o {output.lcextrap} \
            {output.filtbam}
            echo "Finished lc_extrap." >&1
            echo "Finished lc_extrap." >&2
        fi
        """
