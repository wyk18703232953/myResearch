def main(n):
    # 映射：原程序中 n, k 两个输入，这里用 n 作为总体规模
    # 设定 k 为与 n 有确定性关系的整数，保证不同情况都能覆盖
    # 例如：k = max(1, n // 3) 保证 3*k <= n 对于较大 n 经常成立
    if n <= 0:
        return
    k = max(1, n // 3)

    if k == 1:
        result = "1" + "0" * (n - 1)
    elif 3 * k <= n:
        result = ("0" * ((n - k) // 2)) + "1" + ("0" * (k - 2)) + "1" + "0" * ((n - k) // 2)

    else:
        tmp = "0" * ((n - k) // 2) + "1"
        s = tmp
        s = tmp * (n // len(tmp) + 1)
        result = s[:n]

    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的值进行规模化实验
    main(10)