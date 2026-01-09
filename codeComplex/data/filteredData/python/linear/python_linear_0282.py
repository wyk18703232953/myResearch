inf = 10**9

def main(n):
    t = [0] * n
    m = {}
    for j in range(n):
        # 生成第 j 个字符串，长度依赖 n，内容确定性构造
        # 这里构造一个长度为 n 的括号串，模式为若干 "(" 后接若干 ")"
        k = j % (n + 1)  # 前缀 "(" 的数量
        s = "(" * k + ")" * (n - k)

        bal = 0
        req = 0

        for ch in s:
            if ch == ")":
                bal -= 1

            else:
                if bal < 0:
                    req += bal
                    bal = 1

                else:
                    bal += 1

        if req < 0:
            if bal > 0:
                req = inf

            else:
                req += bal

        else:
            req = bal

        t[j] = req

        if req not in m:
            m[req] = 1

        else:
            m[req] += 1

    res = 0
    for x in t:
        if x >= 0:
            if -x in m:
                res += m[-x]

    # print(res)
    pass
if __name__ == "__main__":
    main(10)