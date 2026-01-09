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
        # print("NO")
        pass
        return

    # Deterministic construction of a permutation a of size n
    # Example: a is descending sequence from n to 1
    a = [n - i for i in range(n)]

    # Compute l and r using the same logic as lr
    l, r = lr(a)

    # Reconstruct a2 from l and r using original algorithm logic
    a2 = [0] * n
    for i in range(n):
        for j in range(n):
            if l[j] + r[j] == i:
                a2[j] = n - i

    l1, r1 = lr(a2)
    if l1 != l or r1 != r:
        # print("NO")
        pass

    else:
        # print("YES")
        pass
        # print(' '.join(str(i) for i in a2))
        pass
if __name__ == "__main__":
    main(5)