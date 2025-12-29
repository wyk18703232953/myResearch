import sys
import random


def check(n):
    count1 = 0
    s = ""
    while n != 0:
        if n % 2:
            count1 += 1
            s = "1" + s
        else:
            s = "0" + s
        n //= 2
    return s


def solve(flag, n, l, z):
    temp_ans = 0
    for i in range(n):
        y = (z[flag] ^ int(l[i], 2))
        b = bin(y)
        temp_ans += b.count("1")
        flag = not flag
    return temp_ans


def main(n):
    # 生成测试数据：n 行、每行 n 位的 0/1 串
    def gen_matrix(size):
        rows = []
        for _ in range(size):
            row = "".join(random.choice("01") for _ in range(size))
            rows.append(row)
        return rows

    l1 = gen_matrix(n)
    l2 = gen_matrix(n)
    l3 = gen_matrix(n)
    l4 = gen_matrix(n)

    z = []
    s = 0
    for i in range(n):
        if i % 2 == 1:
            s += (2 ** i)
    z.append(s)
    z.append(z[0] ^ (2 ** n - 1))

    ans = m = sys.maxsize
    for i in range(2, 17):
        s = check(i)
        if s.count("1") == 2:
            s = (4 - len(s)) * "0" + s
            res = sys.maxsize
            for j in range(4):
                if j == 0:
                    x = l1
                elif j == 1:
                    x = l2
                elif j == 2:
                    x = l3
                else:
                    x = l4

                if s[j] == "1":
                    res += min(res, solve(1, n, x, z))
                else:
                    res += min(res, solve(0, n, x, z))
            ans = min(ans, res - m)
    print(ans)