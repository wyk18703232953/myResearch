import random

def main(n):
    # 根据规模 n 生成测试数据：
    # 原题中有两个参数 n, k，这里将 n 作为原始 n 的规模，
    # 再生成一个与 n 同量级的 k，避免除零。
    original_n = n
    k = max(1, random.randint(1, 2 * n))

    # 按照原始逻辑计算
    result = ((2 * original_n + k - 1) // k +
              (5 * original_n + k - 1) // k +
              (8 * original_n + k - 1) // k)

    print(result)

if __name__ == "__main__":
    # 示例：调用 main(10) 进行测试
    main(10)