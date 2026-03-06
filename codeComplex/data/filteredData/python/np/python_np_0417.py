def main(n):
    # Interpret n as number of columns, set rows = n for scalability
    m = n
    # Deterministically generate matrix a of size m x n
    # Example pattern: a[i][j] = (i * 37 + j * 17) % 1000000007
    a = [[(i * 37 + j * 17) % 1000000007 for j in range(n)] for i in range(m)]

    ina, mo = 0, 10**9 + 1
    pos1, pos2 = 0, 0
    mask = (1 << n) - 1

    def check(tang):
        key = set()
        dic = dict()
        for i in range(m):
            temp = 0
            for j in range(n):
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
    print(pos1 + 1, pos2 + 1)


if __name__ == "__main__":
    main(5)