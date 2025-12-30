import random

def main(n):
    # 生成测试数据：t 组测试，每组长度随机，元素值适中
    t = max(1, n // 5)
    test_cases = []
    for _ in range(t):
        length = max(1, random.randint(1, n))
        # 让数值范围与 n 相关，避免过大
        max_val = max(10, n)
        a = [random.randint(1, max_val) for _ in range(length)]
        test_cases.append(a)

    # 原逻辑封装成函数，方便复用
    def solve_case(a):
        if len(set(a)) == 1:
            x = a[0]
            return x, x, x, x
        a.sort()
        g1 = False
        d = {}
        mx = 10001
        for v in a:
            if v not in d:
                d[v] = 1
            else:
                d[v] += 1
            if d[v] == 4:
                g1 = True
                if v < mx:
                    mx = v
        if g1:
            return mx, mx, mx, mx
        else:
            res = []
            for k in d:
                if d[k] >= 2:
                    res.append(k)
            m = len(res)
            if m < 2:
                # 若没有足够的数构成答案，退化处理：随便返回 4 个元素
                x = a[0]
                return x, x, x, x
            minj = 0
            for j in range(m - 1):
                if (res[j] * res[j + 1] * (res[minj] ** 2 + res[minj + 1] ** 2)
                        > res[minj] * res[minj + 1] * (res[j] ** 2 + res[j + 1] ** 2)):
                    minj = j
            return res[minj], res[minj], res[minj + 1], res[minj + 1]

    # 依次处理所有测试用例并打印结果
    for a in test_cases:
        x1, x2, x3, x4 = solve_case(a)
        print(x1, x2, x3, x4)


if __name__ == "__main__":
    # 示例：n 可根据需要修改
    main(20)