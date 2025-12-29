import random

def iscomposite(value):
    for i in range(2, value):
        if value % i == 0:
            return '1'
    else:
        return '0'


def main(n):
    # 若 n 太小，则无有效分解
    if n < 8:
        return None

    # 主逻辑与原程序相同
    for i in range(4, n):
        a = i
        b = n - i
        if iscomposite(a) == '1' and iscomposite(b) == '1':
            print(a, b)
            return (a, b)

    # 若未找到则返回 None
    return None


if __name__ == "__main__":
    # 根据规模 n 生成测试数据，这里直接设置一个与 n 同规模的随机整数进行测试
    # 例如：n 在 [10, 100] 范围随机
    test_n = random.randint(10, 100)
    main(test_n)