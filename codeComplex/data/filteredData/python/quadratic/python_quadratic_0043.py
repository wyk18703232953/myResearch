modulo = int(1e9 + 7)

def main(n: int) -> int:
    # 1. 生成测试数据：长度为 n 的字符串数组，仅包含 'f' 或 'x'
    #    这里简单生成前 n//2 个为 'f'，后面为 'x'，你可以按需要修改生成逻辑。
    arr = ['f' if i < n // 2 else 'x' for i in range(n)]

    # 2. 原逻辑：根据 arr 计算 dp
    dp = [1]
    for i in range(n):
        if arr[i] == 'f':
            dp.append(0)
            continue
        for j in range(1, len(dp)):
            dp[j] = (dp[j] + dp[j - 1]) % modulo

    # 3. 返回结果而不是 print，方便在外部调用或测试
    return dp[-1]

if __name__ == "__main__":
    # 示例：调用 main(5)，实际使用时可自行修改 n
    print(main(5))