from collections import Counter
import random

def main(n):
    # 生成测试数据
    # 设定 k 的规模，这里示例设置为介于 n 和 2n 之间
    k = max(1, 2 * n)
    # 生成长度为 k 的数组 x，元素值范围 [1, n]
    x = [random.randint(1, n) for _ in range(k)]

    dd = Counter()
    for i in range(k):
        dd[x[i]] = dd[x[i]] + 1

    final = 0
    for i in range(1, k + 1):
        ans = 0
        d = dd.copy()
        for _ in range(n):
            for jj in d:
                if d[jj] >= i:
                    d[jj] -= i
                    ans += 1
                    break
        if ans >= n:
            final = i
        else:
            break

    print(final)


if __name__ == "__main__":
    # 示例：调用 main，n 为规模参数
    main(10)