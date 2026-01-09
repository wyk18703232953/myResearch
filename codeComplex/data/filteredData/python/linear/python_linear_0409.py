def find_min_weight(n, k, stages):
    n = len(stages)
    min_weight = float('inf')

    def backtrack(s, w, t):
        nonlocal min_weight 

        if t >= k:
            min_weight = min(min_weight, w)
            return

        if s >= n - 1:
            return

        for i in range(s + 1, n, 1):
            if stages[i] - stages[s] > 1:
                backtrack(i, w + stages[i], t + 1)

    backtrack(0, stages[0], 1)

    if min_weight == float('inf'):
        return -1

    return min_weight


def main(n):
    # 将 n 映射为问题规模：
    # - 字符串长度 = n
    # - k 与 n 相关，确保有一定搜索空间
    if n <= 0:
        return

    # 构造确定性字符串（仅小写字母），长度为 n
    # 周期性使用 'a' 到 'z'
    s_chars = [chr(ord('a') + (i % 26)) for i in range(n)]
    s = "".join(s_chars)

    # 原代码：stages = list(set(map(cint, insr())))
    # cint: a->1, b->2, ...
    stages = list(set(ord(c) - 96 for c in s))
    stages.sort()

    # 定义 k：与去重后阶段数量相关，但不超过一定规模
    m = len(stages)
    if m == 0:
        return
    k = max(1, min(m, n // 3 if n >= 3 else 1))

    result = find_min_weight(m, k, stages)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)