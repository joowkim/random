configfile: "config.yaml"

def get_sample_name():
    import glob
    sample_list = glob.glob("trimmed/*.gz")
    sample_name = [ i.replace("trimmed/", "").split("_")[0] for i in sample_list ]
    return sample_name

rule all:
    input:
        expand('sortmerna/{sample}', sample = get_sample_name())


rule subsample:
    input:
        fq1 = "trimmed/{sample}_L000_R1_001_trimmed.fq.gz",
        fq2 = "trimmed/{sample}_L000_R2_001_trimmed.fq.gz",
    output:
        fq1 = "subsamples/{sample}.subsample.R1.fq.gz",
	    fq2 = "subsamples/{sample}.subsample.R2.fq.gz",
    threads: 4
    params:
        num_of_subsample = 100000
    resources:
        nodes = 1,
        mem_gb = 4,
    envmodules:
        "bbc/seqtk/seqtk-1.3-r115-dirty",
    log:
        stdout = "logs/subsample/{sample}.o",
        stderr = "logs/subsample/{sample}.e",
    shell:
        """
        seqtk sample -s 100 {input.fq1} {params.num_of_subsample} | gzip -c > {output.fq1}
        seqtk sample -s 100 {input.fq2} {params.num_of_subsample} | gzip -c > {output.fq2}
        """


rule sortmerna_PE:
    input:
        fq1 = "subsamples/{sample}.subsample.R1.fq.gz",
        fq2 = "subsamples/{sample}.subsample.R2.fq.gz",
    output:
        directory("sortmerna/{sample}"),
    log:
        stderr = "logs/sortmerna/{sample}.e",
        stdout = "logs/sortmerna/{sample}.o",
    envmodules:
        "bbc/sortmerna/sortmerna-4.3.4",
    params:
        rfam5_8s = config["sortmerna"]["rfam5_8s"],
        rfam5s = config['sortmerna']['rfam5s'],
        silva_arc_16s = config['sortmerna']['silva_arc_16s'],
        silva_arc_23s = config['sortmerna']['silva_arc_23s'],
        silva_bac_16s = config['sortmerna']['silva_bac_16s'],
        silva_bac_23s = config['sortmerna']['silva_bac_23s'],
        silva_euk_18s = config['sortmerna']['silva_euk_18s'],
        silva_euk_28s = config['sortmerna']['silva_euk_28s'],
        idx_dir = config['sortmerna']['idx_dir'],
        output_dir = "sortmerna/{sample}",
    threads: 8
    resources:
        nodes = 1,
        mem_gb = 16,
    shell:
        """
        sortmerna --threads {threads} -reads {input.fq1} -reads {input.fq2} --workdir {params.output_dir}  \
        --idx-dir {params.idx_dir}  \
        --ref {params.rfam5s}  \
        --ref {params.rfam5_8s}  \
        --ref {params.silva_arc_16s}  \
        --ref {params.silva_arc_23s}  \
        --ref {params.silva_bac_16s}  \
        --ref {params.silva_bac_23s}  \
        --ref {params.silva_euk_18s}  \
        --ref {params.silva_euk_28s}
        """
