import random
import string

def main(n: int):
    # 生成测试参数 k，范围 [1, 26]，且不大于 n
    if n <= 0:
        print(0)
        return
    k = random.randint(1, min(26, n))

    # 生成长度为 n 的随机大写字母串 s
    s = ''.join(random.choice(string.ascii_uppercase) for _ in range(n))

    # 原逻辑
    m = 10 ** 10
    for i in range(k):
        c = chr(ord('A') + i)
        m = min(m, s.count(c))
    print(m * k)

if __name__ == "__main__":
    # 示例：可自行修改 n 以测试不同规模
    main(100)