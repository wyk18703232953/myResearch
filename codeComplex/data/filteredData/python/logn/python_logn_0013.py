import random

def main(n: int):
    # 生成规模为 n 的测试数据：两个 n 位二进制整数（去掉前导 0 的影响，保证长度为 n）
    if n <= 0:
        return

    # 生成两个 n 位二进制字符串，最高位不为 0，避免转 int 时缩短长度
    a_bin = '1' + ''.join(random.choice('01') for _ in range(n - 1))
    b_bin = '1' + ''.join(random.choice('01') for _ in range(n - 1))

    a = a_bin
    b = b_bin

    if a == b:
        print("0")
    else:
        xor = bin(int(a) ^ int(b))[2:]
        a = bin(int(a))[2:]
        b = bin(int(b))[2:]
        ans = ""
        if a[0] == b[0]:
            ans += "0"
        else:
            ans += "1"
        for _ in range(len(xor)):
            ans += "1"
        print(int(ans, 2))


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)