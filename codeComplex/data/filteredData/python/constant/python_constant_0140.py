from random import randint

def solve(a, b):
    if a == 0:
        return 0
    return b // a + solve(b % a, a)

def main(n):
    # 生成测试数据：a, b 为 1 到 n 的随机整数，且确保 a, b 不全为 0
    a = randint(1, n)
    b = randint(1, n)
    # 为了和原程序语义一致，这里允许 a > b 或 b > a，原逻辑都能处理
    result = solve(a, b)
    print(result)

if __name__ == "__main__":
    # 示例：规模 n 可在此指定
    main(10)