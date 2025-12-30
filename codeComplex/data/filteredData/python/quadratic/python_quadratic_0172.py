import random


def main(n: int):
    # 生成测试数据：
    # 1. 随机选择 k（段最大长度），范围 [1, max(1, n//2)]
    # 2. 生成 n 个整数 xs，范围 [0, 10**4]
    if n <= 0:
        return

    k = random.randint(1, max(1, n // 2))
    xs = [random.randint(0, 10 ** 4) for _ in range(n)]

    mapka = {}
    lengths = {}
    result = []

    for x in xs:
        if x in mapka:
            result.append(mapka[x])
        else:
            left = max(0, x - k + 1)
            range_potential = x - left
            for i in range(range_potential, -1, -1):
                potential_left = x - i
                if potential_left not in mapka:
                    result.append(potential_left)
                    for y in range(potential_left, x + 1):
                        mapka[y] = potential_left
                    lengths[potential_left] = x - potential_left + 1
                    break
                else:
                    base = mapka[potential_left]
                    if lengths[base] + (x - potential_left) <= k:
                        result.append(base)
                        for y in range(base + lengths[base], x + 1):
                            mapka[y] = base
                            lengths[base] += 1
                        break

    print(' '.join(map(str, result)))


if __name__ == "__main__":
    # 示例：调用 main(10) 运行一组规模为 10 的测试
    main(10)