inf = 10**9

def generate_strings(n):
    # 生成 n 个只含 '(' 和 ')' 的确定性字符串
    # 第 j 个字符串长度为 j+1，模式为：前半段 '('，后半段 ')'
    strings = []
    for j in range(n):
        length = j + 1
        half = length // 2
        s = "(" * half + ")" * (length - half)
        strings.append(s)
    return strings

def process_strings(strings):
    n = len(strings)
    t = [0] * n
    m = {}
    for j in range(n):
        s = strings[j]
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
    for val in t:
        if val >= 0:
            if -val in m:
                res += m[-val]
    return res

def main(n):
    strings = generate_strings(n)
    result = process_strings(strings)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)