from collections import OrderedDict
from collections import defaultdict


def parse_fasta(fa):
    '''
    takes a file handler. so if you want to use this function then put the with statement before this function
    :param fa:
    :return:
    '''
    name, seq = None, []
    for line in fa:
        line = line.rstrip()
        if line.startswith(">"):
            if name:
                yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name:
        yield (name, ''.join(seq))


def order_fasta_to_dict(func):
    '''
    order fasta file by sequence length
    :param fasta_dict:
    :return:
    '''

    def wrapper(*args, **kwargs):
        fasta_dict = func(*args, **kwargs)
        tmp = sorted(fasta_dict.items(), key=lambda x: len(x[1]), reverse=True)
        # [(gene_id, seq), (gene_id, seq)]

        result = OrderedDict()
        for name, seq in tmp:
            result[name] = seq
        return result

    return wrapper


@order_fasta_to_dict
def parse_fasta_to_dict(fa):
    tmp_result = defaultdict(list)
    result = dict()
    name, seq = None, []
    with open(fa)as fin:
        for line in fin:
            if line.startswith(">"):
                name = line.rstrip()
            else:
                tmp_result[name].append(line.rstrip())

    for key in tmp_result:
        seq = ''.join(tmp_result[key])
        result[key] = seq

    return result
