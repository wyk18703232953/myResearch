def main(n):
    # 确定性生成 a, b
    # 约束：1 <= a <= b <= n
    if n < 2:
        # print(0)
        pass
        return
    a = 1
    b = n // 2 if n // 2 >= 1 else 1
    if b > n:
        b = n
    if a > b:
        a, b = b, a

    # 生成长度为 n 的数组 l
    # 使用确定性算术构造元素
    l = [(i * 3 + 7) % (n * 5 + 11) for i in range(n)]

    l.sort()
    # print(l[b] - l[b - 1])
    pass
if __name__ == "__main__":
    main(10)