# coding: utf-8
import sys
from heapq import heappush, heappop, heapify
sys.setrecursionlimit(int(1e7))

def main(n):
    # 生成规模为 n 的测试数据
    # 这里示例生成从 0 到 n-1 的整数序列，可根据需要调整数据生成逻辑
    a = list(range(n))

    # 原始逻辑
    a = [-x - 1 if x >= 0 else x for x in a]
    if n % 2 == 1:
        _, i = min((x, i) for i, x in enumerate(a))
        a[i] = -a[i] - 1

    print(*a)

if __name__ == "__main__":
    # 示例：调用 main(5)，实际使用时可修改为任意 n
    main(5)