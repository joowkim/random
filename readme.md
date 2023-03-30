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


# nextflow

https://carpentries-incubator.github.io/workflows-nextflow/01-getting-started-with-nextflow/index.html

# singularity
```
singularity exec --cleanenv -H $PWD  --bind $PWD:/$PWD /mnt/beegfs/kimj32/singularity/tidyverse_1.0.0.sif Rscript $PWD/star_to_mat.R $PWD/analysis/star/
```

# housekeeping gene list
housekeepers.txt: list of 98 housekeeping genes compiled in Tirosh et al., 2016, to be used in data preprocessing, to remove sources of unwanted variation
See https://github.com/Michorlab/tnbc_scrnaseq