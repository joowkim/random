import os
import glob
from typing import NamedTuple

import click


class Data(NamedTuple):
    sample_name: str
    reads: int
    bp: int
    q30: float
    mean_q: float


def get_file_list(input_dir, exten, sample_type):
    r1 = sample_type
    r2 = ""
    forward = ""
    reverse = ""
    if r1 == "R1":
        r2 = "R2"
        forward = r'*{}*.*{}'.format(r1, exten)
        reverse = r'*{}*.*{}'.format(r2, exten)
    elif r1 == "1":
        r2 = "2"
        forward = r'*_{}.*{}'.format(r1, exten)
        reverse = r'*_{}.*{}'.format(r2, exten)
    else:
        raise NameError(exten, " is either R1 or 1.")

    forward_list = sorted([i for i in glob.glob(os.path.join(input_dir, forward)) if os.path.isfile(i)])
    reverse_list = sorted([i for i in glob.glob(os.path.join(input_dir, reverse)) if os.path.isfile(i)])

    if len(forward_list) != len(reverse_list):
        print("forward fq, reverse fq are different.")
        print(forward_list, reverse_list)
        raise ValueError()

    for f, r in zip(forward_list, reverse_list):
        t1 = f.split("_")[0]
        t2 = r.split("_")[0]
        if t1 != t2:
            print("forward fq, reverse fq are different.")
            print(f, "->", t1, r, "->", t2)
            raise ValueError()
    return forward_list, reverse_list


def run_seqtk(f_list, r_list):
    if not os.path.isdir("out_seqtk"):
        os.makedirs("out_seqtk")

    for f, r in zip(f_list, r_list):
        r1 = f.split("_S")[0]
        cmd = "seqtk fqchk -q30 {} > {}".format(f, os.path.join("out_seqtk", r1 + ".R1.out"))
        os.system(cmd)

        r2 = f.split("_S")[0]
        cmd = "seqtk fqchk -q30 {} > {}".format(r, os.path.join("out_seqtk", r2 + ".R2.out"))
        os.system(cmd)


def parse_seqtk(seqtk_out_dir):
    result = list()

    if not os.path.isdir(seqtk_out_dir):
        print(seqtk_out_dir, "is not found.")
        raise NameError()

    os.chdir(seqtk_out_dir)

    f_list = sorted([i for i in glob.glob("*.R1.out") if os.path.isfile(i)])
    r_list = sorted([i for i in glob.glob("*.R2.out") if os.path.isfile(i)])

    for f, r in zip(f_list, r_list):
        sample = f.split(".")[0]
        reads = 0
        bp1 = 0
        bp2 = 0
        r1_q30 = 0
        r1_mean_q = 0

        r2_q30 = 0
        r2_mean_q = 0

        q30 = 0
        mean_q = 0

        with open(f, 'rt')as fin:
            fin.readline()
            fin.readline()
            parse1 = fin.readline().split()
            parse2 = fin.readline().split()

            bp1 = float(parse1[1])
            reads = float(parse2[1])

            r1_q30 = float(parse1[-1])
            r1_mean_q = float(parse1[7])

        with open(r, 'rt')as fin:
            fin.readline()
            fin.readline()
            parse1 = fin.readline().split()

            bp2 = float(parse1[1])

            r2_q30 = float(parse1[-1])
            r2_mean_q = float(parse1[7])

        q30 = round((r1_q30 + r2_q30) / 2, 1)
        mean_q = round((r1_mean_q + r2_mean_q) / 2, 1)
        bp = bp1 + bp2

        result.append(Data(sample_name=sample, reads=reads, bp=bp, q30=q30, mean_q=mean_q))
    return result


def show_result(out_list):
    print("sample_name,RawReads,ReadLength,Yield,Q30,MeanScore")
    for i in out_list:
        print("{},{},,{},{},{}".format(i.sample_name, i.reads, i.bp, i.q30, i.mean_q))


@click.command()
@click.option('-e', help="sample extension either fastq or gz")
@click.option('-s', help="sample type. either R1 or 1.")
@click.option('-i', help="input dir.")
def main(e, s, i):
    exten = e
    sample_type = s
    input_dir = i
    f_list, r_list = get_file_list(input_dir, exten, sample_type)
    run_seqtk(f_list, r_list)
    result = parse_seqtk("out_seqtk")
    show_result(result)


if __name__ == '__main__':
    main()
