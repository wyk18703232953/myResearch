def inn1(s1, xmi1, xma1, ymi1, yma1, c2):
    t = False
    for i in s1:
        if i[0] >= xmi1 and i[0] <= xma1 and i[1] >= ymi1 and i[1] <= yma1:
            t = True
            break
    if c2[0] >= xmi1 and c2[0] <= xma1 and c2[1] >= ymi1 and c2[1] <= yma1:
        t = True
    return t

def inn2(s, xmi2, xma2, ymi2, yma2, c1):
    t = False
    for i in s:
        if i[0] >= xmi2 and i[0] <= xma2 and i[1] >= ymi2 and i[1] <= yma2:
            t = True
            break
    if c1[0] >= xmi2 and c1[0] <= xma2 and c1[1] >= ymi2 and c1[1] <= yma2:
        t = True
    return t

def conv(s):
    for i in range(4):
        x = s[i][0]
        y = s[i][1]
        s[i][0] = x + y
        s[i][1] = x - y
    return s

def run_once(s, s1):
    st = set()
    for i in s:
        st.add(i[1])

    xma1 = s[0][0]
    xma2 = s1[0][0]
    xmi1 = s[0][0]
    xmi2 = s1[0][0]
    yma1 = s[0][1]
    yma2 = s1[0][1]
    ymi1 = s[0][1]
    ymi2 = s1[0][1]

    for i in range(4):
        xma1 = max(xma1, s[i][0])
        xma2 = max(xma2, s1[i][0])
        xmi1 = min(xmi1, s[i][0])
        xmi2 = min(xmi2, s1[i][0])
        yma1 = max(yma1, s[i][1])
        yma2 = max(yma2, s1[i][1])
        ymi1 = min(ymi1, s[i][1])
        ymi2 = min(ymi2, s1[i][1])

    c1 = [(xma1 + xmi1) / 2, (yma1 + ymi1) / 2]
    c2 = [(xma2 + xmi2) / 2, (yma2 + ymi2) / 2]

    t = False
    if len(st) == 2:
        t = True

    if t:
        t1 = inn1(s1, xmi1, xma1, ymi1, yma1, c2)
        s = conv(s)
        s1 = conv(s1)

        xma1 = s[0][0]
        xma2 = s1[0][0]
        xmi1 = s[0][0]
        xmi2 = s1[0][0]
        yma1 = s[0][1]
        yma2 = s1[0][1]
        ymi1 = s[0][1]
        ymi2 = s1[0][1]

        for i in range(4):
            xma1 = max(xma1, s[i][0])
            xma2 = max(xma2, s1[i][0])
            xmi1 = min(xmi1, s[i][0])
            xmi2 = min(xmi2, s1[i][0])
            yma1 = max(yma1, s[i][1])
            yma2 = max(yma2, s1[i][1])
            ymi1 = min(ymi1, s[i][1])
            ymi2 = min(ymi2, s1[i][1])

        c1 = [(xma1 + xmi1) / 2, (yma1 + ymi1) / 2]
        c2 = [(xma2 + xmi2) / 2, (yma2 + ymi2) / 2]
        t2 = inn2(s, xmi2, xma2, ymi2, yma2, c1)

    else:
        t1 = inn2(s, xmi2, xma2, ymi2, yma2, c1)
        s = conv(s)
        s1 = conv(s1)

        xma1 = s[0][0]
        xma2 = s1[0][0]
        xmi1 = s[0][0]
        xmi2 = s1[0][0]
        yma1 = s[0][1]
        yma2 = s1[0][1]
        ymi1 = s[0][1]
        ymi2 = s1[0][1]

        for i in range(4):
            xma1 = max(xma1, s[i][0])
            xma2 = max(xma2, s1[i][0])
            xmi1 = min(xmi1, s[i][0])
            xmi2 = min(xmi2, s1[i][0])
            yma1 = max(yma1, s[i][1])
            yma2 = max(yma2, s1[i][1])
            ymi1 = min(ymi1, s[i][1])
            ymi2 = min(ymi2, s1[i][1])

        c1 = [(xma1 + xmi1) / 2, (yma1 + ymi1) / 2]
        c2 = [(xma2 + xmi2) / 2, (yma2 + ymi2) / 2]
        t2 = inn1(s1, xmi1, xma1, ymi1, yma1, c2)

    return t1 or t2

def generate_instance(k):
    base = k * 2
    s = []
    s1 = []
    for i in range(4):
        x = base + i
        y = base + (i % 2) * 3
        s.append([x, y])
    for i in range(4):
        x = base + 10 + i
        y = base + 5 + (i % 2) * 2
        s1.append([x, y])
    return s, s1

def main(n):
    # n 表示要执行的独立测试次数
    results = []
    for k in range(1, n + 1):
        s, s1 = generate_instance(k)
        res = run_once(s, s1)
        results.append(res)
    yes_count = sum(1 for r in results if r)
    no_count = n - yes_count
    # print(yes_count, no_count)
    pass
if __name__ == "__main__":
    main(10)