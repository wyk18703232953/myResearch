modulo = int(1e9+7)

def generate_input(n):
    # 生成长度为 n 的字符串数组，只包含 'f' 或 's'
    # 使用简单规则：索引为偶数时为 'f'，奇数为 's'
    arr = ['f' if i % 2 == 0 else 's' for i in range(n)]
    return n, arr

def core_logic(n, arr):
    dp = [1]
    for i in range(n):
        if arr[i] == 'f':
            dp.append(0)
            continue
        for j in range(1, len(dp)):
            dp[j] = (dp[j] + dp[j-1]) % modulo
    return dp[-1]

def main(n):
    n_generated, arr = generate_input(n)
    result = core_logic(n_generated, arr)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)