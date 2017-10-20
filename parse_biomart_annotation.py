from collections import OrderedDict
from namedlist import namedlist


def main(anno_file):
    Data = namedlist("Data", "gene_id symbol desc refseq_mrna refseq_ncrna")
    results = OrderedDict()
    first = ""
    with open(anno_file, 'rt')as fin:
        first = fin.readline()
        for line in fin:
            line = line.strip("\n")
            csv_list = line.split("\t")
            ensembl_id = csv_list[0]
            desc = csv_list[1]
            symbol = csv_list[4]
            mrna = csv_list[2]
            ncrna = csv_list[3]  # tmp[3] hgnc_symbol == gene_name

            if ensembl_id in results:
                tmp = results[ensembl_id]
                if mrna != "":
                    tmp.refseq_mrna +=  mrna + ";"
                if ncrna != "":
                    tmp.refseq_ncrna += ncrna + ";"
            else:
                results[ensembl_id] = Data(gene_id=ensembl_id, symbol=symbol, desc=desc, refseq_mrna=mrna,
                                           refseq_ncrna=ncrna)

    with open(anno_file + ".pared.tsv", 'wt')as fout:
        fout.write("Gene stable ID\tGene name\tdescription\tRefSeq mRNA ID\tRefSeq ncRNA ID\n")
        for i in results:
            tmp = results[i]
            tab = "\t"
            tmp.refseq_mrna = tmp.refseq_mrna.rstrip(";")
            tmp.refseq_ncrna = tmp.refseq_ncrna.rstrip(";")
            wf = tmp.gene_id + tab + tmp.symbol + tab + tmp.desc + tab + tmp.refseq_mrna + tab + tmp.refseq_ncrna + "\n"
            fout.write(wf)


if __name__ == '__main__':
    anno_f = r"D:\mRNAseq\mart_export_GRCh37.tsv"
    main(anno_f)
