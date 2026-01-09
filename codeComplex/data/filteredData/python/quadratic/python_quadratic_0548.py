def main(n):
    # 映射：原程序中 n 为长度，k 为某个参数。
    # 这里固定令 k = n // 3（可根据需要调整，但必须确定性）。
    k = n // 3

    nn = n  # 使用局部变量，避免修改参数 n
    d = nn - k
    d = d // 2

    l = []

    while nn > 0:
        i = min(nn, d)
        while i > 0:
            l.append('1')
            i -= 1
            nn -= 1
        if nn > 0:
            l.append('0')
            nn -= 1

    result = "".join(l)
    return result


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的规模
    for test_n in [1, 5, 10, 20]:
        # print(test_n, main(test_n))
        pass