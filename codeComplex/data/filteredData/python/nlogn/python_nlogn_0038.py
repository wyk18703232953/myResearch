def main(n):
    # 生成规模为 n 的确定性输入列表 b
    if n <= 0:
        return
    b = [i % 5 + 1 for i in range(1, n + 1)]

    z = max(b)
    if z == 1:
        b[b.index(z)] = 2
    else:
        b[b.index(z)] = 1
    print(*sorted(b))


if __name__ == "__main__":
    main(10)