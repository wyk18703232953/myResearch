import random

def main(n):
    # 根据规模 n 生成测试数据：
    # 这里将随机生成两个非负整数 l, r，使它们在 [0, 2^n - 1] 范围内
    # 并确保 l <= r（与原代码逻辑相符）
    if n <= 0:
        l, r = 0, 0
    else:
        max_val = (1 << n) - 1
        l = random.randint(0, max_val)
        r = random.randint(l, max_val)

    # 核心逻辑：给定 l, r，找到从最高位开始第一个不同的二进制位 i
    # 输出 (1 << (i+1)) - 1；若所有位都相同则输出 0
    for i in range(60, -1, -1):
        if ((l >> i) & 1) != ((r >> i) & 1):
            print((1 << (i + 1)) - 1)
            return
    print(0)


if __name__ == "__main__":
    # 示例：调用 main(10)，可按需修改 n
    main(10)