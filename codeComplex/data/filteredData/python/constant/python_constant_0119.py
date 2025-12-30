import random

def main(n: int):
    # 根据规模 n 生成测试数据：长度为 n 的随机整数（含正负号）
    # 确保 n >= 1；若 n < 1，则默认给一个简单字符串
    if n < 1:
        s = "0"
    else:
        # 随机决定是否为负数
        is_negative = random.choice([True, False])
        if n == 1:
            # 只有一位时，若为负，只能是 "0"（否则长度会>1）
            if is_negative:
                s = "0"
            else:
                s = str(random.randint(0, 9))
        else:
            # 生成 (n-1) 位的非负整数（首位不为0，除非长度为1）
            first_digit = random.randint(1, 9)
            rest_digits = [random.randint(0, 9) for _ in range(n - 2)]
            num_str = str(first_digit) + "".join(str(d) for d in rest_digits)
            if is_negative:
                s = "-" + num_str
            else:
                s = num_str

    # 以下是原逻辑
    n = len(s)
    if s[0] == '-':
        if s[n - 1] < s[n - 2]:
            s = s[::-1]
            s = s.replace(s[1], "", 1)
            s = s[::-1]
        else:
            s = s[::-1]
            s = s.replace(s[0], "", 1)
            s = s[::-1]
        if s == "-0":
            print("0")
        else:
            print(s)
    else:
        print(s)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)