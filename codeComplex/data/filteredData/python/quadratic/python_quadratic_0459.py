def main(n):
    # Deterministically generate input array 'a' of length n
    # Example pattern: positive integers with some repetition and variation
    if n <= 0:
        return
    a = [i % 7 + 1 for i in range(n)]

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
    # For time-complexity experiments, it's usually enough to build the string
    # The print here is kept to preserve observable behavior
    # print(''.join(result))
    pass
if __name__ == "__main__":
    main(10)