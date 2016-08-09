def get_all_k_mer(seq):
    '''
    get all k_mer candidate from sequence.
    :param seq:
    :return:
    '''
    result = list()

    for k_length in range(1, len(seq)):
        for index in range(len(seq) - k_length + 1):
            result.append(seq[index : index + k_length])

    return result