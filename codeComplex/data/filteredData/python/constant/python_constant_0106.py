import random

def solve_case(a, b):
    total = 0
    largerNum = max(a, b)
    smallerNum = min(a, b)
    while True:
        div = largerNum // smallerNum
        total += div
        rem = largerNum % (smallerNum * div)
        if rem == 0:
            break
        else:
            largerNum = smallerNum
            smallerNum = rem
    return total

def main(n):
    """
    n: 规模，用来控制测试数据数量
    这里生成 n 组测试数据，每组为两个正整数 (a, b)
    """
    random.seed(0)
    numCases = n
    results = []

    for _ in range(numCases):
        # 生成测试数据，范围可根据需要调整
        a = random.randint(1, 10**6)
        b = random.randint(1, 10**6)
        results.append(solve_case(a, b))

    # 输出结果
    for ans in results:
        print(ans)

if __name__ == "__main__":
    # 示例：n=5
    main(5)