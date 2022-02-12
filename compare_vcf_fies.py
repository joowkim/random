import os.path
from typing import List, Set
import random

COL = "CHROM\tPOS\tID\tREF\tALT\QUAL\tFILTER\tINFO\tFORMAT\tSAMPLE_NAME"


def read_vcf(vcf: str) -> List:
    assert (os.path.isfile(vcf))

    results_list: List = list()
    with open(vcf)as fin:
        for idx, line in enumerate(fin):
            # if line.startswith("##"):
            #     pass
            if not line.startswith("#"):
                tmp_list: List = line.split()
                id: str = "\t".join(tmp_list[0:7])
                if not id in results_list:
                    results_list.append(id)
                else:
                    print(f"{vcf} has a duplicated line at {idx}")
                    print(idx, id)
                    raise ValueError("duplicated line found!")
    return results_list


def compare_vcf(vcf1_list: List, vcf2_list: List):
    vcf1_set: Set = set(vcf1_list)
    vcf2_set: Set = set(vcf2_list)

    print(f"----unique variants in vcf1----")
    for i in sorted(list(vcf1_set.difference(vcf2_set))):
        print(i)
    print(f"----unique variants in vcf2----")
    for i in sorted(list(vcf2_set.difference(vcf1_set))):
        print(i)


def print_diff():
    pass


def test(vcf1: str, vcf2: str):
    vcf1_list: List = read_vcf(vcf1)
    vcf2_list: List = read_vcf(vcf2)
    compare_vcf(vcf1_list, vcf2_list)
    pass


def main():
    pass


if __name__ == '__main__':
    vcf1: str = "/Users/Jay.Kim/Workspace/GRAS_202111_04_VBCS-667/working_dir/decompress_vcf/Col-16.somatic.filtered.vep.vcf"
    vcf2: str = "/Users/Jay.Kim/Workspace/GRAS_202111_04_VBCS-667/working_dir/decompress_vcf/Col-16.hard-filtered.vep.vcf"
    test(vcf1, vcf2)
    main()
