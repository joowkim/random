### ATAC

https://yiweiniu.github.io/blog/2019/03/ATAC-seq-data-analysis-from-FASTQ-to-peaks/

https://tobiasrausch.com/courses/atac/

### xargs

`ls *R1.fastq.gz | cut -d '.' -f 1 | xargs -I {} echo "{}"`


### scRNAseq

| Cell Type                    | Marker                       |
| ---------------------------- | ---------------------------- |
| CD14+ monocytes              | CD14, LYZ                    |
| FCGR3A+ monocytes            | FCGR3A, MS4A7                |
| Conventional dendritic cells | FCER1A, CST3                 |
| Plasmacytoid dendritic cells | IL3RA, GZMB, SERPINF1, ITM2C |
| B cells                      | CD79A, MS4A1                 |
| T cells                      | CD3D                         |
| CD4+ T cells                 | CD3D, IL7R, CCR7             |
| CD8+ T cells                 | CD3D, CD8A                   |
| NK cells                     | GNLY, NKG7                   |
| Megakaryocytes               | PPBP                         |
| Erythrocytes                 | HBB, HBA2                    |
