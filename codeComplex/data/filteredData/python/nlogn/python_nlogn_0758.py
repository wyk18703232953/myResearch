import random

def main(n):
    # 生成测试数据：t 组测试，每组长度为 n 的数组
    # 这里设定 t = 5，可以按需要修改或参数化
    t = 5
    test_cases = []
    for _ in range(t):
        # 生成长度为 n 的随机整数数组，元素范围可按需调整
        ai = [random.randint(1, 10**9) for _ in range(n)]
        test_cases.append(ai)

    # 模拟原逻辑并输出结果
    for ai in test_cases:
        ai.sort()
        # 与原代码保持一致：n 为数组长度
        ans = min(len(ai) - 2, ai[-2] - 1)
        print(ans)

if __name__ == "__main__":
    # 示例：调用 main(5)，规模 n = 5
    main(5)