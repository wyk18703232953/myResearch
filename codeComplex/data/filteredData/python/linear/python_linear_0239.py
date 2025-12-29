import random
import string

def main(n: int):
    # 1. 生成测试数据
    # 为了与原逻辑一致，三串长度应相同，且只使用大小写字母
    # 这里设长度为 n（你可以按需要调整规则）
    l = n
    letters = string.ascii_letters  # A-Z a-z
    st_a = ''.join(random.choice(letters) for _ in range(l))
    st_b = ''.join(random.choice(letters) for _ in range(l))
    st_c = ''.join(random.choice(letters) for _ in range(l))

    # 2. 原算法逻辑
    a = [0 for _ in range(125)]
    b = [0 for _ in range(125)]
    c = [0 for _ in range(125)]

    for i in range(l):
        a[ord(st_a[i])] += 1
        b[ord(st_b[i])] += 1
        c[ord(st_c[i])] += 1

    maxi_a = 0
    maxi_b = 0
    maxi_c = 0

    if n == 1:
        maxi_a = max(a) + 1
        maxi_b = max(b) + 1
        maxi_c = max(c) + 1
        if maxi_a > l:
            maxi_a -= 2
        if maxi_b > l:
            maxi_b -= 2
        if maxi_c > l:
            maxi_c -= 2
    else:
        for i in range(123):
            if (65 <= i <= 90) or (97 <= i <= 122):
                if a[i] + n >= l:
                    maxi_a = max(maxi_a, l)
                else:
                    maxi_a = max(maxi_a, a[i] + n)

                if b[i] + n >= l:
                    maxi_b = max(maxi_b, l)
                else:
                    maxi_b = max(maxi_b, b[i] + n)

                if c[i] + n >= l:
                    maxi_c = max(maxi_c, l)
                else:
                    maxi_c = max(maxi_c, c[i] + n)

    s = [maxi_a, maxi_b, maxi_c]
    s.sort()
    if s[1] == s[2]:
        print("Draw")
    if maxi_a > max(maxi_b, maxi_c):
        print("Kuro")
    if maxi_b > max(maxi_c, maxi_a):
        print("Shiro")
    if maxi_c > max(maxi_b, maxi_a):
        print("Katie")


if __name__ == "__main__":
    # 示例：调用 main(3)
    main(3)