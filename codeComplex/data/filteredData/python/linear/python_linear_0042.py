import random

def main(n):
    # 生成测试数据
    # 随机设定 k：1 到 min(10, n) 之间
    k = random.randint(1, min(10, n)) if n > 0 else 0
    # 生成数组 A，元素值范围 [1, 100000]
    A = [random.randint(1, 100000) for _ in range(n)]

    C = [0] * 100001

    l = 0
    r = 0
    p = 0

    while r < n and p < k:
        C[A[r]] += 1
        if C[A[r]] == 1:
            p += 1
        r += 1

    if p != k:
        print('-1', '-1')
    else:
        while p == k:
            C[A[l]] -= 1
            if C[A[l]] == 0:
                p -= 1
            l += 1

        l -= 1
        print(l + 1, r)

if __name__ == "__main__":
    # 示例：n = 10
    main(10)