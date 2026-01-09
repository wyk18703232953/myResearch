from itertools import permutations

def main(n: int):
    # 根据规模 n 生成测试数据：长度为 3 的列表 k
    # 这里简单设定为 [n, n+1, n+2]，可按需求调整生成策略
    k = [n, n + 1, n + 2]

    worked = 0
    for k1, k2, k3 in permutations(k):
        worked2 = 1
        for t in range(10000):
            if not (t % k1 == 0 or t % k2 == 1 or t % k3 == 2):
                worked2 = 0
                break  # 原代码未加 break，这里可不加，但加上更高效

        if worked2:
            worked = 1
            break

    if worked:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    # 示例：规模 n = 3
    main(3)