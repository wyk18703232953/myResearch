import sys

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

def generate_data(n):
    if n < 1:
        n = 1
    # generate four lists of n binary strings of length n deterministically
    def gen_list(offset):
        res = []
        for i in range(n):
            val = (i * 37 + offset * 101) & ((1 << n) - 1)
            res.append(format(val, '0{}b'.format(n)))
        return res

    l1 = gen_list(1)
    l2 = gen_list(2)
    l3 = gen_list(3)
    l4 = gen_list(4)
    return l1, l2, l3, l4

def main(n):
    l1, l2, l3, l4 = generate_data(n)

    z = []
    s = 0
    for i in range(n):
        if i % 2 == 1:
            s += (2 ** i)
    z.append(s)
    z.append(z[0] ^ (2 ** n - 1))

    ans = m = sys.maxsize
    for i in range(2, 17):
        s_bin = check(i)
        if s_bin.count("1") == 2:
            s_bin = (4 - len(s_bin)) * "0" + s_bin
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

                if s_bin[j] == "1":
                    res += min(res, solve(1, n, x, z))

                else:
                    res += min(res, solve(0, n, x, z))
            ans = min(ans, res - m)
    # print(ans)
    pass
if __name__ == "__main__":
    main(5)