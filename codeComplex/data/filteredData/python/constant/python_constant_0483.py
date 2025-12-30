import random

def main(n: int):
    # 根据规模 n 生成测试数据
    # 约定：k 至少为 1，最大取 10*n
    if n <= 0:
        raise ValueError("n 必须为正整数")
    k = random.randint(1, 10 * n)

    # 原始逻辑
    p = (k - 1) // n + 1
    print(p)

# 示例调用（实际使用时可按需调用 main(n)）
if __name__ == "__main__":
    main(10)