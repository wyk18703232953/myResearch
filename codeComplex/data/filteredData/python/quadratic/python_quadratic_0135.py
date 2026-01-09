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

def main(n):
    # Deterministic generation of l1..l4
    # Each list has n binary strings of length n
    def gen_list(offset):
        res = []
        for i in range(n):
            val = (i + offset) % (1 << n) if n < 30 else (i + offset)
            s = bin(val)[2:]
            if len(s) < n:
                s = "0" * (n - len(s)) + s

            else:
                s = s[-n:]
            res.append(s)
        return res

    l1 = gen_list(0)
    l2 = gen_list(1)
    l3 = gen_list(2)
    l4 = gen_list(3)

    z = []
    s_val = 0
    for i in range(n):
        if i % 2 == 1:
            s_val += (2 ** i)
    z.append(s_val)
    z.append(z[0] ^ (2 ** n - 1))

    ans = m = sys.maxsize
    for i_val in range(2, 17):
        s = check(i_val)
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
    # print(ans)
    pass
if __name__ == "__main__":
    main(5)