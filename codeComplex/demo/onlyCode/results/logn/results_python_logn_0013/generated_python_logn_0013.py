import random

def main(n: int):
    # 1. 生成测试数据：根据规模 n 生成两个整数的字符串 a, b
    # 这里用 n 的位数上限来控制数据规模：a, b 为 [0, 2^n - 1] 之间的整数
    if n <= 0:
        a, b = "0", "0"
    else:
        max_val = (1 << n) - 1
        a_int = random.randint(0, max_val)
        b_int = random.randint(0, max_val)
        a, b = str(a_int), str(b_int)

    # 2. 原始逻辑
    if a == b:
        print("0")
        return

    xor = bin(int(a) ^ int(b))[2:]
    a_bin = bin(int(a))[2:]
    b_bin = bin(int(b))[2:]
    ans = ""

    if a_bin[0] == b_bin[0]:
        ans += "0"
    else:
        ans += "1"

    for _ in range(len(xor)):
        ans += "1"

    print(int(ans, 2))


if __name__ == "__main__":
    # 示例：可修改 n 来控制生成数据的规模（位数上限）
    main(10)