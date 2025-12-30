import random

INF = 10**20
MOD = 10**9 + 7

def main(n: int):
    # 生成测试数据
    # 约束区间 [l, r] 和差值下限 x
    # 生成 n 个题目难度值 a[i]
    random.seed(0)
    a = [random.randint(1, 100) for _ in range(n)]
    total_sum = sum(a)
    l = random.randint(0, max(0, total_sum - 50))
    r = random.randint(l, total_sum)
    x = random.randint(0, 50)

    ans = 0
    # 遍历所有子集（非空且至少两个元素）
    for mask in range(1, 1 << n):
        # 跳过只有一个元素的子集（单比特点）
        if mask & (mask - 1) == 0:
            continue
        mn, mx, total = INF, -INF, 0
        for j in range(n):
            if (mask >> j) & 1:
                mn = min(mn, a[j])
                mx = max(mx, a[j])
                total += a[j]
        if l <= total <= r and mx - mn >= x:
            ans += 1

    print(ans)

if __name__ == "__main__":
    # 示例调用，可按需修改 n
    main(10)