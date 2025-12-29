import random

def main(n):
    # 随机生成规模为 n 的测试数据：
    # 这里将 n 解释为四个参数 k, n_val, s, p 的最大值范围
    # 可根据需要调整生成规则
    k = random.randint(1, n)
    n_val = random.randint(1, n)
    s = random.randint(1, n)
    p = random.randint(1, n)

    # 原逻辑
    x = (n_val + s - 1) // s
    x *= k
    result = (x + p - 1) // p

    print(result)

if __name__ == "__main__":
    # 示例：调用 main，规模参数可自行调整
    main(100)