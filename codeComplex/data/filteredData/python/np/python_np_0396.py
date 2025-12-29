from collections import defaultdict as dd
import random

def main(n):
    # 1. 生成测试数据
    #    这里假设 m 与 n 同级别，可根据需要调整生成规则
    m = max(1, n // 2)
    # 随机生成矩阵 l1，元素在 [0, 10^9] 之间
    l1 = [[random.randint(0, 10**9) for _ in range(m)] for _ in range(n)]

    # 2. 原始逻辑开始
    l = 0
    h = 10 ** 9
    c = (1 << m) - 1
    x, y = 1, 2

    while l <= h:
        mid = (l + h) // 2
        d = dd(int)
        d1 = dd(int)
        for i in range(n):
            bits = []
            for j in range(m):
                if l1[i][j] >= mid:
                    bits.append('1')
                else:
                    bits.append('0')
            s = int(''.join(bits), 2)
            d[s] += 1
            d1[s] = i + 1

        f = 0
        for i_key in d:
            for j_key in d:
                if (i_key | j_key) == c:
                    f = 1
                    x = d1[i_key]
                    y = d1[j_key]
                    break
            if f:
                break

        if f:
            if l == h:
                break
            l = mid + 1
        else:
            if l == h:
                break
            h = mid

    print(x, y)


if __name__ == "__main__":
    # 示例：运行 main，规模 n 自行设定
    main(5)