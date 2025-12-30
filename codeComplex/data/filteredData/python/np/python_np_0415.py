import random

def main(n):
    # 规模 n 为列数，构造行数 m 和矩阵 a
    # 这里示例：行数 m = max(2, n)；数值范围 [0, 10^9]
    m = max(2, n)
    random.seed(0)  # 如需每次不同数据，可去掉这一行
    a = [
        [random.randint(0, 10**9) for _ in range(n)]
        for _ in range(m)
    ]

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
                    temp |= (1 << j)

            if temp in key:
                continue
            key.add(temp)

            tempk = temp
            # 遍历 temp 的所有子集，使用标准子集遍历方式
            while True:
                dic[tempk] = i
                if tempk == 0:
                    break
                tempk = (tempk - 1) & temp

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
    # 示例调用：n 可按需修改
    main(5)