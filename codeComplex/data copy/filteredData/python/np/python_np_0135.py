def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def main(n):
    # 生成规模为 n 的确定性输入数据
    l = [i + 2 for i in range(n)]
    c = [i % 7 + 1 for i in range(n)]

    a = {0: 0}
    b = [0]

    for i in range(n):
        for p in b:
            d = gcd(p, l[i])
            cost = a[p] + c[i]
            if d not in a:
                a[d] = cost
                b.append(d)
            elif a[d] > cost:
                a[d] = cost

    if 1 not in a:
        a[1] = -1
    print(a[1])

if __name__ == "__main__":
    main(10)