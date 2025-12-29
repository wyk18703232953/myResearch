import random

def main(n):
    # 随机生成参数 n, m, k，使得 1 <= m <= n
    N = n
    M = random.randint(1, N)
    K = random.randint(1, max(1, N // 10))

    # 生成严格递增的 p 数组，长度为 M，元素范围在 [1, N]
    # 简单方式：从 1..N 中选 M 个不同的数并排序
    p = sorted(random.sample(range(1, N + 1), M))

    # 原逻辑开始
    i = 0
    ct = 0
    ops = 0
    while i < len(p):
        nm = p[i] - ct
        if nm % K == 0:
            mnm = nm
        else:
            mnm = (nm // K) * K + K
        si = i
        while p[i] - ct <= mnm:
            i += 1
            if i >= len(p):
                break
        ct += i - si
        ops += 1
        if i >= len(p):
            break

    print(ops)


if __name__ == "__main__":
    # 示例：规模 n 可在此处调整
    main(10**5)