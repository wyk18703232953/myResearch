import random

def main(n, seed=0):
    random.seed(seed)

    # 生成测试数据：随机选择 m，并生成长度为 n 的数组 a
    if n <= 0:
        return

    # 随机选择 1 <= m <= n，避免 m=0
    m = random.randint(1, max(1, n))
    # 原程序中 a 是一行 n 个整数，这里随机生成
    # 为了更可控，生成 0~10^9 内的数
    a = [random.randint(0, 10**9) for _ in range(n)]

    # ----------------- 原逻辑开始（去掉 input） -----------------
    rem = [[] for _ in range(m)]
    req = n // m
    ans = 0  # 原代码中未使用，但保留

    for i in range(n):
        rem[a[i] % m].append([a[i], i])

    ind = m - 1
    for i in range(m):
        size = len(rem[i])
        if size > req:
            ind = i
        if size < req:
            ok = False
            for j in range(ind, -1, -1):
                while len(rem[j]) > req:
                    pop, _ = rem[j].pop()
                    rem[i].append([pop + (i - j) % m, _])
                    if len(rem[i]) == req:
                        ok = True
                        break
                if ok:
                    break
                ind -= 1
            else:
                ind = m - 1
                for j in range(ind, -1, -1):
                    while len(rem[j]) > req:
                        pop, _ = rem[j].pop()
                        rem[i].append([pop + (i - j) % m, _])
                        if len(rem[i]) == req:
                            ok = True
                            break
                    if ok:
                        break
                    ind -= 1

    out = [0] * n
    for bucket in rem:
        for val, idx in bucket:
            out[idx] = val

    # 输出与原程序一致
    print(sum(out) - sum(a))
    print(' '.join(map(str, out)))


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)