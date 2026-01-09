def main(n):
    from collections import Counter
    import math
    from fractions import Fraction

    def makedict(var):
        return dict(Counter(var))

    # 构造确定性的输入数据
    # n: 问题规模，同时作为数组长度
    size = max(1, n)

    # indices 构造：保证有一定的上升关系，但不是严格单调
    # 例如：indices[i] = (i * 2) % (size // 2 + 1) + i // 3
    indices = [(i * 2) % (size // 2 + 1) + i // 3 for i in range(size)]

    # cost 构造：简单线性递增再取模，保证正数
    # 例如：cost[i] = (i * 3 + 5) % (2 * size + 1) + 1
    cost = [(i * 3 + 5) % (2 * size + 1) + 1 for i in range(size)]

    # 原核心算法逻辑
    testcases = 1
    for _ in range(testcases):
        ans = float('inf')
        mint = []
        for i in range(size):
            ans = float('inf')
            total = cost[i]
            flag = 0
            for j in range(i):
                if indices[i] > indices[j]:
                    ans = min(ans, cost[j])
                    flag = 1
            if flag != 0:
                total += ans
                ans = float('inf')
                flag = 0
                for k in range(i + 1, size):
                    if indices[k] > indices[i]:
                        ans = min(ans, cost[k])
                        flag = 1
                if flag != 0:
                    total += ans
                    mint.append(total)

                else:
                    continue

            else:
                continue
        if len(mint) > 0:
            # print(min(mint))
            pass

        else:
            # print(-1)
            pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 以做时间复杂度实验
    main(10)