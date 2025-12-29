import random

def solve_case(a, b):
    ans = 0
    while a > 0 and b > 0:
        if a < b:
            a, b = b, a
        ans += a // b
        a = a % b
    return ans

def main(n):
    random.seed(0)
    for _ in range(n):
        # 生成测试数据：a, b 为正整数，范围可根据需要调整
        a = random.randint(1, 10**9)
        b = random.randint(1, 10**9)
        print(solve_case(a, b))

if __name__ == "__main__":
    # 示例：运行 n=5 组测试数据
    main(5)