def main(n):
    # Deterministically construct m, n, and matrix a based on input scale n
    # Here we choose number of rows m = n, number of columns cols = max(1, n % 10 + 1)
    m = n
    cols = max(1, n % 10 + 1)

    a = []
    for i in range(m):
        row = []
        for j in range(cols):
            # Deterministic value construction using i and j
            val = (i * 31 + j * 17 + (i ^ j)) % (10**9 + 7)
            row.append(val)
        a.append(row)

    ina, mo = 0, 10**9 + 1
    pos1, pos2 = 0, 0
    mask = (1 << cols) - 1

    def check(tang):
        key = set()
        dic = dict()
        for i in range(m):
            temp = 0
            for j in range(cols):
                if a[i][j] >= tang:
                    temp += (1 << j)
            if temp in key:
                continue
            key.add(temp)
            tempk = temp
            while tempk >= 0:
                tempk &= temp
                dic[tempk] = i
                tempk -= 1

            tocheck = mask ^ temp
            if tocheck in dic:
                return dic[tocheck], i, True
        return -1, -1, False

    while ina < mo - 1:
        tang = (ina + mo) // 2
        temppos1, temppos2, status = check(tang)
        if status:
            pos1, pos2 = temppos1, temppos2
            ina = tang
        else:
            mo = tang

    # For complexity experiments we can return the result instead of printing
    return pos1 + 1, pos2 + 1


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    result = main(1000)
    print(result)