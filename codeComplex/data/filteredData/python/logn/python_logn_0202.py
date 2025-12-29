import random

def main(n):
    # 1. 生成测试数据：随机生成 s，使得 1 <= s <= 10^n - 1
    # 为避免过大整数，n 过大时限制位数
    max_digits = min(n, 18)  # 控制数值大小在 Python 整型运算范围内更高效
    # 生成位数在 1 到 max_digits 之间的随机整数
    digits = random.randint(1, max_digits)
    s = random.randint(10**(digits - 1), 10**digits - 1)
    # 为了与原代码一致，n 和 s 应该是字符串形式参与逻辑
    n_str = str(n)
    s_str = str(s)

    # 2. 保留原逻辑（去掉 input），用生成的 s_str 和 n_str
    i = int(s_str)
    d_sum = sum(map(int, str(i)))
    while i - d_sum < int(s_str):
        i += 1
        d_sum = sum(map(int, str(i)))

    result = max(0, int(n_str) - i + 1)
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(1000) 规模为 1000，可按需修改
    main(1000)