import random

def main(n):
    # 1. 生成测试数据（有序数组 Ar 和 U）
    # 生成递增数组 Ar
    Ar = []
    cur = 0
    for _ in range(n):
        cur += random.randint(1, 10)
        Ar.append(cur)
    # 生成 U 为一个正整数，范围大致在数组跨度内
    U = random.randint(1, max(1, Ar[-1] - Ar[0]))

    # 2. 原逻辑
    R = 0
    ans = -1.0
    for i in range(n):
        while R + 1 < n and Ar[R + 1] - Ar[i] <= U:
            R += 1
        if i + 1 < R:
            val = (Ar[R] - Ar[i + 1]) / (Ar[R] - Ar[i])
            if val > ans:
                ans = val

    print(ans)


if __name__ == "__main__":
    # 示例调用：可修改 n 测试不同规模
    main(10)