# Align reads to a reference genome

## Create index

```bwa index -p <genome_prefix> <reference.fasta>```

## Alignment

### Read Group Identifiers

Read group identifiers are used to identify sequence data by sequencing technology (e.g. Illumina), flow cell, lane, sample ID, and library. Using these identifiers ensures that batch effects, or biases in the data that might have been introduced at different stages of the sequencing process can be properly accounted for. Detailed documentation on Read Groups can be found on the GATK website.

The most common and recommended read groups are:

- ID : Read Group Identifier
    A unique identifier for each read group. The convention for Illumina data is ```{FLOWCELL}.{LANE}```.

- PU: Platform Unit
    A sample/library specific identifier, specified with: ```{FLOWCELL_BARCODE}.{LANE}.{SAMPLE}```. The flowcell barcode is a unique identifier for a flow cell, lane is the lane of that flowcell, and sample is the sample or library specific identifier.

- SM: Sample
    The name of the sample represented by this read group. This will be the name used in the sample column of the VCF file.

- PL: Platform
    The sequencing technology used to create the data. Current valid values: ILLUMINA, SOLID, LS454, HELICOS, and PACBIO.

- LB: Data Preparation Library Identifier
    The library preparation identifier. This is used by MarkDuplicates to identify which read groups contain molecular (e.g. PCR) duplicates.

The read group information can be found in the file header (look for @RG) and the RG:Z tag for each sequence record. This information is not automatically added to Fastq files following sequencing, but needs to be added either when mapping with BWA or separately after mapping with Picard's AddOrReplaceReadGroups tool.


For most resequencing data, we want to use the bwa mem algorithm (for 70bp to 1Mbp query sequences) to map our reads. A typical command would be:

```bwa mem -M -t 1 -R '@RG\tID:{FLOWCELL}.{LANE}\tPU:{FLOWCELL_BARCODE}.{LANE}.{SAMPLE}\tSM:{SAMPLE}\tPL:{PLATFORM}\tLB{LIBRARY}' <genome_prefix> <reads_1.fq> <reads_2.fq> > | samtools sort -O BAM -@ 4 -o $bam ```

Argument 	Description

 - -M 	Mark shorter split hits as secondary - mandatory for Picard compatibility
 
 - -R <str> 	Read group information (see above for description)

 - -p 	Specifies that fastq read 1 and read 2 files are interleaved, if only one fastq is specified and this command is not used, will assume single-end data


 [reference - harvard informatics tutorial](https://informatics.fas.harvard.edu/whole-genome-resquencing-for-population-genomics-fastq-to-vcf.html#reads)