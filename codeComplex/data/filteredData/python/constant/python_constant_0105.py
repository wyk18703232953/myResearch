import random

def substraction(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        if a > b:
            count = a // b
            return substraction(a % b, b) + count
        else:
            count = b // a
            return substraction(a, b % a) + count

def main(n):
    """
    n: 规模，表示要生成的测试用例数 t
    为每个测试用例随机生成两个正整数 a, b 并调用 substraction(a, b)
    输出每个测试用例的结果
    """
    t = n
    res = []
    # 生成测试数据，这里生成范围在 [1, 10^6] 的正整数对
    for _ in range(t):
        a = random.randint(1, 10**6)
        b = random.randint(1, 10**6)
        ele = substraction(a, b)
        res.append(ele)

    for val in res:
        print(val)

if __name__ == "__main__":
    # 示例：运行规模为 5 的测试
    main(5)