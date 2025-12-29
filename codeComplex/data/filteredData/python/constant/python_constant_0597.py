from math import ceil
import random

def main(n):
    # 根据规模 n 生成测试数据：
    # 这里假设原本的 n 表示题意中的 n，
    # 生成 k 为 [1, 3n] 范围内的随机正整数（避免除零）
    if n <= 0:
        return 0  # 或者视题意决定如何处理，这里简单返回 0

    k = random.randint(1, max(1, 3 * n))

    # 原逻辑
    result = ceil((n * 2) / k) + ceil((n * 5) / k) + ceil((n * 8) / k)
    print(result)
    return result

if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可修改 n
    main(10)