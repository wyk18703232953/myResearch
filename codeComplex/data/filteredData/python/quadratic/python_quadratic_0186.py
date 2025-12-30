import random

def main(n):
    # 1) 生成规模为 n 的测试数据
    # a: 原始数组，元素为 0~100 的随机整数
    a = [random.randint(0, 100) for _ in range(n)]

    # q: 随机查询次数，这里设为 n（可按需调整）
    q = n
    # 查询区间 [l, r]，1 <= l <= r <= n
    queries = []
    for _ in range(q):
        l = random.randint(1, n)
        r = random.randint(l, n)
        queries.append((l, r))

    # 2) 保留原逻辑：构建 array
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

    # 3) 按查询输出答案
    for l, r in queries:
        print(str(array[r - l][l - 1]))


# 示例：当直接运行该文件时，执行 main(5)
if __name__ == "__main__":
    main(5)