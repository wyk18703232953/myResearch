import random

def main(n: int):
    # 生成测试数据：
    # c：长度为 n 的正整数数组
    # a：长度为 n 的排列，表示每个点指向的下一个点（1-based）
    c = [random.randint(1, 10**9) for _ in range(n)]
    perm = list(range(1, n + 1))
    random.shuffle(perm)
    a = perm[:]  # a 为 1..n 的随机排列

    u = [0] * len(a)
    ans = 0

    for i in range(len(a)):
        if u[i] != 0:
            continue
        idx = i
        while u[idx] == 0:
            u[idx] = 1
            idx = a[idx] - 1

        if u[idx] == 2:
            idx = i
            while u[idx] == 1:
                u[idx] = 2
                idx = a[idx] - 1
            continue

        start = idx
        mn = c[idx]
        u[idx] = 2
        while a[idx] - 1 != start:
            idx = a[idx] - 1
            mn = min(mn, c[idx])
            u[idx] = 2

        idx = i
        while u[idx] == 1:
            u[idx] = 2
            idx = a[idx] - 1
        ans += mn

    print(ans)


if __name__ == "__main__":
    # 示例：n = 10
    main(10)