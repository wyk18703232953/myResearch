import random

def main(n: int):
    # 1. 根据 n 生成测试数据串 a
    # 规则示例：随机生成由 'H' 和 'T' 组成的长度为 n 的字符串，
    # 且保证至少有一个 'T'，以避免原逻辑中 b=0 的退化情况。
    if n <= 0:
        print(0)
        return

    # 至少一个 'T'
    pos_T = random.randrange(n)
    chars = []
    for i in range(n):
        if i == pos_T:
            chars.append('T')
        else:
            chars.append(random.choice(['H', 'T']))
    a = ''.join(chars)

    # 2. 原始逻辑
    b = a.count('T')
    c = -1
    for i in range(n):
        d = 0
        for j in range(b):
            d += int(a[(i + j) % n] == 'H')
        if c == -1 or d < c:
            c = d

    # 3. 输出结果
    print(c)

# 示例调用（提交平台通常只调用 main）
if __name__ == "__main__":
    main(10)