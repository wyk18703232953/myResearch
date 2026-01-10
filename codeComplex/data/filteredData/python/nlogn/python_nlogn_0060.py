def main(n):
    # n 表示数组长度
    a = [(i * 3 + 1) % (2 * n + 1) for i in range(n)]
    s = " ".join(str(x) for x in a)  # 保留原程序的第一个 input 结构（无实际用途）

    k = sorted(a)
    b = 0
    q = 0
    m = 0
    for i in k:
        b = b + i
    for i in k[::-1]:
        q = q + i
        m = m + 1
        if q > (b / 2):
            break
    print(m)


if __name__ == "__main__":
    main(10)