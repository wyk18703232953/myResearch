import random

def main(n: int):
    # 1. 生成测试数据：两条由 '0' 和 'X' 组成的字符串，各长度为 n
    s1 = ''.join(random.choice(['0', 'X']) for _ in range(n))
    s2 = ''.join(random.choice(['0', 'X']) for _ in range(n))

    # 2. 原逻辑改写（去掉 input()）
    # l, r = [{'0': 1, 'X': 0}[c] for cc in zip(input(), input()) for c in cc], 0
    mapping = {'0': 1, 'X': 0}
    l = [mapping[c] for cc in zip(s1, s2) for c in cc]
    r = 0
    for i in range(0, len(l) - 3, 2):
        s = 7 - sum(l[i:i + 4])
        if s < 5:
            r += 1
            l[i:i + s] = [0] * s

    print(r)

if __name__ == "__main__":
    # 示例：n = 10，可按需修改
    main(10)