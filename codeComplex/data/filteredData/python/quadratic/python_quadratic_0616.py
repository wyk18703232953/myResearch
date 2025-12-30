import random

def main(n):
    # 生成测试数据：n, m, k 和长度为 n 的数组 a
    # 这里简单设定：1 <= m <= n，k 为适度范围的随机数
    m = random.randint(1, n)
    k = random.randint(0, 10)

    # 生成数组 a，元素在 -10 到 10 之间
    a = [random.randint(-10, 10) for _ in range(n)]

    values = []
    for j in range(n):
        result = a[j]
        sum1 = 0
        for i in range(m):
            if j - i >= 0:
                sum1 += a[j - i]
                if sum1 > result:
                    result = sum1
            else:
                continue
        if j - m >= 0:
            result = max(result, sum1 + values[j - m])
        values.append(max(0, result - k))

    # 返回结果（原程序是 print(max(values))）
    return max(values)

if __name__ == "__main__":
    # 示例：调用 main(10)，规模 n = 10
    ans = main(10)
    print(ans)