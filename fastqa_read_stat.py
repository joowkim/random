import glob
import operator
import os
import statistics
import subprocess

import click


def get_fasta_stat(fa_list, path):
    os.chdir(path)
    result = dict()
    for i in fa_list:
        sample_name = os.path.basename(i).split(".")[0]
        cmd = 'grep ">" -c {}'.format(i)
        output = subprocess.check_output(cmd, shell=True)
        read_cnt = int(str(output, "utf-8").strip())
        result[sample_name] = read_cnt

    os.chdir("../")
    return sorted(result.items(), key=operator.itemgetter(1))


def get_fastq_stat(fq_list, path):
    os.chdir(path)
    result = dict()
    if "gz" in fq_list[0]:
        for i in fq_list:
            sample_name = os.path.basename(i).split(".")[0]
            cmd = "zcat {} | wc -l".format(i)
            output = subprocess.check_output(cmd, shell=True)
            read_cnt = int(str(output, "utf-8").strip())/4
            result[sample_name] = read_cnt

    else:
        for i in fq_list:
            sample_name = os.path.basename(i).split(".")[0]
            cmd = "cat {} | wc -l".format(i)
            output = subprocess.check_output(cmd, shell=True)
            read_cnt = int(str(output, "utf-8").strip())/4
            result[sample_name] = read_cnt

    os.chdir("../")
    return sorted(result.items(), key=operator.itemgetter(1))


def get_fasta_list(exten, path):
    os.chdir(path)
    fa_list = [i for i in glob.glob("*." + exten) if os.path.isfile(i)]
    os.chdir("../")
    return fa_list


def get_fastq_list(exten, path):
    os.chdir(path)
    fq_list = [i for i in glob.glob("*." + exten) if os.path.isfile(i)]
    os.chdir("../")
    return fq_list


def parse_output(sorted_list, output_file_prefix):
    '''

    :param sorted_list: result = [("samplename, read-count-numer'),,,,,]
    :return:
    '''
    with open(output_file_prefix + ".csv", 'w')as fout:
        min_val = sorted_list[0][1]
        max_val = sorted_list[-1][1]
        mean = statistics.mean([i[1] for i in sorted_list])

        for item in sorted_list:
            sample, cnt = item[0], item[1]
            string = "{},{}\n".format(sample, cnt)

            fout.write(string)
        fout.write("min,{}\n".format(min_val))
        fout.write("max,{}\n".format(max_val))
        fout.write("mean,{}\n".format(mean))


@click.command()
@click.option('-e', help="sample extension | fastq.gz, fq.gz, fq, fastq, fa, fasta, fna")
@click.option('-i', help="path")
@click.option('-o', help="output file prefix")
def main(e, i, o):
    exten = e
    path = i
    output_prefix = o
    if "fq" in exten or "fastq" in exten:
        fq_list = get_fastq_list(exten, path)
        sorted_list = get_fastq_stat(fq_list, path)
        parse_output(sorted_list, output_prefix)
    else:
        fa_list = get_fasta_list(exten, path)
        sorted_list = get_fasta_stat(fa_list, path)
        parse_output(sorted_list, output_prefix)
    print("done.")


if __name__ == '__main__':
    main()
