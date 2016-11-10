import shutil
import logging
from Bio import SeqIO
from sys import argv
from sys import exit
from collections import OrderedDict

logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s- %(message)s')


def main(fastaF):
    shutil.copy(fastaF, fastaF + ".bak")
    records = list(SeqIO.parse(fastaF, "fasta"))
    output = dict()

    for rec in records:
        output[str(rec.seq)] = rec.id

    result = sort_dict(output)

    with open(fastaF, "w")as fout:
        for i in result.keys():
            fout.write(i + "\n")
            fout.write(result[i] + "\n")
    print("done.")


def sort_dict(arg_dict):
    result = OrderedDict()
    for seq, num in zip(sorted(arg_dict.keys(), key=len)[::-1],
                        range(len(arg_dict.keys()))):
        tmp = ">contig"
        result_num = tmp + str(num + 1).zfill(5)
        result[result_num] = seq
        logging.info(result_num)
    return result


if __name__ == '__main__':
    if len(argv) != 2:
        print()
        print('''After running this file, .bak will show up,
            which is the original file.''')
        exit("python this.py fasta.file")
    main(argv[1])
