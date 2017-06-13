import glob
import os

import click


def get_file_list(input_dir, exten, sample_type):
    f1 = sample_type
    r2 = ""
    forward = ""
    reverse = ""
    if f1 == "R1":
        r2 = "R2"
        forward = r'*{}*.*{}'.format(f1, exten)
        reverse = r'*{}*.*{}'.format(r2, exten)
    elif f1 == "1":
        r2 = "2"
        forward = r'*_{}.*{}'.format(f1, exten)
        reverse = r'*_{}.*{}'.format(r2, exten)
    else:
        print(exten, " is either R1 or 1.")
        quit()

    forward_list = sorted([i for i in glob.glob(os.path.join(input_dir, forward)) if os.path.isfile(i)])
    reverse_list = sorted([i for i in glob.glob(os.path.join(input_dir, reverse)) if os.path.isfile(i)])

    if len(forward_list) != len(reverse_list):
        print("forward fq, reverse fq are different.")
        print(forward_list, reverse_list)
        quit()

    for f, r in zip(forward_list, reverse_list):
        t1 = f.split("_")[0]
        t2 = r.split("_")[0]
        if t1 != t2:
            print("forward fq, reverse fq are different.")
            print(f, "->", t1, r, "->", t2)
            quit()
    return forward_list, reverse_list


def run_trimmomatic(f_list, r_list, threads, lgth, output_dir, qual):
    for f, r in zip(f_list, r_list):
        fname = os.path.basename(f).split(".")[0]
        rname = os.path.basename(r).split(".")[0]
        cmd = 'trimmomatic PE -threads {thread} {for_fq} {rev_fq} {output}/{for_name}.p.fastq.gz unpaired/{for_name}.up.fastq.gz {output}/{rev_name}.p.fastq.gz unpaired/{rev_name}.up.fastq.gz LEADING:3 TRAILING:3 SLIDINGWINDOW:4:{q} MINLEN:{l} AVGQUAL:{q} > trim.log'.format(
            thread=threads,
            for_fq=f,
            for_name=fname,
            rev_fq=r,
            rev_name=rname,
            l=lgth,
            output=output_dir,
            q=qual,
        )
        print(cmd)
        os.system(cmd)


@click.command()
@click.option('-e', help="sample extension either fastq or gz")
@click.option('-s', help="sample type. either R1 or 1.")
@click.option('-t', type=int, help="threads.")
@click.option('-l', type=int, help="length-cutoff.")
@click.option('-o', help="output dir.", default="paired")
@click.option('-q', type=int, help="quality score.", default=25)
@click.option('-i', help="input dir.")
def main(e, t, s, l, o, q, i):
    input_dir = i
    output_dir = o
    exten = e
    threads = t
    lgth = l
    qual = q
    sample_type = s
    up = r'unpaired'

    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    if not os.path.isdir(up):
        os.makedirs(up)
    f_list, r_list = get_file_list(input_dir, exten, sample_type)
    run_trimmomatic(f_list, r_list, threads, lgth, output_dir, qual)


if __name__ == '__main__':
    main()
