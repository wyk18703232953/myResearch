import random

def main(n: int):
    # 1. 生成规模为 n 的测试数据：整数数组 a
    # 这里假设数据范围为 [-n, n]，可按需要调整
    a = [random.randint(-n, n) for _ in range(n)]

    # 2. 保持原逻辑：统计不同元素个数，如果包含 0 则减一
    b = set(a)
    res = len(b)
    if 0 in b:
        res -= 1

    print(res)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)