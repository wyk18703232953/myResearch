def main(n):
    # 映射：原程序的 n 作为规模参数
    # 生成确定性 v，与 n 有固定关系
    v = n // 2 + 1

    x = 0
    c = 0
    for i in range(1, n):
        if x < n - i:
            delta = min((n - i), v - x)
            c += i * delta
            x += delta
        x -= 1

    # print(c)
    pass
if __name__ == "__main__":
    main(10)