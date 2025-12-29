import random

def main(n):
    # 生成测试数据：n 和 k，保证 0 <= p_i < 256
    # 这里让 k 在 [1, 10]，n 在调用时指定，ps 为长度为 n 的随机数组
    k = random.randint(1, 10)
    ps = [random.randint(0, 255) for _ in range(n)]

    mapping = [-1 for _ in range(256)]
    res = []

    for p in ps:
        if mapping[p] == -1:
            j = p - k + 1
            # 找到合适的 j，使得区间 [j, j+k-1] 能覆盖 p 且不与已有映射冲突
            while j < 0 or (mapping[j] != -1 and mapping[j] + k <= p):
                j += 1
            for i in range(j, p + 1):
                mapping[i] = j
        res.append(mapping[p])

    print("n:", n)
    print("k:", k)
    print("ps:", " ".join(map(str, ps)))
    print("res:", " ".join(map(str, res)))


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)