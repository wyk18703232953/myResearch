from itertools import combinations
from collections import defaultdict
import random

def main(n: int):
    # 生成测试数据
    # 约束：m 不宜太大，因为程序中有 1<<m 的位运算；这里设为 min(10, n) 以保持可运行性
    m = max(2, min(10, n))     # 至少 2 列
    # 随机生成 n 行 m 列矩阵，元素范围 [1, 10^9]
    a = [[random.randint(1, 10**9) for _ in range(m)] for _ in range(n)]

    mx = max(max(row) for row in a)
    if n == 1:
        print(1, 1)
        return

    l = 0
    r = mx + 1
    while l + 1 < r:
        flg = 0
        x = (l + r) // 2
        jud = set()
        dc = defaultdict(int)

        for i in range(n):
            jnum = 0
            for j in range(m):
                if a[i][j] >= x:
                    jnum += 1 << j
            if dc[jnum] == 0:
                dc[jnum] = i + 1
            if jnum == (1 << m) - 1:
                flg = 1
                if i == 0:
                    ans = (i + 1, i + 2 if n >= 2 else 1)
                else:
                    ans = (1, i + 1)
            jud.add(jnum)

        for p, q in combinations(jud, 2):
            if p | q == (1 << m) - 1:
                flg = 1
                ans = (dc[p], dc[q])

        if flg:
            l = x
        else:
            r = x

    if l == 0:
        # 若二分答案为 0，原代码直接输出 1 2
        # 若 n == 1 已在前面返回，这里保证 n >= 2
        print(1, 2)
    else:
        print(*ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)