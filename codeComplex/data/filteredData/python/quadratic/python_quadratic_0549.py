def main(n):
    # 映射含义：
    #   原程序中有两个输入：n, e
    #   这里固定令 e = n // 2，使得 (n - e) // 2 有合理规模
    total_n = n
    e = total_n // 2

    n_val = total_n
    d = (n_val - e) // 2
    q = []
    while n_val > 0:
        i = min(n_val, d)
        while i > 0:
            q.append('1')
            i -= 1
            n_val -= 1
        if n_val > 0:
            q.append('0')
            n_val -= 1

    result = "".join(q)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(1000)