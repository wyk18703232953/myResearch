import random

def main(n):
    # 生成测试数据
    # k 为窗口大小，1 <= k <= n
    k = random.randint(1, n)
    # theorems 为长度为 n 的正整数数组
    theorems = [random.randint(1, 10) for _ in range(n)]
    # sleep 为长度为 n 的 0/1 数组
    sleep = [random.randint(0, 1) for _ in range(n)]

    # 原始逻辑
    tsum = []
    ts = 0
    sleepsum = []
    slsum = 0

    for i in range(n):
        ts += theorems[i]
        tsum.append(ts)
        if sleep[i] == 1:
            slsum += theorems[i]
        sleepsum.append(slsum)

    maxdiff = tsum[k - 1] - sleepsum[k - 1]
    for i in range(1, n - k + 1):
        diff = (tsum[i + k - 1] - tsum[i - 1]) - (sleepsum[i + k - 1] - sleepsum[i - 1])
        maxdiff = max(maxdiff, diff)

    print(slsum + maxdiff)


if __name__ == "__main__":
    # 示例：规模 n=10
    main(10)