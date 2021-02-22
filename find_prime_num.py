def find_prime_num(ary):
    result = list()
    for i in ary:
        if helper(i):
            result.append(i)
    return result


def helper(i):
    for j in range(2,i):
        if i % j == 0:
            print(i,j)
            return False
    return i
