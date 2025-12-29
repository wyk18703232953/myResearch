import random
import math

def check_number(n: int) -> str:
    for d in [2, 4]:
        if n % d != 0:
            continue
        temp = int((n // d) ** 0.5)
        temp -= 1
        while temp * temp < n // d:
            temp += 1
        if temp * temp == n // d:
            return "YES"
    return "NO"

def main(n: int):
    # 生成 n 个测试数据，这里生成 1 到 10^12 范围内的随机整数
    # 也可以根据需要调整数据分布
    random.seed(0)
    test_cases = [random.randint(1, 10**12) for _ in range(n)]

    results = []
    for x in test_cases:
        results.append(check_number(x))

    # 按原逻辑只输出结果，不输出中间测试数据
    for res in results:
        print(res)

if __name__ == "__main__":
    # 示例：调用 main(5) 产生 5 组测试数据并运行
    main(5)