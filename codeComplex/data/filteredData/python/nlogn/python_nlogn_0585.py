def main(n):
    import math

    # 根据 n 构造输入规模
    # 为了可规模化，这里直接把 n 作为原程序中的 n
    N = max(1, n)

    if N == 3:
        # print('1 1 3')
        pass

    else:
        t = 1
        while t <= N:
            ct = math.ceil((N // t) / 2)
            for _ in range(ct):
                # print(t, end=" ")
                pass
            if ct == 2 and (N // t) % 2 != 0:
                t = t * 3

            else:
                t = t * 2
        # print(" ")
        pass
if __name__ == "__main__":
    # 示例：使用 n = 10 运行
    main(10)