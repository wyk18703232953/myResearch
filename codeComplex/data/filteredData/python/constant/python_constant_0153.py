def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def main(n):
    # 这里直接使用传入的 n 作为规模参数
    # 原逻辑：给定 n，输出两个合数之和为 n（偶数时固定 4 + (n-4)，奇数时枚举）
    if n % 2 == 0:
        print('4', n - 4)
    else:
        i = 4
        while i <= n // 2 + 1:
            k = n - i
            if not isPrime(k):
                print(i, k)
                break
            i += 2


if __name__ == "__main__":
    # 示例测试数据：可以根据需要调用 main(n)
    # 例如：测试 n 从 10 到 20
    for test_n in range(10, 21):
        print(f"n = {test_n}: ", end="")
        main(test_n)