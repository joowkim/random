import glob
import os

import click


def parse_bed(bed):
    result = dict()
    with open(bed, 'rt')as fin:
        for line in fin:
            line = line.strip()
            tmp = line.split('\t')
            ensembl_id = tmp[3]
            gene_name = tmp[-1]
            result[ensembl_id] = gene_name
    return result


def get_rsem_results_files(path):
    return [i for i in glob.glob("*.genes.results") if os.path.isfile(i)]


def write_files(bed_dict, rsem_files):
    for rsem in rsem_files:
        rsem_out_file = rsem.replace("genes", "genes.add_geneid")
        with open(rsem, 'rt')as fin, open(rsem_out_file, 'wt')as fout:
            first_line = 'gene_symbol\t' + fin.readline()
            fout.write(first_line)
            for line in fin:
                tmp = line.split('\t')
                ensembl_id = tmp[0]
                if ensembl_id in bed_dict:
                    line = bed_dict[ensembl_id] + '\t' + line
                    fout.write(line)
        print("{} is done.".format(rsem))


@click.command()
@click.option('-b', help="bed file path")
@click.option('-i', help="rsem.genes.results files path")
def main(i, b):
    path = i
    bed = b
    bed_dict = parse_bed(bed)
    rsem_files = get_rsem_results_files(path)
    write_files(bed_dict, rsem_files)


if __name__ == '__main__':
    main()
