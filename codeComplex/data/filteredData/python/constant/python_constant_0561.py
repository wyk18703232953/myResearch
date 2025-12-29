import random

def main(n):
    # 生成测试数据：
    # 假设 n 是总人数上界，我们在 [1, n] 范围内随机生成 n, m, k, l
    # 并确保 n 至少为 1
    if n < 1:
        n = 1

    # 为了更合理，令:
    #   total_n ∈ [1, n]
    #   m, k, l ∈ [1, n]
    total_n = random.randint(1, n)
    m = random.randint(1, n)
    k = random.randint(1, n)
    l = random.randint(1, n)

    required = k + l
    per_friend = (required + m - 1) // m
    if m * per_friend > total_n:
        print(-1)
    else:
        print(per_friend)


if __name__ == "__main__":
    # 示例调用：规模 n 可在此修改
    main(100)