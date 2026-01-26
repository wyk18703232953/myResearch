def main(n):
    # Deterministically generate input of size n
    # Original program expects:
    # n: length of array
    # a: list of n integers
    #
    # Here we generate a[i] = (i % 5) + 1 so that values are >= 1
    a = [(i % 5) + 1 for i in range(n)]

    h = [-1] * n
    b = [(a[i], i) for i in range(n)]
    b.sort(reverse=True)

    for e in b:
        num, idx = e
        flag = True
        allNeg = True
        foundLosing = False
        foundWin = False
        for i in range(idx % num, n, num):
            if i == idx:
                continue
            if h[i] != -1:
                allNeg = False
            if h[i] == 0:
                foundLosing = True
                break
            if h[i] == 1:
                foundWin = False
        if allNeg:
            h[idx] = 0
        elif foundLosing:
            h[idx] = 1

        else:
            h[idx] = 0

    result = []
    for i in range(n):
        if h[i] == 0:
            result.append('B')

        else:
            result.append('A')
    output = "".join(result)
    # print(output)
    pass
    return output


if __name__ == "__main__":
    # Example deterministic call; change n as needed for experiments
    main(10)