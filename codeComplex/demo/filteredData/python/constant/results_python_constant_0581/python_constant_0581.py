def main(n):
    # 确定性生成 x, y，映射到 [1, n]
    if n <= 0:
        return
    x = (n // 2) % n + 1
    y = (n // 3) % n + 1

    ans = (x - 1) + (y - 1) <= (n - x) + (n - y)
    # print('White' if ans else 'Black')
    pass
if __name__ == "__main__":
    main(10)