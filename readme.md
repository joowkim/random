# Install Java
Use `sdkman`
1. curl -s `"https://get.sdkman.io" | bash`
2. source `"$HOME/.sdkman/bin/sdkman-init.sh"`
3. `sdk version`
4. If it goes well, you can see `sdkman 5.15.0`
5. `sdk install java`

go to [Installation of Java from nextflow docs](https://www.nextflow.io/docs/latest/getstarted.html) or [sdkman](https://sdkman.io/install)

# Secondary alignment
A secondary alignment refers to a read that produces multiple alignmentsin the genome. One of these alignments will be typically referred to as the“primary” alignment.

# Supplementary alignment
A supplementary alignment (also known as a chimeric alignment) is an align-ment where the read partially matches different regions of the genome with-out overlapping the same alignment.

# Docker
docker run -v ${PWD}:/docker/ quay.io/biocontainers/fastqc:0.11.9--0 fastqc /docker/data/ggal/gut-1.fq -o /docker/fastqc-out
-v ${PWD} host machine current dir
:/docker/ docker container


----
Locus (pl. loci):  A fixed position on a chromosome that may be occupied by one or more genes. 
Allele: One of a number of alternative forms of the same gene occupying a given locus on a chromosome.
Genotype: The DNA sequence  of the genetic makeup of an organism which determines a specific phenotype of that organism


Allele: a basic unit to describe a variant form of a given gene
genotype: genetic material of an organismallele: a basic unit to describe a variation from a given gene
