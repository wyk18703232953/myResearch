from bisect import bisect_right
import random

MOD = 10**9 + 7

def main(n):
    # 参数化生成测试数据：
    # 生成 n 个区间 [s[i], e[i]]，保证 s[i] < e[i]
    # 同时生成 x, y 为正整数
    random.seed(0)
    x = random.randint(1, 10**4)
    y = random.randint(1, 10**4)

    s = [0] * n
    e = [0] * n
    v = [0] * n

    # 生成区间，范围可根据需要调整
    for i in range(n):
        start = random.randint(0, 10**5)
        end = random.randint(start + 1, start + 10**5)
        s[i] = start
        e[i] = end

    c = 0
    for i in range(n):
        c += x + (e[i] - s[i]) * y

    s.sort()
    e.sort()

    for i in range(n - 2, -1, -1):
        k = bisect_right(s, e[i])
        while (k < n) and (v[k] == 1) and (s[k] - e[i]) * y < x:
            k += 1
        if k == n:
            continue
        if (s[k] - e[i]) * y < x:
            v[k] = 1
            c += (s[k] - e[i]) * y - x

    print(c % MOD)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)