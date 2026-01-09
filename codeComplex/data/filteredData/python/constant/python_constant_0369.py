def main(n):
    # 确定性生成 a, b, c, n_original
    a = n
    b = n // 2 + 1
    c = n // 3
    n_original = 2 * n

    if c > b or c > a or c > n_original:
        # print(-1)
        pass

    else:
        k = c + (a - c) + (b - c)
        k = n_original - k
        if k > 0:
            # print(k)
            pass

        else:
            # print(-1)
            pass
if __name__ == "__main__":
    main(10)