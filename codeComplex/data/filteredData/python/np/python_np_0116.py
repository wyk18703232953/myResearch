import random

def main(n: int):
    # 生成规模为 n 的测试数据（原来是 m 和 m 个整数）
    m = n
    test_values = [random.randint(0, 10**9) for _ in range(m)]

    values = []
    idx = []

    for i in range(m):
        x = test_values[i]
        ans = 0
        for xx, ii in zip(values, idx):
            if (xx ^ x) < x:
                x ^= xx
                ans ^= ii
        if x == 0:
            anss = []
            tmp = ans
            for j in range(i):
                if (tmp & 1) != 0:
                    anss.append(j)
                tmp >>= 1
            print(len(anss), *anss)
        else:
            print(0)
            values.append(x)
            idx.append(ans ^ (1 << i))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)