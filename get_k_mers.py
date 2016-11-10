from collections import Counter


def get_all_k_mer(seq):
    '''
    get all k_mer candidate from sequence.
    :param seq:
    :return:
    '''
    result = list()

    for k_length in range(1, len(seq)):
        for index in range(len(seq) - k_length + 1):
            result.append(seq[index: index + k_length])

    return result


def get_k_mer(seq, k_lgth):
    result = list()

    for i in range(len(seq) - k_lgth + 1):
        result.append(seq[i: i + k_lgth])

    return result


def get_most_common_k_mer(seq, k_lgth):
    '''
    :param seq_list: k-mer list
    :return:
    '''
    seq_list = get_k_mer(seq, k_lgth)
    cnt = Counter(seq_list)
    tmp_cnt = cnt.most_common
    most_common = tmp_cnt(1)[0][1]

    if most_common <= 0:
        print("the frequent item is None...")
        raise ValueError

    result = [x[0] for x in tmp_cnt() if x[1] == most_common]

    return result, most_common


string = "ACGTTGCATGTCGCATGATGCATGAGAGCT"

print(get_k_mer(string, 4))
