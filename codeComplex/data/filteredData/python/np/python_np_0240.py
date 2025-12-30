import random

def main(n):
    # 生成测试数据
    # 随机生成区间 [l, r] 和难度差阈值 x
    # 难度值 A[i] 在 [1, 1000] 范围内
    A = [random.randint(1, 1000) for _ in range(n)]
    l = random.randint(1, max(1, sum(A) // 4))
    r = random.randint(l, max(l, sum(A)))
    x = random.randint(0, max(A) - min(A) if n > 1 else 0)

    count = 0
    for i in range(1 << n):
        total = 0
        mn = 10**9
        mx = -10**9
        for k in range(n):
            if i & (1 << k):
                total += A[k]
                if A[k] < mn:
                    mn = A[k]
                if A[k] > mx:
                    mx = A[k]
        if total >= l and total <= r and mx - mn >= x:
            count += 1

    print(count)

if __name__ == "__main__":
    # 示例：n=5
    main(5)