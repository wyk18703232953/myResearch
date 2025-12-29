def main(n):
    # 预处理：构造累积位数数组 sum[i]，表示从 1 到 10^i - 1 的数字总位数
    sum_digits = [0 for _ in range(12)]
    i = 0
    # 直到位数总和超过 10^12（足够大），原逻辑保持不变
    while sum_digits[i] < 10 ** 12 and i + 1 < len(sum_digits):
        i += 1
        sum_digits[i] = sum_digits[i - 1] + i * (10 ** i - 10 ** (i - 1))

    # 将 n 作为原代码中的 k 使用
    k = n

    # 找到所在区间 i，使得 sum_digits[i-1] < k <= sum_digits[i]
    i = 0
    while k > sum_digits[i]:
        i += 1

    # ans 为包含第 k 位数字的具体数字
    ans = 10 ** (i - 1) - 1
    ans += (k - sum_digits[i - 1]) // i
    if (k - sum_digits[i - 1]) % i != 0:
        ans += 1

    # 求出在该数字中的具体位置并输出对应数字字符
    pos = (k - sum_digits[i - 1]) % i
    # 原逻辑中当余数为 0 时索引为 -1，刚好取最后一位
    print(str(ans)[pos - 1])


if __name__ == "__main__":
    # 示例：调用 main(15) 寻找第 15 个数字
    # 可按需要修改 n 进行测试
    n = 15
    main(n)