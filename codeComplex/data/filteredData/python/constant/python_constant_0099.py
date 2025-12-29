import random
import collections  # 保留原有 import（虽未使用）


def numz(a, b):
    if a and b:
        if b > a:
            a, b = b, a
        d, m = divmod(a, b)
        return d + numz(b, m)
    else:
        return 0


def main(n):
    """
    n: 测试数据规模，即生成 n 行 (a, b) 对，并输出 numz(a, b)
    """
    # 根据 n 生成测试数据：n 行，每行两个正整数 (a, b)
    # 可根据需要调整范围
    test_data = []
    for _ in range(n):
        a = random.randint(1, 10**6)
        b = random.randint(1, 10**6)
        test_data.append((a, b))

    # 模拟原逻辑：跳过第一行输入（原代码跳过的是数量行）
    # 在这里第一行不需要，所以直接从 test_data[0:] 使用
    for a, b in test_data:
        print(numz(a, b))


if __name__ == "__main__":
    # 示例: 调用 main(5) 生成 5 组测试数据
    main(5)