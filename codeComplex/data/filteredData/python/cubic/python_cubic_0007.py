import random
import string

def main(n: int):
    # 生成长度为 n 的随机小写字母串作为测试数据
    S = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    best = 0
    for i in range(len(S)):
        for j in range(i + 1, len(S) + 1):
            s = S[i:j]
            c = 0
            for k in range(len(S)):
                if S[k:].startswith(s):
                    c += 1
            if c >= 2:
                best = max(best, len(s))
    print(best)

if __name__ == "__main__":
    # 示例：规模 n = 20
    main(20)