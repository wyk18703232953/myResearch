import random

def main(n):
    # 生成测试数据
    # n 表示元素个数
    # 设定总大小上限 b[1]，并生成 n 个 [a_i, b_i]，其中 b_i <= a_i
    a = []
    b = []

    # 生成 b[0] = n，b[1] 为目标上限（随机一个适中值）
    total_original = 0
    total_compressed = 0
    pairs = []

    for _ in range(n):
        # 生成原大小和压缩后大小
        orig = random.randint(1, 1000)
        comp = random.randint(0, orig)
        pairs.append([orig, comp])
        total_original += orig
        total_compressed += comp

    # 让 b[1] 介于 total_compressed 和 total_original 之间，或稍有概率其它情况
    # 保证有一些可压缩空间
    if total_compressed == total_original:
        limit = total_original
    else:
        # 随机在 [total_compressed, total_original] 之间
        limit = random.randint(total_compressed, total_original)

    b = [n, limit]
    inputs = pairs

    # 以下为原逻辑
    diff = []
    sinComprimir = 0

    comprimido = 0
    for k in range(len(inputs)):
        sinComprimir = sinComprimir + inputs[k][0]
        diff.append(inputs[k][0] - inputs[k][1])
        comprimido = comprimido + inputs[k][1]

    difference = sorted(diff)
    invDifference = difference[::-1]
    newTotal = sinComprimir
    iteraciones = 0
    iterador = 0

    if sinComprimir <= b[1]:
        print("0")
    elif comprimido > b[1]:
        print("-1")
    else:
        while newTotal > b[1]:
            iterador = iterador + 1
            newTotal = newTotal - invDifference[iterador - 1]
            iteraciones += 1
        print(iteraciones)


if __name__ == "__main__":
    # 示例调用：规模 n = 10
    main(10)