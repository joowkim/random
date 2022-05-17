configfile: "bin/config.yaml"


def get_sample_name():
    import glob
    sample_list = glob.glob("analysis/star/*.bam")
    sample_name = [i.replace("analysis/star/","").split(".Aligned")[0] for i in
                   sample_list]
    return sample_name


rule all:
    input:
        expand("analysis/qualimap/{sample}/done",sample=get_sample_name())


rule qualimap:
    """
    Run qualimap on bam files.
    """
    input:
        bam = "analysis/star/{sample}.Aligned.sortedByCoord.out.bam",
    output:
        touch("analysis/qualimap/{sample}/done")
    log:
        stdout="logs/qualimap/{sample}.o",
        stderr="logs/qualimap/{sample}.e"
    benchmark:
        "benchmarks/qualimap/{sample}.txt"
    envmodules:
        "bbc/qualimap/qualimap_v.2.2.2"
    params:
        gtf = config["ref"]["annotation"],
    resources:
        mem_gb=100,
    threads: 8,
    shell:
        """
        qualimap rnaseq -bam {input} \
        -gtf {params.gtf} --paired \
        --sequencing-protocol strand-specific-reverse \
        -outdir analysis/qualimap/{wildcards.sample} \
        --java-mem-size={resources.mem_gb}G
        """
