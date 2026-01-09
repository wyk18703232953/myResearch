def main(n):
    # 根据 n 确定性生成 a, b, c
    a = n
    b = 2 * n
    c = (a + b) // 2
    if c > a or c > b or (a + b) - c >= n:
        # print(-1)
        pass

    else:
        # print(n - ((a + b) - c))
        pass
if __name__ == "__main__":
    main(10)