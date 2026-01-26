def f(d, n):
    res = 0
    prev = None
    ans = [0] * (n + 1)
    for i in sorted(d.keys()):
        if prev is None:
            prev = i

        else:
            ans[res] += i - prev
            prev = i
        res += d[i]
    return ans[1:]


def main(n):
    from collections import defaultdict
    d = defaultdict(int)
    # 生成 n 个区间 [x, y]，完全确定性
    # 示例：x = i, y = i + (i % 5)
    for i in range(1, n + 1):
        x = i
        y = i + (i % 5)
        d[x] += 1
        d[y + 1] -= 1
    result = f(d, n)
    # print(*result)
    pass
if __name__ == "__main__":
    main(10)