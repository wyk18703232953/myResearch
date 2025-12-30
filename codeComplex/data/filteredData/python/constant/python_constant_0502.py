import math
import random

def main(n):
    """
    n: 规模，用于生成 n 组测试数据 (q = n)
    自动生成 q 组 (x, y, k) 并按原逻辑输出结果
    """
    q = n

    # 生成测试数据：x, y, k 为非负整数，可根据需要调整范围
    test_cases = []
    for _ in range(q):
        # 示例：x, y, k 在 [0, 10^6] 内随机生成
        k = random.randint(0, 10**6)
        x = random.randint(0, k) if random.random() < 0.7 else random.randint(0, 10**6)
        y = random.randint(0, k) if random.random() < 0.7 else random.randint(0, 10**6)
        test_cases.append((x, y, k))

    # 按原逻辑处理并输出
    for x, y, k in test_cases:
        if x > k or y > k:
            print(-1)
        else:
            if (x + y) % 2 == 0:
                if (k - max(x, y)) % 2 == 0:
                    print(k)
                else:
                    print(k - 2)
            else:
                if (k - max(x, y)) % 2 == 0:
                    print(k - 1)
                else:
                    print(k - 1)

if __name__ == "__main__":
    # 示例调用：规模为 5
    main(5)