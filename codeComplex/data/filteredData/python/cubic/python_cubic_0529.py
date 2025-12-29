import random

def main(n: int):
    # 1. 生成规模为 n 的测试数据
    # 生成一个由 n 个数字字符组成的字符串（允许重复），并生成一个上界整数 b
    digits = [str(random.randint(0, 9)) for _ in range(n)]
    a = sorted(digits)
    # 生成 b，使得 b 至少不小于当前数字，避免过多无效回退
    c_init = int("".join(a))
    # b 在 [c_init, c_init + 10^n) 区间随机
    b = c_init + random.randint(0, 10**max(1, n) - 1)

    # 2. 原始逻辑
    a, b = a, int(b)
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            c = int("".join(a))
            a[i], a[j] = a[j], a[i]
            d = int("".join(a))
            if c <= d <= b:
                continue
            else:
                a[i], a[j] = a[j], a[i]
    print("".join(a))


if __name__ == "__main__":
    # 示例：规模为 5
    main(5)