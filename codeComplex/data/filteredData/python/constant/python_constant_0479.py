import random

def main(n: int):
    # 根据规模 n 生成测试数据，这里让 a, b 的数量级随 n 增长
    # 例如 a, b 在 [1, 10^n] 范围内随机生成
    upper = 10 ** max(1, n)  # 防止 n=0 时为 10^0=1
    a = random.randint(1, upper)
    b = random.randint(1, upper)

    # 原逻辑：计算向上取整的 b / a
    result = (b + a - 1) // a
    print(result)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(2)