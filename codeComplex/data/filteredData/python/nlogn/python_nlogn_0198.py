def almost_difference(array):
    n = len(array)
    if n == 1:
        return 0
    dict_equal = dict()
    ad_sum = 0
    prev_sum = 0
    for i in range(n):
        v = array[i]
        if v not in dict_equal:
            dict_equal[v] = 0
        if v - 1 not in dict_equal:
            dict_equal[v - 1] = 0
        if v + 1 not in dict_equal:
            dict_equal[v + 1] = 0
        ad_sum = ad_sum + i * v - prev_sum + dict_equal[v + 1] - dict_equal[v - 1]
        dict_equal[v] += 1
        prev_sum += v
    return ad_sum


def main(n):
    if n <= 0:
        return 0
    # deterministic generation: array of length n
    # values grow moderately to keep them in a reasonable range
    array = [(i * 2) % (10 ** 6) for i in range(1, n + 1)]
    result = almost_difference(array)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(10)