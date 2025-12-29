import random

def main(n):
    # 生成测试数据
    # 1 <= a[i] <= n，随机选择 val
    a = [0] + [random.randint(1, n) for _ in range(n)]
    val = random.randint(1, n)

    suma = [0 for _ in range(n + 1)]
    mx = 0
    target = 0

    for i in range(1, n + 1):
        suma[i] = suma[i - 1]
        mx = max(mx, a[i])
        if a[i] == val:
            target += 1
            suma[i] += 1

    ans = 0
    pre = [0 for _ in range(mx + 1)]
    dp = [0]

    for i in range(1, n + 1):
        dp.append(max(1, 1 + dp[pre[a[i]]] - suma[i] + suma[pre[a[i]]]))
        if a[i] != val:
            ans = max(ans, dp[i])
        pre[a[i]] = i

    print(ans + target)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)