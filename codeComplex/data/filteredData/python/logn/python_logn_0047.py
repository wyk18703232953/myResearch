import random

def main(n: int):
    # 生成规模为 n 的测试数据：
    # 使用 n 作为最大值，生成两个在 [0, n] 范围内的整数 m, k
    m = random.randint(0, n)
    k = random.randint(0, n)

    # 原逻辑开始
    res = m ^ k                  # 异或运算
    s = bin(res)                 # 转换为二进制字符串，如 '0b10101'
    s = s[2:]                    # 去掉 '0b' 前缀，如 '10101'
    s = int(s) if s != '' else 0 # 转换为整数（与原逻辑保持一致）

    if s == 0:
        print(0)
    else:
        s = str(s)
        res = (2 ** len(s)) - 1  # 计算 2^位数 - 1
        print(res)

if __name__ == "__main__":
    # 示例：可以在此处指定规模 n
    main(1000)