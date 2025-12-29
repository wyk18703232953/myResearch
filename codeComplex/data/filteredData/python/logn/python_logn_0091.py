import random

def main(n: int):
    # 生成测试数据：a, b 为 [0, 2^n) 内的随机整数
    # 若 n 过大可根据需要截断
    max_bits = max(1, min(n, 63))  # 保证不超过原程序的位数范围
    a = random.randint(0, (1 << max_bits) - 1)
    b = random.randint(0, (1 << max_bits) - 1)

    # 原始逻辑
    if a == b:
        print(0)
    else:
        idx = 0
        for i in range(63, -1, -1):
            set1 = (a >> i) & 1
            set2 = (b >> i) & 1
            if set1 != set2:
                idx = i
                break
        print((1 << (idx + 1)) - 1)

if __name__ == "__main__":
    # 示例：可自行修改 n
    main(10)