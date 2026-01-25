from collections import Counter
from math import *
import sys

mod = 1000000007

def pro(arr, q):
    n = len(arr)
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                ans += 1

    res = ans % 2
    for x, y in q:
        k = y - x + 1
        k = k // 2
        k = k % 2
        res = k ^ res
        if res:
            print('odd')
        else:
            print('even')

def main(n):
    if n <= 0:
        return
    # 定义数组规模和查询数量，确保都随 n 线性增长
    size_arr = n
    t = n

    # 确定性生成数组：一个简单的非单调序列，便于产生逆序对
    arr = [((i * 17) % (size_arr + 3)) for i in range(size_arr)]

    # 确定性生成查询：在 1..size_arr 的范围内生成 [l, r] 区间
    # 使用简单算术保证覆盖不同长度和位置
    que = []
    for i in range(t):
        l = (i * 7) % size_arr + 1
        r = (i * 13 + 5) % size_arr + 1
        if l > r:
            l, r = r, l
        que.append([l, r])

    pro(arr, que)

if __name__ == "__main__":
    main(10)