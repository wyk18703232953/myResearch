import random

modulo = int(1e9 + 7)

def main(n: int) -> int:
    # 根据 n 生成测试数据：长度为 n 的数组，元素随机为 'f' 或 's'
    arr = [random.choice(['f', 's']) for _ in range(n)]

    dp = [1]
    for i in range(n):
        if arr[i] == 'f':
            dp.append(0)
            continue
        for j in range(1, len(dp)):
            dp[j] = (dp[j] + dp[j - 1]) % modulo
    return dp[-1]


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    result = main(5)
    print(result)