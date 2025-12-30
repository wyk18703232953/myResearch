import random

def main(n: int):
    # 根据 n 生成测试数据：行数 n，二进制字符串长度 m
    # 这里设定 m = max(1, n)；可按需要调整规则
    m = max(1, n)

    # 生成 n 个长度为 m 的随机二进制字符串
    # 每位为 '0' 或 '1'，并转为整数
    a = []
    for _ in range(n):
        bits = ''.join(random.choice('01') for _ in range(m))
        a.append(int(bits, 2))

    s = 0
    t = 0
    for x in a:
        t |= s & x
        s |= x

    # 完全保留原逻辑和输出形式
    print(('YES', 'NO')[all(x & s & ~t for x in a)])


if __name__ == "__main__":
    # 示例：调用 main(5)，实际使用时可按需调用 main(n)
    main(5)