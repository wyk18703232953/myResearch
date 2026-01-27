def main(n):
    # 确定性生成 k，使得存在合法解 i
    # 从原方程 k = n*(n+1)/2 - i*(i+1)/2 推出：
    # 这里固定选择 i = n//2，保证 0 <= i <= n-1
    i = n // 2
    k = n * (n + 1) // 2 - i * (i + 1) // 2

    b = -(2 * n + 3)
    c = n * n + n - 2 * k
    x = (-b - ((b * b - 4 * c) ** 0.5)) // 2
    y = (-b + ((b * b - 4 * c) ** 0.5)) // 2
    x, y = int(x), int(y)
    ans = None
    for t in [x - 1, x, x + 1, y - 1, y, y + 1]:
        if t * t + b * t + c == 0 and 0 <= t <= n - 1:
            ans = t
            break
    if ans is not None:
        # print(ans)
        pass

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    main(10)