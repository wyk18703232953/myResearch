import random

def solve(n: int) -> int:
    # 原逻辑的封装，返回结果而不是打印
    if n >= 0:
        return n
    else:
        s = str(abs(n))
        n1 = int(s[:len(s) - 1])

        temp = s[len(s) - 1]
        n2_str = s[:len(s) - 2]
        n2 = int(n2_str + temp) if n2_str != "" else int(temp)

        if n1 <= n2:
            return -n1 if n1 != 0 else 0
        else:
            return -n2 if n2 != 0 else 0

def main(n: int):
    # 根据规模 n 生成测试数据：
    # 生成 [-10^n + 1, 10^n - 1] 范围内的随机整数
    if n <= 0:
        test_value = 0
    else:
        limit = 10 ** n - 1
        test_value = random.randint(-limit, limit)

    result = solve(test_value)
    print(result)

if __name__ == "__main__":
    # 示例：用 n=3 运行一次
    main(3)