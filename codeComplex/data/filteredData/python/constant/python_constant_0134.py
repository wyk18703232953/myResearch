import random
import math

def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里生成两个 1 ~ n 之间的随机正整数 a, b
    a = random.randint(1, n)
    b = random.randint(1, n)

    # 保留原始 a, b 仅用于调试或验证时查看
    # print(f"a = {a}, b = {b}")

    ans = 0
    if a > b:
        ans += a // b
        a = a % b
    while b != 0:
        ans += a // b
        a, b = b, a % b
    print(ans)

if __name__ == "__main__":
    # 示例：可根据需要修改规模 n
    main(1000)