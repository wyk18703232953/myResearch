import random

def main(n):
    # 生成测试数据：随机挑选 t 组，每组长度 n，元素为 1~2n 之间的整数
    t = 5  # 可按需修改测试组数
    test_cases = []
    for _ in range(t):
        ar = [random.randint(1, 2 * n) for _ in range(n)]
        test_cases.append(ar)

    # 按原逻辑处理每一组数据并输出
    for ar in test_cases:
        if n <= 2:
            print(0)
            continue
        ar_sorted = sorted(ar, reverse=True)
        ans = 0
        for i in range(1, n - 1):
            if ar_sorted[0] > i and ar_sorted[1] > i:
                ans = i
        print(ans)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)