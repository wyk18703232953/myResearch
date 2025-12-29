import random
import string

def main(n: int):
    # 生成长度为 n 的随机字符串，字符从小写字母中选
    t = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    n = len(t)
    maxi = 0

    for i in range(n):
        s = t[i]
        if t.count(s) > 1:
            maxi = max(maxi, 1)
        nr = 1
        for j in range(i + 1, n):
            s += t[j]
            nr += 1
            g = 0
            for h in range(n - nr + 1):
                if s == t[h:h + nr]:
                    g += 1
            if g > 1:
                maxi = max(nr, maxi)

    print(maxi)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)