library("tidyverse")

args<-commandArgs(TRUE)

blast_file <- args[1]

## sanity check
stopifnot(file.exists(blast_file))

## output file path
output_path <- args[2]

#blast_colname <- c("query_id", "sub_acc", "percnt_iden", "length", "mismatch", "gapopen", "qstart",
#                                            "qend", "sstart", "send", "evalue", "bitscore")

blast_colname <- c("query_id", "sub_acc", "percnt_iden", "length", "mismatch", "gapopen", "qstart", "qend", "sstart", "send", "evalue", "bitscore", "qcovs", "qcov_hsp_perc", "qlen", "slen")

blast_df <- read_tsv(blast_file, col_names = blast_colname)

blast_filt_df <- blast_df %>% filter(evalue <= 0.000001 & qcov_hsp_perc >= 80 & percnt_iden >= 80) %>% 
                        group_by(query_id) %>%
                        #arrange(desc(evalue), qcovs, bitscore, percnt_iden) %>%
                        arrange(evalue, desc(qcov_hsp_perc), desc(bitscore), desc(percnt_iden)) %>%
                        filter(row_number() ==1 )

write_tsv(blast_filt_df, output_path)
