def main(n):
    # 确定性生成输入数据
    A = n
    B = n % 5 + 1
    C = (n % 7) + 2
    T = 2 * n + 10
    t = [(i * 3 + 1) % (T + 5) for i in range(n)]

    if B > C:
        # print(n * A)
        pass

    else:
        c = 0
        t.sort()
        for i in t:
            c += (T - i) * (C - B) + A
        # print(c)
        pass
if __name__ == "__main__":
    main(10)