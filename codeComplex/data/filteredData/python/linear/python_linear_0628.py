def solve_one(n, k):
    if n >= 40:
        return "YES " + str(n - 1)
    else:
        ans = -1
        for m in range(1, n + 1):
            asd = (4 ** m - 1) // 3
            asd2 = (2 ** m - 1) ** 2
            asd2 *= (4 ** (n - m) - 1) // 3
            asd += asd2
            if asd >= k and m * m <= k:
                ans = n - m
                break
        if ans == -1:
            return "NO"
        else:
            return "YES " + str(ans)


def main(n):
    # 生成规模为 n 的测试数据：
    # 构造 t 组测试，每组固定 n，k 从 1 到 n 变化
    t = n
    results = []
    for i in range(1, t + 1):
        k = i
        results.append(solve_one(n, k))

    # 按原逻辑打印输出
    for res in results:
        print(res)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)