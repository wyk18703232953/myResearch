from itertools import accumulate
import random

def Binary_Search(arr, n, x):
    l, r = 0, n - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid + 1
        elif arr[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    return r + 1

def main(n):
    # 生成测试数据
    # a 为正整数数组，长度 n
    a = [random.randint(1, 10) for _ in range(n)]
    # q 为查询次数，这里设为 n，可按需要调整策略
    q = n
    # b 为每次攻击数值
    b = [random.randint(1, 10) for _ in range(q)]

    ps = list(accumulate(a))
    res = []
    sm = 0
    for i in range(q):
        sm += b[i]
        if sm >= ps[-1]:
            res.append(n)
            sm = 0
        else:
            z = Binary_Search(ps, n, sm)
            res.append(n - z)
    for i in res:
        print(i)

if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)