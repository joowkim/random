import random


def generate_random_seq(num):
    return ''.join([random.choice('ACGT') for _ in range(10)])


def generate_subreads_genome(genome, num_reads, read_len):
    result = list()

    if len(genome) > read_len:

        for _ in range(num_reads):
            start = random.randint(0, len(genome) - read_len) + 1
            if len(genome[start: start + read_len]) >= read_len:
                result.append(genome[start: start + read_len])
    return result
