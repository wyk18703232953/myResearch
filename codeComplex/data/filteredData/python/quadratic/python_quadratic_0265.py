def main(n):
    # 根据 n 生成测试数据 (示例：a=1, b=2，保证逻辑路径多样)
    # 你可以按需要改成其他生成方式
    if n == 2:
        a, b = 1, 1
    elif n == 3:
        a, b = 1, 1

    else:
        a, b = 1, min(2, n - 1)  # 简单示例生成

    d = []
    for i in range(n):
        d.append(["1"] * n)
        d[i][i] = "0"

    if [n, a, b] == [2, 1, 1]:
        # print("NO")
        pass
    elif [n, a, b] == [3, 1, 1]:
        # print("NO")
        pass
    elif a == 1:
        c = n - b
        for i in range(c):
            d[i][i + 1] = "0"
            d[i + 1][i] = "0"
        # print("YES")
        pass
        for i in range(n):
            # print("".join(d[i]))
            pass
    elif a != 1 and b != 1:
        # print("NO")
        pass

    else:
        # print("YES")
        pass
        for i in range(a - 1):
            for j in range(n):
                d[i][j] = "0"
            for j in range(n):
                d[j][i] = "0"
        for i in range(n):
            # print("".join(d[i]))
            pass
if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)