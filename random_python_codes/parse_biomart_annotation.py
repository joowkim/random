from collections import OrderedDict
from namedlist import namedlist


def main(anno_file):
    Data = namedlist("Data", "Gene_stable_id refseq_ncrna hgnc_symbol description")
    results = OrderedDict()
    first = ""
    with open(anno_file, 'rt')as fin:
        first = fin.readline()
        for line in fin:
            line = line.strip("\n")
            csv_list = line.split("\t")
            ensembl_id = csv_list[0]
            ncrna = csv_list[1]
            symbol = csv_list[2]
            desc = csv_list[3]

            if ensembl_id in results:
                tmp = results[ensembl_id]
                if ncrna != "":
                    tmp.refseq_ncrna += ncrna + ";"
            else:
                results[ensembl_id] = Data(Gene_stable_id=ensembl_id, refseq_ncrna=ncrna, hgnc_symbol=symbol,
                                           description=desc)

    with open(anno_file + ".pared.tsv", 'wt')as fout:
        fout.write("HGNC symbol\tGene stable ID\tRefSeq ncRNA ID\tdescription\n")
        for i in results:
            tmp = results[i]
            tab = "\t"
            tmp.refseq_ncrna = tmp.refseq_ncrna.rstrip(";")
            wf = tmp.hgnc_symbol + tab + tmp.Gene_stable_id +tab + tmp.refseq_ncrna + tab + tmp.description + "\n"
            fout.write(wf)


if __name__ == '__main__':
    anno_f = r"E:\work\mRNA-seq\annotation\BiomaRt.GRCh37.p13.anno.gz.txt"
    main(anno_f)
