def main(n):
    # n controls the size of arrays a and b (both of length n)
    # Values are chosen from 1..n to ensure pos_of index safety
    a = [((i * 2) % n) + 1 for i in range(n)]
    # Make a a permutation-like sequence by simple deterministic transform
    used = [False] * (n + 1)
    perm_a = []
    for x in a:
        if not used[x]:
            perm_a.append(x)
            used[x] = True
    # fill remaining numbers
    for v in range(1, n + 1):
        if not used[v]:
            perm_a.append(v)
            used[v] = True
    a = perm_a

    # b is another deterministic sequence derived from a and indices
    b = [a[i] if i % 2 == 0 else ((i * 3) % n) + 1 for i in range(n)]

    max_val = max(max(a), max(b)) if n > 0 else 0
    size = max(2 * 10**5 + 1, max_val + 1)
    pos_of = [-1 for _ in range(size)]

    for i, ele in enumerate(a):
        pos_of[ele] = i + 1

    current_pos = 0
    ans = []
    for x in b:
        if pos_of[x] > current_pos:
            ans.append(pos_of[x] - current_pos)
            current_pos = pos_of[x]

        else:
            ans.append(0)

    # print(' '.join(map(str, ans)))
    pass
if __name__ == "__main__":
    main(10)