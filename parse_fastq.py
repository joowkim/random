import sys


def parse_fastaq(fq):
    '''
        takes file handler. so if you want to use this function then put with open something before this function
        :param fp:
        :return:
    '''
    name, seq, strand, qual = None, None, None, None
    for line in fq:
        line = line.rstrip()
        if line.startswith("@"):
            name = line
            seq = fq.readline().rstrip()
            strand = fq.readline().rstrip()
            qual = fq.readline().rstrip()
            yield (name, seq, strand, qual)
        else:
            print('the header line does not start with @!.')
            sys.exit("abort!")