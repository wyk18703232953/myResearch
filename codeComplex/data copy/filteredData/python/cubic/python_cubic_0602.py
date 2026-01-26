def min_sub_array(day, k):
    if not day:
        return [0] * (k + 1)
    n = len(day)
    best = [float('inf')] * (n + 1)
    best[0] = 0
    best[1] = 1
    for size in range(2, n + 1):
        for i in range(n + 1 - size):
            best[size] = min(best[size], day[i + size - 1] - day[i] + 1)
    output = [0] * (k + 1)
    for i in range(k + 1):
        if n - i > 0:
            output[i] = best[n - i]
    return output


def main(n):
    # 映射规则：
    # n >= 1
    # N = max(1, n // 3)       -> 测试用例个数
    # M = max(1, n)            -> 每行字符串长度
    # K = min(M, max(0, n // 4)) -> 允许的 K 上界
    if n < 1:
        n = 1

    N = max(1, n // 3)
    M = max(1, n)
    K = min(M, max(0, n // 4))

    # 生成 N 行确定性 01 字符串，长度为 M
    # 规则：第 t 行中，第 i 位为 '1' 当且仅当 (i + t) % d == 0
    # 其中 d = max(1, n // 5)
    d = max(1, n // 5)
    best = None

    for t in range(N):
        s = ''.join('1' if (i + t) % d == 0 else '0' for i in range(M))
        day = [i for i, val in enumerate(s) if val == '1']
        day_best = min_sub_array(day, K)
        if best is None:
            best = day_best

        else:
            new_best = [float('inf')] * (K + 1)
            for i in range(K + 1):
                for j in range(i + 1):
                    new_best[i] = min(new_best[i], day_best[j] + best[i - j])
            best = new_best

    # print(best[K])
    pass
if __name__ == "__main__":
    main(10)