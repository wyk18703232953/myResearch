import random

def main(n):
    # 生成测试数据：m 行 n 列
    # 为了有一定规模，这里令 m = max(2, n)
    m = max(2, n)
    # 数值范围可自己调整，这里设置为 0~10^9
    MAXV = 10**9
    a = [[random.randint(0, MAXV) for _ in range(n)] for _ in range(m)]

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
    # 示例：调用 main(5)
    main(5)