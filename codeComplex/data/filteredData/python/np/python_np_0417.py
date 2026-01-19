import sys

def build_data(n):
    if n < 1:
        n = 1
    # Interpret n as both m and number of columns
    m = n
    cols = n
    a = []
    for i in range(m):
        row = []
        for j in range(cols):
            # Deterministic pseudo-random-ish pattern, always >= 0
            v = (i * 131 + j * 197 + 7) % (10**9 + 7)
            row.append(v)
        a.append(row)
    return m, cols, a

def main(n):
    m, ncols, a = build_data(n)
    m_local = m
    n_local = ncols

    ina, mo = 0, 10**9 + 1
    pos1, pos2 = 0, 0
    mask = (1 << n_local) - 1

    def check(tang):
        key = set()
        dic = dict()
        for i in range(m_local):
            temp = 0
            for j in range(n_local):
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