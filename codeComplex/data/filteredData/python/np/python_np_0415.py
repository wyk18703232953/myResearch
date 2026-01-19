def main(n):
    # Interpret n as both matrix dimensions: m = n rows, k = n columns
    # Generate a deterministic m x k matrix a[i][j] = (i + 1) * (j + 1)
    m = n
    k = n
    a = [[(i + 1) * (j + 1) for j in range(k)] for i in range(m)]

    ina, mo = 0, 10 ** 9 + 1
    pos1, pos2 = 0, 0
    mask = (1 << k) - 1

    def check(tang):
        key = set()
        dic = dict()
        for i in range(m):
            temp = 0
            for j in range(k):
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