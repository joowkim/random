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
