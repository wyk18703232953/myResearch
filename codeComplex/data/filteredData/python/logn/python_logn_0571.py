def main(n):
    # 根据规模 n 生成一个合理范围内的查询 k（第 k 位数字）
    # 这里简单设为查询第 n 位数字（从 1 开始）
    k = n

    x, y = 1, 9
    k -= 1
    while k > x * y:
        k -= x * y
        x += 1
        y *= 10
    a = 10 ** (x - 1) + k // x
    print(str(a)[k % x])


if __name__ == "__main__":
    # 示例：调用 main(100) 可根据需要自行修改测试规模
    main(100)