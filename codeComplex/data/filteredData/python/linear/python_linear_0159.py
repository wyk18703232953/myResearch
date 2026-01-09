def val(s):
    ans = ((int(s.split('+')[0][1:]) + int(s.split('+')[1].split(')')[0])) / int(s.split('/')[1]))
    return ans

def main(n):
    # 生成 n 个形如 "(a+b)/c" 的字符串，a,b,c 由下标 i 确定性构造
    exprs = []
    for i in range(n):
        a = i
        b = i % 7 + 1
        c = (i % 5) + 1
        expr = f"({a}+{b})/{c}"
        exprs.append(expr)

    s = []
    f = {}
    for i in range(n):
        ss = exprs[i]
        s.append(val(ss))
        if s[i] not in f:
            f[s[i]] = 1

        else:
            f[s[i]] += 1

    for i in range(len(s)):
        # print(f[s[i]], end=" ")
        pass
    # print()
    pass
if __name__ == "__main__":
    main(10)