import random

def Is_prime(n: int) -> bool:
    if n < 2:
        return False
    # 小优化：先排除偶数
    if n > 2 and n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def main(n: int):
    # 1. 根据规模 n 生成测试数据
    # 原程序逻辑：给定一个整数 n，寻找 2..99 中的非素数 i 和 n-i 都为非素数
    # 这里按要求“根据 n 生成测试数据”：如果 n 不合适（太小），就基于 n 生成一个更大的测试数
    if n < 10:
        # 保证搜索空间中更可能存在解
        n = max(10, n * 10)

    # 2. 保留原始核心逻辑：从 2 到 99 中找非素数 i 和非素数 n-i
    for i in range(2, 100):
        if not Is_prime(i) and not Is_prime(n - i):
            print(i, n - i)
            break

if __name__ == "__main__":
    # 示例：以 n = 100 作为规模调用
    main(100)