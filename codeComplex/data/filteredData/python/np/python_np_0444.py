import random
from collections import defaultdict as dd

mod = int(1e9) + 7

def cal(x, n, m, A):
    l1 = set()
    d = dd(int)
    a = []
    for i in range(n):
        k = 0
        for j in range(m):
            if A[i][j] >= x:
                k += 1 << j
        l1.add(k)
        d[k] = i + 1
    l1 = list(l1)
    s = (1 << m) - 1
    for i in l1:
        for j in l1:
            if i | j == s:
                a = [d[i], d[j]]
    return a

def main(n):
    # 生成规模为 n 的测试数据：
    # 固定列数 m，元素为 [0, 1e9] 的随机整数
    m = 5
    A = [[random.randint(0, 10**9) for _ in range(m)] for _ in range(n)]

    l, r = 0, 10**9
    last_ok_mid = -1
    while l <= r:
        mid = (l + r) // 2
        if cal(mid, n, m, A):
            last_ok_mid = mid
            l = mid + 1
        else:
            r = mid - 1

    if last_ok_mid != -1:
        a = cal(last_ok_mid, n, m, A)
        print(a[0], a[1])
    else:
        # 如果完全没有可行解，按原逻辑退一格尝试
        a = cal(0, n, m, A)
        if a:
            print(a[0], a[1])
        else:
            # 实在找不到就输出占位
            print(-1, -1)

if __name__ == "__main__":
    # 示例调用：规模 n 可自行修改
    main(10)