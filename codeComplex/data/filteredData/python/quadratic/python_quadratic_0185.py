import random

def main(n):
    # 1) 生成规模为 n 的随机测试数据
    # 原代码中：a 是长度为 n 的整数数组
    a = [random.randint(0, 10**9) for _ in range(n)]

    array = []
    array.append(a)

    # 2) 按原逻辑构造 xor 三角形
    for _ in range(n - 1):
        aux = []
        for j in range(1, len(array[-1])):
            xor_val = array[-1][j - 1] ^ array[-1][j]
            aux.append(xor_val)
        array.append(aux)

    # 3) 进行“最大值传播”处理
    for j in range(1, len(array)):
        for k in range(len(array[j])):
            maximo = max(array[j][k], array[j - 1][k], array[j - 1][k + 1])
            array[j][k] = maximo

    # 4) 生成测试查询数据 q 以及若干 (l, r)
    # 这里设定 q = n，查询若干随机区间，保证 1 <= l <= r <= n
    q = n
    queries = []
    for _ in range(q):
        l = random.randint(1, n)
        r = random.randint(l, n)
        queries.append((l, r))

    # 5) 输出每个查询的结果（保留原有输出格式）
    for l, r in queries:
        print(str(array[r - l][l - 1]))


# 示例：运行 main 并指定规模
if __name__ == "__main__":
    main(5)