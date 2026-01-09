import math

def score(x: int) -> int:
    ans = 0
    xr = math.ceil(math.sqrt(x))

    divisors = []
    for i in range(1, xr + 3):
        if x % i == 0:
            divisors.append(i)
            divisors.append(x // i)

    divisors = sorted(set(divisors))

    # exclude 1 and x itself
    for d in divisors[1:-1]:
        ans += x // d

    return ans


def main(n: int):
    # 题目本身不依赖外部输入，只与 n 有关。
    # 将 n 视为规模参数，此处不再从 input() 读取。
    if n <= 3:
        # print(0)
        pass
        return

    total = 0
    for i in range(4, n + 1):
        total += score(i)

    # print(total * 4)
    pass
if __name__ == "__main__":
    # 示例：根据规模生成测试数据，这里直接调用 main(n)
    # 可自行修改 n 进行测试
    test_n = 10
    main(test_n)