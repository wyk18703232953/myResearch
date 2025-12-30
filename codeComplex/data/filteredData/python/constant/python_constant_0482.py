def main(n):
    # 根据规模 n 生成测试数据
    # 这里假设 k 为与 n 同规模的数，例如 k = n^2
    k = n * n

    # 原逻辑：ceil(k / n)
    ans = (k + n - 1) // n
    print(ans)


if __name__ == '__main__':
    # 可以在此处自定义测试规模
    # 示例：当规模为 10 时运行
    main(10)