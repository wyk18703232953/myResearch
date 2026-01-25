def if_spruce(n, l, s):
    d = [0] * (n + 1)
    for i in range(1, n + 1):
        if i not in s:
            d[l[i]] += 1
    for i in range(1, n + 1):
        if i in s and d[i] < 3:
            return "No"
    return "Yes"


def main(n):
    if n < 2:
        n = 2
    l = [0, 0]
    for i in range(2, n + 1):
        parent = max(1, i // 2)
        l.append(parent)
    s = set(l)
    result = if_spruce(n, l, s)
    print(result)


if __name__ == "__main__":
    main(10)