def main(n: int):
    # 这里将原来的 k = int(input()) - 1 改为用 n 构造测试数据
    # 假设规模 n 表示我们要查询的第 n 个数字（从 1 开始计数）
    # 与原程序一致，内部用 0-based 索引，所以减 1
    k = n - 1

    l = 1
    c = 9
    while k >= c * l:
        k -= c * l
        l += 1
        c *= 10

    c = 10 ** (l - 1) + k // l
    print(str(c)[k % l])


if __name__ == "__main__":
    # 示例调用：规模为 15
    main(15)