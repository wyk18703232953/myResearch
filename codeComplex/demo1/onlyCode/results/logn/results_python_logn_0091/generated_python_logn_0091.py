import random

def main(n: int):
    # 根据规模 n 生成测试数据，这里简单生成两个 0 ~ 2^n-1 的随机整数
    # 为避免超过 64 位移位范围，将 n 限制在 1..64
    n = max(1, min(n, 64))
    a = random.randint(0, (1 << n) - 1)
    b = random.randint(0, (1 << n) - 1)

    idx = 0
    if a == b:
        print(0)
    else:
        for i in range(63, -1, -1):
            set1 = (a >> i) & 1
            set2 = (b >> i) & 1
            if set1 != set2:
                idx = i
                break
        print((1 << (idx + 1)) - 1)


if __name__ == "__main__":
    # 示例：调用 main，规模设为 10
    main(10)