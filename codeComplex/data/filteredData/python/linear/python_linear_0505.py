from collections import defaultdict
import random

def main(n: int):
    # 1. 生成测试数据：构造 1..n 的一个随机排列
    # 原代码中 l 是 1-based，下标 0 位置填充 0
    perm = list(range(1, n + 1))
    random.shuffle(perm)
    l = [0] + perm

    ans = ['A', 'B']
    x = defaultdict(int)
    table = [-1] * (n + 1)

    # 计算每个值在 l 中的位置：x[value] = index
    for i in range(1, n + 1):
        x[l[i]] = i

    table[x[n]] = 1
    for i in range(n - 1, 0, -1):
        if (x[i] - i > 0):
            for j in range(x[i], 0, -i):
                if (l[j] > i):
                    if (table[j] == 1):
                        table[x[i]] = 0
                        break
        if (n - i > 0 and table[x[i]] == -1):
            for j in range(x[i], n + 1, i):
                if (l[j] > i):
                    if (table[j] == 1):
                        table[x[i]] = 0
                        break

        if (table[x[i]] == -1):
            table[x[i]] = 1

    # 输出结果（与原程序行为一致：一行，不带换行）
    for v in table[1:]:
        print(ans[v], end='')


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)