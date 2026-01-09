def main(n):
    # 根据规模 n 生成测试数据，示例：令 k = n*(n+1)//4（可根据需要修改）
    # 保证是整数时建议让 n*(n+1) 能被 4 整除
    k = n * (n + 1) // 4

    a = 1
    b = -(2 * n + 3)
    c = n * n + n - 2 * k

    d = int((b * b - 4 * a * c) ** 0.5)

    s1 = (-b + d) // (2 * a)
    s2 = (-b - d) // (2 * a)

    if 0 <= s1 <= n:
        # print(s1)
        pass

    else:
        # print(s2)
        pass
if __name__ == "__main__":
    # 示例运行
    main(10)