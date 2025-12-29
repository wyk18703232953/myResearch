from operator import xor
from random import randint

def main(n):
    # 生成测试数据：
    # 第一行：长度为 n 的数组（值在 0~10 之间）
    # 第二行：查询个数 m
    # 接下来 m 行：区间 [l, r]，1 <= l <= r <= n
    a = [[randint(0, 10) for _ in range(n)]]
    m = max(1, n)  # 至少 1 个查询
    queries = []
    for _ in range(m):
        l = randint(1, n)
        r = randint(l, n)
        queries.append((l, r))

    # 原逻辑：预处理 a 的各层（异或）
    for i in range(1, n):
        a.append(list(map(xor, a[-1][:-1], a[-1][1:])))

    # 原逻辑：转为每层上从下层向上取区间最大值
    for i in range(n - 1):
        a[i + 1] = list(map(max, a[i][:-1], a[i][1:], a[i + 1]))

    out = []
    for l, r in queries:
        out.append(a[r - l][l - 1])

    # 输出结果（每行一个答案）
    print("\n".join(map(str, out)))


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)