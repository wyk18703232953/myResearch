def main(n):
    # 确定性生成 x, y，映射到 [1, n] 区间
    if n <= 0:
        return
    x = (n // 2) % n + 1
    y = (n // 3) % n + 1

    d1 = max(x - 1, y - 1)
    d2 = max(n - x, n - y)
    if d1 <= d2:
        # print("White")
        pass

    else:
        # print("Black")
        pass
if __name__ == "__main__":
    main(10)