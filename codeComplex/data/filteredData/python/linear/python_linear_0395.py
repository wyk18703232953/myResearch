import random

M = 0x3b800001

def main(n: int) -> int:
    # 生成规模为 n 的测试数据，这里示例为随机整数
    # 根据需要可调整生成范围
    a = [random.randint(0, 10**9) for _ in range(n)]

    wa = 0
    now = 1
    wa += a[-1]
    for i in range(n - 1)[::-1]:
        wa += (now * (n - i - 1) + now * 2) * a[i]
        wa %= M
        now *= 2
        now %= M
    return wa % M

if __name__ == "__main__":
    # 示例：调用 main(5)
    result = main(5)
    print(result)