import random

def main(n):
    # 生成测试数据：
    # t：测试组数，这里简单设为 n（也可以根据需要调整）
    t = n

    # 为每组生成一个长度为 n 的数组，
    # 元素范围设为 [1, 2n]，保证有足够分散的值。
    test_cases = []
    for _ in range(t):
        arr = [random.randint(1, 2 * n) for _ in range(n)]
        test_cases.append(arr)

    # 对每个测试用例执行原逻辑并打印结果
    for arr in test_cases:
        arr_sorted = sorted(arr)
        a = arr_sorted[-2]
        print(min(n - 2, a - 1))


if __name__ == "__main__":
    # 示例调用：规模 n = 5
    main(5)