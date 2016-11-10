from Bio import SeqIO
import random
import sys


def check_extention(fastf):
    extension = ""
    if fastf.endswith(".fasta") or fastf.endswith(".fa") or fastf.endswith(
            ".fas") or fastf.endswith(".fna"):
        extension = "fasta"
    elif fastf.endswith(".fastq"):
        extension = 'fastq'
    else:
        print()
        "get me .fasta or .fastq."
        sys.exit()
    return extension


def get_reads_file(fastf, num, exten):
    records = list(SeqIO.parse(fastf, exten))
    if len(records) <= num:
        print()
        "fasta/q has less contigs than your number."
        sys.exit()
    reads_list = sorted(random.sample(range(len(records)), num))

    seq_record_list = (records[rec] for rec in range(len(records)) if
                       rec in reads_list)

    with open(fastf + "_sub", "w")as fout:
        SeqIO.write(seq_record_list, fout, exten)


def main(fastf, num):
    exten = check_extention(fastf)
    get_reads_file(fastf, num, exten)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print()
        sys.exit("python this.py fasta|q random_read")
    main(sys.argv[1], int(sys.argv[2]))
