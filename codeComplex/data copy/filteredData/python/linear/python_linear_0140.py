def f(ar):
    mx = ar.index(max(ar))
    cmark = 0
    ans = 0
    big = [0] * (len(ar))
    for i in range(len(ar) - 1, -1, -1):
        cmark = max(cmark - 1, ar[i] + 1, 0)
        big[i] = cmark
    cmark = 0
    t = [0] * (len(ar))
    for i in range(len(ar)):
        cmark = max(cmark, big[i])
        t[i] = cmark
    ans = 0
    for i in range(len(ar)):
        t[i] = t[i] - ar[i] - 1
    return sum(t)


def main(n):
    if n <= 0:
        ar = []

    else:
        ar = [i % 7 + i // 3 for i in range(n)]
    result = f(ar)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)