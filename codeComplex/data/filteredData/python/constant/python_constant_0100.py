import random

def main(n: int):
    """
    n: 测试数据规模，即测试用例个数
    自动生成 n 组 (a, b)，并按原逻辑计算输出结果。
    """
    t = n
    ans = ''
    
    # 生成测试数据：a, b 为正整数，避免为 0
    # 可根据需要调整生成范围
    test_data = []
    for _ in range(t):
        a = random.randint(1, 10**9)
        b = random.randint(1, 10**9)
        test_data.append((a, b))
    
    for a, b in test_data:
        k = 0
        while a > 0 and b > 0:
            if a >= b:
                k += a // b
                a %= b
            else:
                k += b // a
                b %= a
        ans += str(k) + '\n'
    
    print(ans, end='')


if __name__ == "__main__":
    # 示例：运行 5 组测试
    main(5)