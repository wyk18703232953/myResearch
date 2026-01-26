def main(n):
    arr = []
    d = {}
    # n 表示测试用例数量
    for _ in range(n):
        # 确定性生成 a, b, c
        a = _ + 1              # 1, 2, 3, ...
        b = (_ * 2) + 3        # 3, 5, 7, ...
        c = (_ % 5) + 1        # 1, 2, 3, 4, 5, 1, 2, ...
        x = (a + b) / c
        arr.append(x)
        if x not in d:
            d[x] = 0
        d[x] += 1

    for i in arr:
        # print(d[i], end=" ")
        pass
if __name__ == "__main__":
    main(10)