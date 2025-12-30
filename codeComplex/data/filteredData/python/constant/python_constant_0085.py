import random

def solve(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 6
    if n % 2 == 0:
        if n % 3 == 0:
            return (n - 1) * (n - 2) * (n - 3)
        else:
            return n * (n - 1) * (n - 3)
    else:
        return n * (n - 1) * (n - 2)

def main(n: int):
    # 根据规模 n 生成测试数据，这里简单设为：在 [1, n] 中随机取一个整数作为测试输入
    test_n = random.randint(1, max(1, n))
    ans = solve(test_n)
    print(ans)

if __name__ == "__main__":
    # 示例：可自行修改规模 n
    main(10)