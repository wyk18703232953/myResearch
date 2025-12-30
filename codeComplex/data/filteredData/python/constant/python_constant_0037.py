import random

def main(n: int):
    """
    n: 测试规模，表示要生成的随机整数上界（1..n）
    """
    if n <= 0:
        return None  # 或者抛出异常，根据需要调整

    # 生成测试数据：从 1 到 n 之间的随机整数
    x = random.randint(1, n)

    # 原始逻辑：print(int(input())//2*3)
    result = x // 2 * 3

    # 返回结果及测试数据，便于验证
    return x, result


if __name__ == "__main__":
    # 示例：当作脚本使用时，给定一个规模，比如 100
    x, ans = main(100)
    print(x // 2 * 3)  # 与原程序行为一致，仅打印结果