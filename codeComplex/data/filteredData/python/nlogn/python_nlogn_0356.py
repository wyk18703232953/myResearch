import random

def main(n):
    # 根据规模 n 生成测试数据：从 [1, 2n] 中随机选 n 个不同整数
    arr = set(random.sample(range(1, 2 * n + 1), n))

    def solve():
        for i in arr:
            for k in range(31):
                if i - (1 << k) in arr and i + (1 << k) in arr:
                    return [i - (1 << k), i, i + (1 << k)]
        for i in arr:
            for k in range(31):
                if i + (1 << k) in arr:
                    return [i, i + (1 << k)]
        for i in arr:
            return [i]

    lst = solve()
    print(len(lst))
    print(*lst)


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)