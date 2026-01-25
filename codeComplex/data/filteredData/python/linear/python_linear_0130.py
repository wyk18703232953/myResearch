N = 1030
MOD = int(1e9 + 7)

# 预计算组合数
c = [[0] * N for _ in range(N)]
for i in range(N):
    c[i][0] = 1
for i in range(1, N):
    for j in range(1, N):
        c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % MOD

# 预计算 dp
dp = [0] * N
for i in range(2, N):
    dp[i] = dp[bin(i).count('1')] + 1


def main(n: int):
    # 将 n 映射为输入规模：
    # - 二进制数组长度为 len(arr) = min(max(n,1), N-1)
    # - cnt = (n % 11)，并限定在 [0,20] 范围，以避免超过 dp、使用有代表性的值
    if n <= 0:
        arr_len = 1
    else:
        arr_len = n
    if arr_len >= N:
        arr_len = N - 1

    # 确定性生成二进制数组 arr，长度为 arr_len
    # 使用简单算术：arr[i] = ((i * 137) // 17) % 2
    arr = [((i * 137) // 17) % 2 for i in range(arr_len)]

    # 确定性生成 cnt，限制在非负小范围
    cnt = n % 21

    if cnt == 0:
        print(1)
        return

    res = 0
    for i in range(1, N):
        if dp[i] != cnt - 1:
            continue
        cur_n, k = len(arr) - 1, i
        for pos in range(len(arr)):
            if arr[pos] == 1:
                res = (res + c[cur_n][k]) % MOD
                k -= 1
            cur_n -= 1
        if cur_n == -1 and k == 0:
            res += 1
    if cnt == 1:
        res -= 1
    print(res % MOD)


if __name__ == "__main__":
    # 示例调用，可按需修改 n 进行实验
    main(10)