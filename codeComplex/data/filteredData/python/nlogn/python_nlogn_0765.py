import random

def main(n):
    # 生成测试数据：长度为 n 的整数数组
    # 这里生成 1~10^9 范围的随机整数，可按需要调整
    l = sorted(random.randint(1, 10**9) for _ in range(n))
    
    # 原逻辑
    k = max(0, min(n - 2, l[-2] - 1))
    print(k)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)