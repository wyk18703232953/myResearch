import random

def main(n):
    # 生成测试数据
    # 随机生成递增数组 a（原程序隐含要求 a 是非降序，否则差值无意义）
    a = sorted(random.randint(0, 10 * n) for _ in range(n))
    # 生成 m（最大跨度），设为与数据规模相关
    m = random.randint(1, 10 * n)

    k = 0
    ans = -1.0
    for i in range(n - 1):
        while k < n - 1 and a[k + 1] - a[i] <= m:
            k += 1
        if i < k - 1:
            ans = max(ans, (a[k] - a[i + 1]) / (a[k] - a[i]))
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，n 可按需修改
    main(10)