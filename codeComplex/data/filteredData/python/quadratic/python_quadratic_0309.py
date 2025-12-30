import random

def main(n):
    # 生成测试数据：长度为 n 的数组 a，k 为 [1, n] 内的随机整数
    if n <= 0:
        return

    k = random.randint(1, n)
    # 例如生成范围在 [-10**4, 10**4] 的随机整数
    a = [random.randint(-10**4, 10**4) for _ in range(n)]

    ans = -1 * 10**9 + 7
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += a[j]
            if j - i + 1 >= k:
                ans = max(ans, s / (j - i + 1))
    print(ans)

# 示例调用
if __name__ == "__main__":
    main(10)