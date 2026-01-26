def main(n):
    # 将 n 映射为原程序中的 n, m
    # 这里令:
    #   original_n = n
    #   original_m = n  （规模为 n 的线性循环）
    original_n = n
    original_m = n

    res = 0
    mx = (original_n - 1) * original_n // 2
    if original_n & 1:
        mn = (original_n // 2) * (original_n // 2 + 1)

    else:
        mn = original_n * original_n // 4

    # 确定性生成 m 组 (x, d)
    # 例如:
    #   x_i = i
    #   d_i 在正负之间交替，幅度与 i 相关
    for i in range(original_m):
        x = i
        d = (i // 2 + 1) * (1 if i % 2 == 0 else -1)

        res += x * original_n
        if d > 0:
            res += mx * d

        else:
            res += mn * d

    ans = res / original_n
    # print(f"{ans:.10f}")
    pass
    return ans


if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n
    main(10)