import os
import sys


def get_path(path):
    results_dict = dict()
    sample_name = ""
    print("Sample\tmapping.rate\tmapped.reads")
    for (pat, dirs, files) in os.walk(path):
        for filename in files:
            if not "_STARpass1" in pat:
                if "Log.final.out" == filename:
                    sample_name = pat.replace(r"./", "")
                    results = helper_parse_log(os.path.join(pat, filename))
                    results_dict[sample_name] = "{}\t{}".format(round(results[1], 0), results[0])
                    # print(sample_name, round(results[1], 0), results[0])
    return results_dict


def helper_parse_log(log_file):
    input_reads = None
    result = list()
    with open(log_file)as fin:
        for i in fin:
            line = i.strip()
            if "unmapped" in line:
                tmp = line.split()
                num = tmp[-1].split("%")[0]
                num = float(num)
                result.append(num)
            if "Number of input reads" in line:
                tmp = line.split()
                input_reads = int(tmp[-1])

        return (100 - sum(result), input_reads * (100 - sum(result)))


def show_results(dic):
    for key in sorted(dic.keys()):
        print("{}\t{}".format(key, dic[key]))


def main(path):
    results = get_path(path)
    show_results(results)
    print()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("python this.py 01.Align")
        quit()
    main(sys.argv[1])
