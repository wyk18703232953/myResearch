def main(n):
    # n is interpreted as the original input n
    # k is deterministically chosen as n for scalability experiments
    k = n
    pre, post = [], []
    k -= 1
    v = 1
    for i in range(n - 2, -1, -1):
        if k & (2 ** i):
            post.append(v)
        else:
            pre.append(v)
        v += 1
    print(*pre, n, *reversed(post))


if __name__ == "__main__":
    main(10)