def find_motif(source, substr):
    pos = 0
    result = list()
    while source.find(substr, pos) != -1:
        pos = source.find(substr, pos)
        result.append(pos)
        pos += 1
    return result
