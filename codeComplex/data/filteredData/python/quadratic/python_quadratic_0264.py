def main(n: int):
    # 根据 n 生成测试数据，这里给出一种确定性规则：
    # 若 n <= 1：a = 1, b = 1
    # 若 2 <= n <= 3：a = 1, b = 2
    # 若 n >= 4：a = 1, b = n - 1
    # 你可以根据需要自定义生成方式
    if n <= 1:
        a, b = 1, 1
    elif n <= 3:
        a, b = 1, 2
    else:
        a, b = 1, n - 1

    # 以下为原逻辑（移除 input() 并使用上面生成的 a, b）
    if min(a, b) > 1 or 1 < n < 4 and max(a, b) == 1:
        print('NO')
        return

    print('YES')
    f = int(a == 1)
    g = [a, b][f]
    r = [[f] * n for _ in range(n)]
    for i in range(n):
        r[i][i] = 0
    for i in range(n - g):
        r[i][i + 1] ^= 1
        r[i + 1][i] ^= 1
    for x in r:
        print(*x, sep='')

    johnny = 0  # 保留原变量以保持结构（未使用）


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)