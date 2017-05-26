import sys
from Bio import SeqIO
import time


def check_extention(fastf):
    extention = ""
    if fastf.endswith(".fasta") or fastf.endswith(".fa") or fastf.endswith(
            ".fas") or fastf.endswith(".fna"):
        extention = "fasta"
    elif fastf.endswith(".fastq") or fastf.endswith(".fq"):
        extention = 'fastq'
    else:
        print("get me .fasta or .fastq.")
        quit()
    return extention


def assembly_stat(input_file, exten):
    infile = open(input_file, 'rU')
    seq_lgth_list = []
    contig_id_list = []
    a_count = 0
    t_count = 0
    g_count = 0
    c_count = 0

    for record in SeqIO.parse(infile, exten):
        bp = len(record.seq)
        seq_lgth_list.append(bp)
        contig_id_list.append(record.id)
        sequence = str(record.seq)
        a_count += sequence.upper().count('A')
        t_count += sequence.upper().count('T')
        g_count += sequence.upper().count('G')
        c_count += sequence.upper().count('C')

    total_length = sum(seq_lgth_list)

    A = round(100 * a_count / total_length, 1)
    T = round(100 * t_count / total_length, 1)
    G = round(100 * g_count / total_length, 1)
    C = round(100 * c_count / total_length, 1)

    print("----Nucleotide distribution----")
    print("Adenine (A)  Count: {}, Frequency: {}%".format(a_count, A))
    print("Cytosine(C)  Count: {}, Frequency: {}%".format(c_count, C))
    print("Guanine (G)  Count: {}, Frequency: {}%".format(g_count, G))
    print("Thymine (T)  Count: {}, Frequency: {}%".format(t_count, T))
    print(
        "GC ratio {}%".format(round(100 * (g_count + c_count) / total_length),
                              1))

    seq_lgth_list = sorted(seq_lgth_list)
    contig_count = len(contig_id_list)
    print()
    print("----Contig measurements----")
    print("Total contig : {}".format(contig_count))
    print("Max sequence length : {}".format(seq_lgth_list[-1]))
    print("Min sequence length : {}".format(seq_lgth_list[0]))

    n25 = 0
    n50 = 0
    n75 = 0
    acc_length = 0

    for x in seq_lgth_list:
        acc_length += x
        if acc_length >= 0.25 * total_length and n25 == 0:
            n25 = x
        if acc_length >= 0.5 * total_length and n50 == 0:
            n50 = x
        if acc_length >= 0.75 * total_length and n75 == 0:
            n75 = x

    print("Total sequence length : {} ".format(total_length))
    total_avg = round(total_length / contig_count, 1)
    print("Average sequence length : {}".format(total_avg))
    print("N25 : {}".format(n25))
    print("N50 : {}".format(n50))
    print("N75 : {}".format(n75))

    infile.close()


def main(fileN):
    extention = check_extention(fileN)
    assembly_stat(fileN, extention)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("python this.py fasta|fastq")
        sys.exit()
    start = time.time()
    main(sys.argv[1])
    print()
    print("The elapsed time is", time.time() - start, "seconds.")
