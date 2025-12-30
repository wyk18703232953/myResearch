import random

def main(n: int):
    """
    n 为规模参数，用于控制生成测试数据的范围。
    这里简单设定：生成一个长度在 [2, max(3, n)] 之间的随机整数的字符串 r。
    """
    # 为避免长度过小或无意义，这里做一个下限控制
    length = max(2, min(18, n))  # 防止数字过大导致 int 转换超出实际使用场景
    # 确保首位非 0
    first_digit = str(random.randint(1, 9))
    other_digits = ''.join(str(random.randint(0, 9)) for _ in range(length - 1))
    r = first_digit + other_digits

    # 原始逻辑
    t1 = int(r)
    t2 = int(r[:len(r) - 1])           # 去掉最后一位
    t3 = int(r[:len(r) - 2] + r[-1])   # 去掉倒数第二位

    print(max(t1, t2, t3))


if __name__ == "__main__":
    # 示例：可以修改这里的 n 来测试不同规模
    main(10)