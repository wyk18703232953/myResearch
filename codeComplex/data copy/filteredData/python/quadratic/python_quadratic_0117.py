def main(n):
    # 约定：n 为数组 a 的长度；m 为 a 中值域上界（1..m）
    if n <= 0:
        return

    # 确定性地生成 m：保证 m >= 1
    m = n // 2 + 1

    # 确定性构造长度为 n 的数组 a，元素在 1..m 之间
    # 使用简单算术和取模，保证无随机性
    a = [(i % m) + 1 for i in range(1, n + 1)]

    b = [0] * m
    for x in a:
        b[x - 1] += 1
    b.sort()
    # 为保持与原程序的输出行为一致，这里打印最小计数
    # print(b[0])
    pass
if __name__ == "__main__":
    main(10)