def resheto(a):
    numbers = list(range(0, a + 1))
    primes = set()
    for k in range(2, a + 1):
        if numbers[k] != 0:
            primes.add(k)
            for j in range(2 * k, a + 1, k):
                numbers[j] = 0
    return primes


def main(n):
    # 根据 n 生成测试数据：这里直接使用传入的 n 作为规模
    limit = max(10**6, n)  # 确保筛子上界足够大
    all_primes = resheto(limit)
    for i in range(2, n):
        if i not in all_primes and (n - i) not in all_primes:
            # print(i, n - i)
            pass
            break


if __name__ == "__main__":
    # 示例：可自己修改 n 测试
    main(100)