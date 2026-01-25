def main(n):
    # 通过 n 确定性生成 (n, a, b)
    # 约束：a, b 在 [1, n]，并且常见情况均可覆盖
    if n < 2:
        # 对于太小的 n，不满足原算法输入约束，这里直接返回
        return

    # 确定性构造 a, b（不使用随机）：
    # 将 a, b 映射到 [1, n] 区间内，覆盖多种组合
    a = (n % n) + 1          # 实际上恒为 1
    b = ((n // 2) % n) + 1   # 周期性遍历 1..n

    # 按原代码逻辑执行
    d = []
    for i in range(n):
        d.append(["1"] * n)
        d[i][i] = "0"

    if [n, a, b] == [2, 1, 1]:
        print("NO")
    elif [n, a, b] == [3, 1, 1]:
        print("NO")
    elif a == 1:
        c = n - b
        for i in range(c):
            d[i][i + 1] = "0"
            d[i + 1][i] = "0"
        print("YES")
        for i in range(n):
            print("".join(d[i]))
    elif a != 1 and b != 1:
        print("NO")
    else:
        print("YES")
        for i in range(a - 1):
            for j in range(n):
                d[i][j] = "0"
            for j in range(n):
                d[j][i] = "0"
        for i in range(n):
            print("".join(d[i]))


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的规模
    main(10)