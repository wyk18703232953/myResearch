def main(n):
    # Interpret n as total number of records (split between cf and tc)
    # Ensure at least 1 element in each if n >= 2
    n_cf = n // 2
    n_tc = n - n_cf

    cf = {}
    tc = {}

    # Deterministic generation of cf: keys 1..n_cf, values = i * 2
    for i in range(1, n_cf + 1):
        cf[i] = i * 2

    # Deterministic generation of tc:
    # keys chosen so that there is some overlap and some new keys
    # key formula: i (overlap) and shifted indices for extra
    # We just use 1..n_tc but different values to create variety
    for i in range(1, n_tc + 1):
        tc[i] = i * 3

    sett = set(list(cf.keys()) + list(tc.keys()))
    summ = 0
    for i in sett:
        temp = 0
        try:
            temp = max(tc[i], cf[i])
        except:
            try:
                temp = cf[i]
            except:
                temp = tc[i]
        summ += temp

    print(summ)


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)