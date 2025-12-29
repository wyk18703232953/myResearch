def main(n: int):
    # 这里根据 n 生成一组测试数据：
    # 约定：
    #   1 ≤ a < b ≤ n
    #   1 ≤ pos ≤ n
    # 简单生成一组可行数据（也可按需自定义策略）
    a = 1
    b = n
    pos = (n + 1) // 2  # 中间位置

    lf, rf = a - 1, n - b
    if lf == rf == 0:
        print("0")
    elif lf == 0:
        print(abs(pos - b) + 1)
    elif rf == 0:
        print(abs(pos - a) + 1)
    else:
        cl = abs(a - pos) + 1
        cr = abs(b - pos) + 1
        xn = abs(a - b) + 1
        if cl < cr:
            print(cl + xn)
        else:
            print(cr + xn)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)