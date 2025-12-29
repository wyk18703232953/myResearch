import random

def main(n):
    # 1. 生成测试数据
    # a 为字符串长度，设为 n
    a = n
    # 随机生成一个由 'H' 和 'T' 组成的长度为 a 的字符串
    # 保证至少有一个 'H'，否则和原逻辑行为不明显
    if a <= 1:
        s = 'H'
    else:
        # 至少放一个 'H'
        s_list = ['H'] + [random.choice(['H', 'T']) for _ in range(a - 1)]
        random.shuffle(s_list)
        s = ''.join(s_list)

    # 2. 原始逻辑
    d = s.count('H')
    p = []
    for i in range(len(s)):
        if i + d > len(s):
            n_over = d + i - len(s)
            m = d - n_over
            h = s[:m] + s[-n_over:]
            k = h.count("T")
            p.append(k)
        else:
            h = s[i:d + i]
            k = h.count("T")
            p.append(k)

    mi = a
    for i in range(len(p)):
        if p[i] < mi:
            mi = p[i]

    if s.count("H") == 1 or s.count("T") == 0:
        print(0)
    else:
        print(mi)

    # 如需调试，可打印生成的 s：
    # print("s =", s)

# 示例：运行 main(10)
if __name__ == "__main__":
    main(10)