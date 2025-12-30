inf = 10**9

def main(n):
    import random

    # 根据 n 生成测试数据：n 个括号串，长度适中，可根据需要调整
    # 这里每个串长度在 [1, 2*n] 内随机生成
    strings = []
    for _ in range(n):
        length = random.randint(1, max(2, 2 * n))
        s = ''.join(random.choice('()') for _ in range(length))
        strings.append(s)

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
    for i in t:
        if i >= 0:
            if -i in m:
                res += m[-i]

    print(res)


if __name__ == "__main__":
    # 示例：调用 main(5)，可根据需要修改 n
    main(5)