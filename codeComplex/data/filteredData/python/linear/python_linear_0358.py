import random

def main(n: int):
    # 生成长度为 n 的随机数字串（包含 0-9）
    s = ''.join(str(random.randint(0, 9)) for _ in range(n))

    ans = 0
    c = 0
    l = []
    for i in range(n):
        a = int(s[i]) % 3
        if a == 0:
            ans += 1
            c = 0
            l = []
        else:
            if c == 0:
                l.append(int(s[i]))
                c += 1
            elif c == 1:
                if (a + l[0]) % 3 == 0:
                    ans += 1
                    c = 0
                    l = []
                else:
                    c += 1
            else:
                ans += 1
                c = 0
                l = []
    print(ans)


if __name__ == "__main__":
    # 示例：规模 n = 20
    main(20)