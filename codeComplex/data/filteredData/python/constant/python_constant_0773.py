import random

def sq(x: int) -> bool:
    return int(x ** 0.5) ** 2 == x

def main(n: int):
    # 生成 n 个测试样例
    test_cases = []
    for _ in range(n):
        # 随机生成一个正整数作为 n 的测试值
        # 可根据需要调整范围
        val = random.randint(1, 10**9)
        test_cases.append(val)

    # 按原逻辑处理每个测试样例
    for v in test_cases:
        if (v % 2 == 0 and sq(v // 2)) or (v % 4 == 0 and sq(v // 4)):
            print('YES')
        else:
            print('NO')


if __name__ == "__main__":
    # 示例：运行规模 n=10
    main(10)