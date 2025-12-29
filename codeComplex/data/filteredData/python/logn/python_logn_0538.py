import random

def main(n):
    # 生成测试数据：随机生成一个 1 到 n 之间的 k
    # 按原题逻辑，k 表示在无限数字串 "123456789101112..." 中的第 k 位
    if n <= 0:
        return
    k = random.randint(1, n)

    digit = 1
    low = 1
    high = 9
    totalDigit = 9
    lastTotalDigit = 0

    # 查找 k 所在的位数段
    while totalDigit < k:
        low *= 10
        high = 10 * low - 1
        digit += 1
        lastTotalDigit = totalDigit
        totalDigit += (high + 1 - low) * digit

    # 调整 k 为在当前位数段中的偏移
    k -= lastTotalDigit
    cur = str(low + (k - 1) // digit)
    print(cur[(k - 1) % digit])

# 示例调用
if __name__ == "__main__":
    main(100000)