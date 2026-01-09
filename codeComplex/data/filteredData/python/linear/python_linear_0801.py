def main(n):
    # Deterministic data generation
    # Interpret n as m (length of arr); choose fixed k
    m = max(1, n)
    k = 5
    # Generate arr as increasing integers starting from 1 with step 1
    arr = [i + 1 for i in range(m)]

    modulo = 0
    tmp = 0
    op = 1
    cur = (arr[0] - 1) // k
    for i in range(m):
        if (arr[i] - 1 - modulo) // k != cur:
            modulo += tmp
            cur = (arr[i] - 1 - modulo) // k
            tmp = 0
            op += 1
        tmp += 1
    # print(op)
    pass
if __name__ == "__main__":
    main(10)