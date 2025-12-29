import random

def main(n):
    # 根据规模 n 生成测试数据：
    # 这里构造一个 S，使得量级与 n 相关，便于测试
    # 例如：S 为 1 到 n^2 间的随机数
    if n <= 0:
        raise ValueError("n 必须为正整数")
    S = random.randint(1, n * n)

    # 原逻辑：输出 (S + n - 1) // n
    result = (S + n - 1) // n
    print(result)

# 示例：手动调用
# main(10)