def lr(a):
    l = [0] * len(a)
    r = [0] * len(a)
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[j] > a[i]:
                r[i] += 1
            if a[i] > a[j]:
                l[j] += 1
    return l, r


def main(n):
    if n <= 0:
        print("NO")
        return

    # Deterministic generation of l and r for a permutation a of [1..n]
    # We construct a simple pattern permutation:
    # a = [2, 4, 6, ..., even..., odd..., 1]
    # which is fully determined by n.
    a = list(range(2, n + 1, 2)) + list(range(1, n + 1, 2))
    l, r = lr(a)

    # Now run the original reconstruction logic using l, r as if they were input.
    a_rec = [0] * n
    for i in range(n):
        for j in range(n):
            if l[j] + r[j] == i:
                a_rec[j] = n - i
    l1, r1 = lr(a_rec)
    if l1 != l or r1 != r:
        print("NO")
    else:
        print("YES")
        print(" ".join(str(x) for x in a_rec))


if __name__ == "__main__":
    main(5)