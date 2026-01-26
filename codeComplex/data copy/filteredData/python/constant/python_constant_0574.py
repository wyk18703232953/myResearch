def main(n):
    # 确定性生成 x, y
    x = n // 2 + 1
    y = n // 3 + 1
    x = min(max(1, x), n)
    y = min(max(1, y), n)

    if x - 1 + y - 1 <= n - x + n - y:
        # print('White')
        pass

    else:
        # print('Black')
        pass
if __name__ == "__main__":
    main(10)