def main(n):
    # 根据 n 生成 s：例如取一个和 n 同数量级的值
    # 可按需要调整生成策略
    s = n // 2 + 10

    r = 0
    v = min(n + 1, s + 19 * 9)
    for i in range(s, v):
        zz = f'{i}'
        sm = i
        for z in zz:
            sm -= int(z)

        if sm >= s:
            r += 1

    result = r + n - v + 1
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # 示例：调用 main，n 可按需要修改
    main(100000)