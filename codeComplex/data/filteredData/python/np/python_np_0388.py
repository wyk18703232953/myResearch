from collections import defaultdict
import random

def main(n):
    # 1. 生成测试数据
    # 设定列数 m，可以根据需要调整或与 n 关联
    m = max(1, min(10, n))  # 示例：m 不超过 10，且至少为 1
    # 元素值范围 [1, 1e9]
    l = [[random.randint(1, 10**9) for _ in range(m)] for _ in range(n)]

    # 2. 原逻辑开始
    pm = (1 << m) - 1  # 2**m - 1

    def find(x):
        s = set()
        d = defaultdict(int)
        for i in range(n):
            a = ""
            for j in range(m):
                if l[i][j] >= x:
                    a += '1'
                else:
                    a += '0'
            val = int(a, 2)
            d[val] = i
            s.add(val)
        s = list(s)
        for i in range(len(s)):
            for j in range(i, len(s)):
                if (s[i] | s[j]) == pm:
                    # 返回 1-based 下标
                    return [d[s[i]] + 1, d[s[j]] + 1]
        return [-1, -1]

    st = 0
    end = 10**9
    ans = (0, 0)
    while st <= end:
        mid = (st + end) // 2
        s = find(mid)
        if s[0] != -1:
            ans = s
            st = mid + 1
        else:
            end = mid - 1

    print(*ans)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行调整
    main(5)