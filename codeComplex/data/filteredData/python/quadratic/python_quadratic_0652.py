import random

def main(n: int) -> int:
    # 生成规模为 n 的测试数据：1 到 10*n 之间的随机整数
    a = [random.randint(1, 10 * n) for _ in range(n)]

    a.sort()
    ans = 0
    # 直接模拟原逻辑
    while len(a) > 0:
        k = a.pop(0)
        a = [i for i in a if i % k != 0]
        ans += 1

    return ans


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可按需调整 n
    result = main(10)
    print(result)