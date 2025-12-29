import random

def main(n: int):
    # 生成测试数据：t组测试，每组n个正整数
    # 这里让 t = 1，如需多组可修改
    t = 1
    test_cases = []
    for _ in range(t):
        # 生成一个长度为 n 的数组，元素范围 1~10
        # 范围可根据需要调整
        a = [random.randint(1, 10) for _ in range(n)]
        test_cases.append(a)

    for a in test_cases:
        n = len(a)
        b = []
        res_a, res_b = 1, 10**18

        a = sorted(a)
        i = 0
        while i < n - 1:
            if a[i] == a[i + 1]:
                b.append(a[i])
                i += 1
            i += 1

        def p2s(x, y):
            return (x + y) ** 2 / (x * y)

        for i in range(len(b) - 1):
            if p2s(res_a, res_b) > p2s(b[i], b[i + 1]):
                res_a, res_b = b[i], b[i + 1]

        print(res_a, res_a, res_b, res_b)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)