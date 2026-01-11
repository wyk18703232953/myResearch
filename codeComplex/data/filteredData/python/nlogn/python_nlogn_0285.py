def main(n):
    import string
    from heapq import heappop , heappush
    from bisect import *
    from collections import deque , Counter , defaultdict
    from math import *
    from itertools import permutations , accumulate

    dx = [-1 , 1 , 0 , 0]
    dy = [0 , 0 , 1 , -1]

    # 数据规模设计：
    # 原程序有两组输入：第一组 n 行，第二组 m 行
    # 这里令第一组大小为 n，第二组大小为 n // 2（可按需调整）
    n1 = max(1, n)
    m1 = max(1, n // 2)

    d = {}
    sm = 0

    # 构造第一组数据：
    # indx: 从 0 开始递增
    # y: 简单的确定性函数 (i % 10)
    for i in range(n1):
        indx = i
        y = i % 10
        d[indx] = [1, [y]]

    # 构造第二组数据：
    # 为了触发“已存在键”和“新键”两种情况：
    # - 前一半落在已有索引范围内
    # - 后一半落在新的索引上
    for i in range(m1):
        if i < n1:
            indx = i  # 与第一组重复

        else:
            indx = n1 + (i - n1)  # 新索引
        y = (i * 3) % 7
        if indx in d:
            d[indx][0] += 1
            d[indx][1].append(y)

        else:
            d[indx] = [1, [y]]

    for i in d:
        if d[i][0] == 1:
            sm += d[i][1][0]

        else:
            sm += max(d[i][1])

    # print(sm)
    pass
if __name__ == "__main__":
    main(10)