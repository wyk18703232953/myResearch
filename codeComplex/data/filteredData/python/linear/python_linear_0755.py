import sys
from heapq import heappush, heappop, heapify
sys.setrecursionlimit(int(1e7))

def transform_array(a):
    n = len(a)
    a = [-x - 1 if x >= 0 else x for x in a]
    if n % 2 == 1:
        _, i = min((x, i) for i, x in enumerate(a))
        a[i] = -a[i] - 1
    return a

def main(n):
    # 生成确定性的长度为 n 的数组
    # 既包含非负数也包含负数，便于保留原逻辑特性
    a = [i // 2 if i % 3 == 0 else -i for i in range(n)]
    res = transform_array(a)
    # print(*res)
    pass
if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)