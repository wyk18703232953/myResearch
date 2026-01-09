def main(n):
    # n 作为输入规模，同时生成两个长度均为 n 的数组 c 和 a
    # c 为递增序列，a 为每隔两个元素略大一些的序列，用简单算术保证确定性
    m = n
    c = [i for i in range(1, n + 1)]
    a = [i // 2 + 1 for i in range(1, m + 1)]

    c_i = 0
    a_i = 0
    bought = 0
    while c_i != n and a_i != m:
        if a[a_i] >= c[c_i]:
            a_i += 1
            c_i += 1
            bought += 1

        else:
            c_i += 1
    # print(bought)
    pass
if __name__ == "__main__":
    main(10)