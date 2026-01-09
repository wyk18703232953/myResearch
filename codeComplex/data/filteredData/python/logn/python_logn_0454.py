def main(n):
    import math

    # Deterministic generation of test cases based on n
    # We create n test cases (t = n)
    # For each i in [1..n]:
    #   n_i  ranges between 1 and 100 (or higher if desired), here capped deterministically
    #   k_i  is constructed from n_i in a deterministic manner
    t = n
    res = []
    for i in range(1, t + 1):
        ni = (i % 100) + 1  # ni in [1, 100]
        ki = (i * i) % (4 * ni + 10) + 1  # ki in [1, 4*ni+10], deterministic

        limit = -1
        if ni <= 60:
            limit = 0
            pow4 = 1
            for _ in range(ni):
                limit += pow4
                pow4 *= 4
        if (limit < ki and limit != -1) or (ni == 2 and ki == 3):
            res.append('NO')

        else:
            div = 1
            ki -= 1
            size = 1
            while div < ni and ki >= 4 * size - 1:
                ki -= 4 * size - 1
                size *= 2
                div += 1
            res.append('YES ' + str(ni - div))

    # print('\n'.join(res))
    pass
if __name__ == "__main__":
    # Example: run with input scale n = 10
    main(10)