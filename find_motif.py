def find_motif(source, substr):
    pos = 0
    result = list()
    while source.find(substr, pos) != -1:
        pos = source.find(substr, pos)
        result.append(pos)
        pos += 1
    return result


def find_motif_bad_way(strg, motif):
    result = list()
    for i in range(len(strg)):
        if strg[i:len(motif) + i] == motif:
            result.append(1)
    print (sum(result))
