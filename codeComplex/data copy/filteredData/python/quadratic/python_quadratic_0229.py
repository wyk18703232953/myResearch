import math

def generate_input(n):
    # 确保规模至少为 3，才能让原算法有意义
    if n < 3:
        n = 3
    # 生成严格递增的 s，避免退化成无解
    s = list(range(1, n + 1))
    # 生成确定性的 ce：简单的算术序列
    ce = [(i * 7 + 3) % 1000 + 1 for i in range(n)]
    return n, s, ce

def core_algorithm(n, s, ce):
    best = 10 ** 9
    for j in range(1, n - 1):
        a = ce[j]
        b = 10 ** 9
        c = 10 ** 9
        for i in range(j - 1, -1, -1):
            if s[i] < s[j]:
                b = min(b, ce[i])
        for k in range(j + 1, n):
            if s[k] > s[j]:
                c = min(c, ce[k])
        best = min(best, a + b + c)

    if best >= 10 ** 9:
        return -1

    else:
        return best

def main(n):
    n, s, ce = generate_input(n)
    result = core_algorithm(n, s, ce)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)