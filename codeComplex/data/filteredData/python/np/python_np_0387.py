MAX = 10**9  # O((n*m+(2**m)**2)*log(MAX))

def solve(arrs, m):
    def convertToBinary(arr, minB):
        b = 0
        for i in range(m):
            if arr[i] >= minB:
                b |= (1 << i)
        return b

    def checkPossible(minB):
        binRepresentations = set()
        for arr in arrs:
            binRepresentations.add(convertToBinary(arr, minB))
        binList = list(binRepresentations)
        ii = jj = -1
        n_local = len(binList)
        for i in range(n_local):
            for j in range(i, n_local):
                if binList[i] | binList[j] == (1 << m) - 1:
                    ii = binList[i]
                    jj = binList[j]
        if ii != -1:
            ansi = ansj = -1
            for i in range(len(arrs)):
                b = convertToBinary(arrs[i], minB)
                if b == ii:
                    ansi = i
                if b == jj:
                    ansj = i
            return (ansi, ansj)
        else:
            return None

    minB = -1
    i = j = -1
    b = MAX
    while b > 0:
        temp = checkPossible(minB + b)
        if temp is None:
            b //= 2
        else:
            minB += b
            i, j = temp
    i += 1
    j += 1
    return i, j


def main(n):
    # Deterministic input generation based on n
    # We interpret n as both number of rows and columns: n = number of arrays = length of each array
    # To keep the original algorithm meaningful, require n >= 1
    if n <= 0:
        n = 1
    m = n
    arrs = []
    for i in range(n):
        # Deterministic construction: arr[i][j] = (i + 1) * (j + 2)
        row = [ (i + 1) * (j + 2) for j in range(m) ]
        arrs.append(row)

    i, j = solve(arrs, m)
    print(f"{i} {j}")


if __name__ == "__main__":
    # Example deterministic call; adjust n to change input scale
    main(5)