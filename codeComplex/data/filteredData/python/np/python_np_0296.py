MOD = 10**9 + 7
MAXV = 10**5 + 5  # 上界保持与原程序一致，用于预计算

def Calculate_Mobius(limit):
    arr = [1] * (limit + 1)
    prime_count = [0] * (limit + 1)
    mobius_value = [0] * (limit + 1)

    for i in range(2, limit + 1):
        if prime_count[i] == 0:
            for j in range(i, limit + 1, i):
                prime_count[j] += 1
                arr[j] *= i

    for i in range(1, limit + 1):
        if arr[i] == i:
            mobius_value[i] = 1 if (prime_count[i] & 1) == 0 else -1
        else:
            mobius_value[i] = 0

    return mobius_value

# 预计算 2 的幂
def precompute_powers(limit):
    p2 = [0] * (limit + 1)
    p2[0] = 1
    for i in range(1, limit + 1):
        p2[i] = (p2[i - 1] * 2) % MOD
    return p2

MOBIUS = Calculate_Mobius(MAXV)
P2 = precompute_powers(MAXV)

def main(n):
    """
    n: 输入规模，即数组 b 的长度。
    这里根据 n 生成测试数据 b，元素范围为 [1, MAXV-1]。
    """
    import random

    # 生成测试数据：均匀随机在 [1, MAXV-1] 内
    b = [random.randint(1, MAXV - 1) for _ in range(n)]

    freq = [0] * MAXV
    for x in b:
        freq[x] += 1

    ans = 0
    for i in range(1, MAXV):
        cnt = 0
        for j in range(i, MAXV, i):
            cnt += freq[j]
        if cnt == 0:
            continue
        total_subsequences = (P2[cnt] - 1) % MOD
        ans = (ans + MOBIUS[i] * total_subsequences) % MOD

    ans = (ans + MOD) % MOD
    print(ans)

# 示例调用
if __name__ == "__main__":
    main(10)  # 可修改 n 测试不同规模