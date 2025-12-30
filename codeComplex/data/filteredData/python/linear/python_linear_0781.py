from collections import defaultdict as dd
import random

def main(n):
    # 1. 生成测试数据：长度为 n 的非负整数数组 A
    #   这里采用简单策略：A[i] = i 或附加一些随机扰动，保证可控
    #   为更贴近原题性质（任意多重集），使用适度随机
    random.seed(0)  # 固定种子便于复现
    A = [random.randint(0, n // 2 + 1) for _ in range(n)]

    C = dd(int)
    for a in A:
        C[a] += 1

    thedup = None
    ndup = 0
    screwed = False
    for c in C:
        if C[c] > 2:
            screwed = True
        elif C[c] == 2:
            if c == 0:
                screwed = True
            thedup = c
            ndup += 1

    if screwed or ndup > 1:
        print('cslnb')
        return

    if ndup == 1:
        if C[thedup - 1] != 0:
            print('cslnb')
            return

    n_len = len(A)
    target = sum(range(n_len))
    cur = sum(A)
    togo = cur - target

    if togo % 2 == 0:
        print('cslnb')
    else:
        print('sjfnb')


# 示例调用（提交到评测时可删除或注释）
if __name__ == "__main__":
    main(5)