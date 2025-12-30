base = 998244353

def power(x, y):
    if y == 0:
        return 1
    t = power(x, y // 2)
    t = (t * t) % base
    if y % 2:
        t = (t * x) % base
    return t

def inverse(x):
    return power(x, base - 2)

def main(n):
    # 生成测试数据：长度为 n 的数组 a，元素为 -1 或 1..n
    # 这里给一个简单的可重复生成方式：前一半为 -1，后一半为 1..(n - n//2)
    a = [0]
    half = n // 2
    for i in range(1, n + 1):
        if i <= half:
            a.append(-1)
        else:
            # 保证在 [1, n] 范围内
            a.append(i - half)

    # Fenwick 树大小按 n 即可
    size = n
    ft = [0] * (size + 2)

    def get(i):
        res = 0
        while i <= size:
            res += ft[i]
            i += i & -i
        return res

    def update(i, x):
        while i > 0:
            ft[i] += x
            i -= i & -i

    neg = [0]
    non = [0]

    for _ in range(1, n + 1):
        non.append(0)

    for i in range(1, n + 1):
        if a[i] != -1:
            non[a[i]] += 1

    for i in range(1, n + 1):
        non[i] += non[i - 1]

    for i in range(1, n + 1):
        if a[i] == -1:
            neg.append(neg[i - 1] + 1)
        else:
            neg.append(neg[i - 1])

    m = neg[n]
    ans = 0
    for i in range(1, n + 1):
        if a[i] != -1:
            ans += get(a[i])
            update(a[i], 1)

    fm = 1
    fs = fm
    for i in range(1, m + 1):
        fs = fm
        fm = (fm * i) % base
    fs = (fs * inverse(fm)) % base

    for i in range(1, n + 1):
        if a[i] != -1:
            less = a[i] - non[a[i]]
            more = m - less
            ans = (ans + neg[i] * more * fs) % base
            ans = (ans + (m - neg[i]) * less * fs) % base

    ans = (ans + m * (m - 1) * inverse(4)) % base
    print(ans)

# 示例调用
# main(10)