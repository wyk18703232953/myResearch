def main(n):
    from collections import Counter

    # Ensure n is non-negative
    if n <= 0:
        # print(0)
        pass
        # print()
        pass
        return

    # Deterministic generation of s and t of length n
    # s: cyclic 'a'..'z'
    s = [chr(ord('a') + (i % 26)) for i in range(n)]
    # t: a deterministic permutation of s by reversing blocks of size 3
    t = s[:]  # same multiset of characters

    def transform_by_blocks(arr, block_size):
        res = arr[:]
        for start in range(0, len(res), block_size):
            end = min(start + block_size, len(res))
            res[start:end] = reversed(res[start:end])
        return res

    t = transform_by_blocks(t, 3)

    cs = Counter(s)
    ct = Counter(t)
    if cs != ct:
        # print(-1)
        pass
        return

    xs = [[] for _ in range(26)]
    xt = [[] for _ in range(26)]
    for i in range(n):
        j = ord(s[i]) - ord('a')
        xs[j].append(i)

    for i in range(n):
        j = ord(t[i]) - ord('a')
        xt[j].append(i)

    x = [-1] * n
    for i in range(26):
        for j_idx, k_idx in zip(xs[i], xt[i]):
            x[j_idx] = k_idx

    ans = []
    for i in range(n):
        for j in reversed(range(i + 1, n)):
            if x[j - 1] > x[j]:
                x[j - 1], x[j] = x[j], x[j - 1]
                ans.append(j)
    # print(len(ans))
    pass

    if ans:
        # print(*ans)
        pass

    else:
        # print()
        pass
if __name__ == "__main__":
    main(10)