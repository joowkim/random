# Install Java
Use `sdkman`
1. curl -s `"https://get.sdkman.io" | bash`
2. source `"$HOME/.sdkman/bin/sdkman-init.sh"`
3. `sdk version`
4. If it goes well, you can see `sdkman 5.15.0`
5. `sdk install java`

go to [Installation of Java from nextflow docs](https://www.nextflow.io/docs/latest/getstarted.html) or [sdkman](https://sdkman.io/install)

# Next Generation Sequencing file Formats

[great documentation by Pierre Lindenbaum
](https://www.slideshare.net/lindenb/next-generation-sequencing-file-formats-2017)

## Secondary alignment
A secondary alignment refers to a read that produces multiple alignmentsin the genome. One of these alignments will be typically referred to as the“primary” alignment.

## Supplementary alignment
A supplementary alignment (also known as a chimeric alignment) is an align-ment where the read partially matches different regions of the genome with-out overlapping the same alignment.

# Docker
docker run -v ${PWD}:/docker/ quay.io/biocontainers/fastqc:0.11.9--0 fastqc /docker/data/ggal/gut-1.fq -o /docker/fastqc-out
-v ${PWD} host machine current dir
:/docker/ docker container

# Git
git remote add origin https://github.com/<your-github-username>/your-project.git

git push -u origin main

# fastqc

well explained

https://rtsf.natsci.msu.edu/sites/_rtsf/assets/File/FastQC_TutorialAndFAQ_080717.pdf

https://hbctraining.github.io/Intro-to-rnaseq-hpc-salmon/lessons/qc_fastqc_assessment.html

https://www.sc-best-practices.org/introduction/raw_data_processing.html

# nextflow

https://carpentries-incubator.github.io/workflows-nextflow/01-getting-started-with-nextflow/index.html

# singularity
```
singularity exec --cleanenv -H $PWD  --bind $PWD:/$PWD /mnt/beegfs/kimj32/singularity/tidyverse_1.0.0.sif Rscript $PWD/star_to_mat.R $PWD/analysis/star/
```

Be aware that singularity can't follow symlinks.

`singularity run --bind analysis/sing:/data/ ~/beegfs/singularity/multiqc.sif multiqc /data/`

Your home directory (or current directory, on older versions) on the host machine is mounted in and used as the working directory inside the container. You can use the --pwd flag to override this.

See https://stackoverflow.com/questions/65642199/difference-between-working-directory-of-docker-and-singularity

# housekeeping gene list
housekeepers.txt: list of 98 housekeeping genes compiled in Tirosh et al., 2016, to be used in data preprocessing, to remove sources of unwanted variation
See https://github.com/Michorlab/tnbc_scrnaseq

# Google tricks
- Add [r] to search R programming related pages. i.e. "rotate x axis label [python]
- Use quotations `" "` to searech for the exact phrase.
- Add a tilde `~` in front of a word to find synonyms.
- Exclude terms with a minux `-` symbol.
- Search specific sites with `site:` e.g. "heatmap site:https://support.binconductor.org"
- Define a filetype by : `heatmap filetype:pdf`. It will only give you PDF files in the results. -from Dr. Ming Tang (https://www.youtube.com/watch?v=qg3FP2CCeRw)

# List of illumina adapter sequences

See https://knowledge.illumina.com/library-preparation/general-library-preparation/library-preparation-general-reference_material-list/000001314

# Specific problems for illumina libraries

https://training.galaxyproject.org/training-material/topics/sequence-analysis/tutorials/quality-control/tutorial.html

# illumina index sequence

https://github.com/faircloth-lab/illumiprocessor/blob/main/docs/usage.rst
  
# font
https://www.koddi.or.kr/ud/sub1_2



# illumina regarding lanes

Standard workflow allows for one library pool to be loaded in all lanes of the flow cell. On the other hand, the XP workflow enables the sequencing of different library pools in each lane of the Novaseq flow cells.

## How to concatenate fastq files from different lanes

https://knowledge.illumina.com/software/cloud-software/software-cloud-software-reference_material-list/000002035

# workshop materials

https://ucdavis-bioinformatics-training.github.io/

## singlecell
https://matthieuxmoreau.github.io/EarlyPallialNeurogenesis/

https://broadinstitute.github.io/2020_scWorkshop/

# useful sequencing info from UC Davies

https://dnatech.genomecenter.ucdavis.edu/faqs/

# bunch of random bioinformatics materials

learngenomics.dev

https://readiab.org/introduction.html

variancePartition

https://bioconductor.org/packages/release/bioc/html/variancePartition.html


# Galaxy singularity repo

https://depot.galaxyproject.org/singularity/