def Is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def core_logic(n):
    for i in range(2, 100):
        if not Is_prime(i) and not Is_prime(n - i):
            return i, n - i
    return None, None


def main(n):
    # 将 n 映射为原程序中的单个整数输入规模
    # 使用一个简单的确定性算式生成测试值
    test_value = 4 + 2 * n  # 保证为偶数且随 n 线性增长
    a, b = core_logic(test_value)
    if a is not None:
        # print(a, b)
        pass

    else:
        # print("No pair found")
        pass
if __name__ == "__main__":
    # 示例调用，可按需修改 n 的大小做时间复杂度实验
    main(10)