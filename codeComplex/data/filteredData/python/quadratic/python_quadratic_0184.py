import random

def main(n):
    # 1. 生成规模为 n 的测试数据 a
    # 这里生成 0~1000 的随机整数，可以按需修改数据范围
    a = [random.randint(0, 1000) for _ in range(n)]

    # 2. 构建 array，与原逻辑一致
    array = []
    array.append(a)

    for _ in range(n - 1):
        aux = []
        for j in range(1, len(array[-1])):
            xor_val = array[-1][j - 1] ^ array[-1][j]
            aux.append(xor_val)
        array.append(aux)

    for j in range(1, len(array)):
        for k in range(len(array[j])):
            maximo = max(array[j][k], array[j - 1][k], array[j - 1][k + 1])
            array[j][k] = maximo

    # 3. 根据 n 生成查询 q 以及 (l, r)
    # 这里让 q 与 n 同规模，并随机生成合法的 [l, r]
    q = n
    queries = []
    for _ in range(q):
        l = random.randint(1, n)
        r = random.randint(l, n)
        queries.append((l, r))

    # 4. 输出查询结果（与原程序一样对 array 进行访问）
    for l, r in queries:
        print(array[r - l][l - 1])


if __name__ == "__main__":
    # 示例调用：可以修改 n 测试不同规模
    main(5)