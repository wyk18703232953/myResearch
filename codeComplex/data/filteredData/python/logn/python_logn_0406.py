def main(n):
    import random

    # 生成测试数据：t 组 (n_i, k_i)
    # 这里让所有测试用例的 n_i = n，k_i 在 1 ~ 2^(2n) 范围内随机
    # 可按需要修改生成策略
    t = 5
    test_cases = []
    max_k = 1 << (2 * n)  # 2^(2n)，大致上界即可
    for _ in range(t):
        ni = n
        ki = random.randint(1, max_k)
        test_cases.append((ni, ki))

    for ni, ki in test_cases:
        if ni >= 40:
            print("YES " + str(ni - 1))
        else:
            ans = -1
            for m in range(1, ni + 1):
                asd = (4 ** m - 1) // 3
                asd2 = (2 ** m - 1) ** 2
                asd2 *= (4 ** (ni - m) - 1) // 3
                asd += asd2
                if asd >= ki and m * m <= ki:
                    ans = ni - m
                    break
            if ans == -1:
                print("NO")
            else:
                print("YES " + str(ans))


if __name__ == "__main__":
    # 示例：运行规模 n=10
    main(10)