import random

def main(n):
    # 生成测试数据：n 个数，保证在 0..255 范围内
    # 随机生成 k，保证 k>=1 且不超过 256
    k = random.randint(1, 256)
    ps = [random.randint(0, 255) for _ in range(n)]

    mapping = [-1 for _ in range(256)]
    res = []

    for p in ps:
        if mapping[p] == -1:
            j = p - k + 1
            while j < 0 or (mapping[j] != -1 and mapping[j] + k <= p):
                j += 1
            for i in range(j, p + 1):
                mapping[i] = j
        res.append(mapping[p])

    print("n =", n)
    print("k =", k)
    print("ps =", " ".join(map(str, ps)))
    print("res =", " ".join(map(str, res)))


if __name__ == "__main__":
    # 示例调用，规模可自行调整
    main(10)