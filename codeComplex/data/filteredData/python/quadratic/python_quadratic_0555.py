def main(n: int):
    # 生成测试数据：让 m 与 n 同规模（可按需修改生成规则）
    m = n

    res = []
    for j in range(n // 2):
        for k in range(m):
            res.append(str(j + 1) + " " + str(k + 1))
            res.append(str(n - j) + " " + str(m - k))
    if n % 2:
        for j in range(m // 2):
            res.append(f"{n // 2 + 1} {j + 1}")
            res.append(f"{n // 2 + 1} {m - j}")
        if m % 2:
            res.append(f"{n // 2 + 1} {m // 2 + 1}")
    print("\n".join(res))


if __name__ == "__main__":
    # 示例：调用 main(5)，可按需修改 n
    main(5)